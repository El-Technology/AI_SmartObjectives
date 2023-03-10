import os
import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openai_api_key.txt')


def request_func(prompt, engine='text-davinci-003',
                 temp=0.7,
                 top_p=1.0,
                 tokens=400,
                 freq_pen=0.0,
                 pres_pen=0.0,
                 stop=['IT Demand:', 'Requester:']
                 ):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    conversation = list()



while True:
    print('Kindly provide a brief description about your job or past your job description here...')
    user_input = input('\n')
    conversation.append('%s' % user_input)
    text_block = '\n'.join(conversation)
    prompt = open_file('requestPrompt.txt').replace('<<BLOCK>>', text_block)
    prompt = prompt + '\n'
    response = request_func(prompt)
    print(response)
    conversation.append('%s' % response)
    # print(conversation)
    print('\n'+'Do you want to recreate new SMART goals? (y/n)'+'\n')
    user_decision = input('')
    if user_decision == 'y':
        continue
    elif user_decision == 'n':
        break
