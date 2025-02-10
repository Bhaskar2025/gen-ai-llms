import openai
import os
from dotenv import load_dotenv
import requests

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable not set")
print("OpenAI API key loaded successfully.")

openai_model = "gpt-4o-mini"
llama_model = "llama3.2"

openai_system_prompt = ("You are an assistant who believes that the Sattu is the best drink. "
                        "Its very healthy. You are against Whey protein and other branded supplements. "
                        "Sattu is an Indian drink which is made of roasted chana powder and water "
                        "and very famous in northern India. You are a true supporter of Sattu. Now you "
                        "are in Sattu vs Whey Protein debate with other chatbot. Try to win the debate.")

llama_system_prompt = ("You are an assistant who believes that the Whey protein is the best drink. "
                        "Its very healthy. You are against Sattu and other desi supplements. "
                        "Sattu is an Indian drink which is made of roasted chana powder and water "
                        "and very famous in northern India. You are a true supporter of Whey Protein. Now you "
                        "are in Sattu vs Whey Protein debate with other chatbot. Try to win the debate.")

gpt_messages = ["Hi There"]
llama_messages = ["Hi"]

def call_gpt():
    messages = [{"role": "system", "content": openai_system_prompt}]
    for gpt, llama in zip(gpt_messages, llama_messages):
        messages.append({"role": "user", "content": gpt})
        messages.append({"role": "assistant", "content": llama})

    response = openai.chat.completions.create(
        model=openai_model,
        messages=messages
    )
    return response.choices[0].message.content


OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}


def call_llama():
    messages = [{"role": "system", "content": llama_system_prompt}]
    for gpt, llama in zip(gpt_messages, llama_messages):
        messages.append({"role": "user", "content": gpt})
        messages.append({"role": "assistant", "content": llama})
        messages.append({"role": "user", "content": gpt_messages[-1]})

    payload = {"model": llama_model, "messages": messages, "stream": False}

    llama_response = requests.post(
        OLLAMA_API,
        headers=HEADERS,
        json=payload)
    return llama_response.json()['message']['content']



print(f"GPT response:\n {gpt_messages[0]}\n")
print(f"Llama response:\n {llama_messages[0]}\n")

for i in range(3):
    gpt_next = call_gpt()
    print(f"GPT response:\n {gpt_next}\n")
    gpt_messages.append(gpt_next)

    llama_next = call_llama()
    print(f"Llama response:\n {llama_next}\n")
    llama_messages.append(llama_next)










