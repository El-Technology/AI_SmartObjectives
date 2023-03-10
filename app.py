import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
#openai.api_key = "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"

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


#Read the key from the file
openai.api_key = open_file('openai_api_key.txt')

# Definition of the prompt for Chatgpt
bot_instruction = open_file('requestPrompt.txt')

#The instruction for the user
user_instruction = 'Kindly provide a brief description about your job or past your job description here...'


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

#prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



# def chatgpt_clone(input, history):
#     history = history or []
#     s = list(sum(history, ()))
#     s.append(input)
#     inp = ' '.join(s)
#     output = openai_create(bot_instruction+inp)
#     history.append((input, output))
#     return history, history

def chatgpt_clone(input, history):
    history = history or []
    output = openai_create(bot_instruction+input)
    history.append((input, output))
    return history, history

block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Create your own smart goals...</center></h1>""")
    gr.Markdown("""<p><center>Please briefly describe your job or past the Job description of your role within Kahramaa</center></p>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=user_instruction)
    state = gr.State()
    submit = gr.Button("SUBMIT")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)