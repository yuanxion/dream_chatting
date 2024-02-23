import gradio as gr
import os
import random
import sys
import time

from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("silk-road/ChatHaruhi_RolePlaying_qwen_7b", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained("silk-road/ChatHaruhi_RolePlaying_qwen_7b", device_map="auto", trust_remote_code=True)
model = model.eval()

sys.path.append('../')
from ChatHaruhi import ChatHaruhi
db_folder = './content/libai'
system_prompt = './content/system_prompt-libai.txt'
bot_qf = ChatHaruhi( system_prompt = system_prompt,\
                  llm = 'openai' ,\
                  ) #story_db = db_folder)
role = '杜甫'

def get_response(chat_history):
    text, response = chat_history[-1]
    print(f'{text = } {response = }')
    #prompt = bot_qf.generate_prompt(role=role, text=text)
    prompt = bot_qf.generate_prompt(role=None, text=text)
    bot_qf.llm.print_prompt()
    response, history = model.chat(tokenizer, prompt, history=[])
    print(f'{type(response) = } {response = }')
    bot_qf.append_response(response)
    #chat_history.append((text, response))
    #return '', chat_history

    chat_history[-1][1] = ''
    for character in response:
        chat_history[-1][1] += character
        yield chat_history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("清除")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    #msg.submit(get_response, [msg, chatbot], [msg, chatbot])
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        get_response, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)


#demo.queue()
demo.launch()
