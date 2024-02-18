from openai import OpenAI
from config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

def generateResonse(prompt):
    messages = []
    messages.append({"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."})

    question = {
        'role' : 'user',
        'content' : prompt,
    }

    messages.append(question)

#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}

    response = client.chat.completions.create(model="gpt-3.5-turbo",messages=[messages])
    answer = response

    return answer

promt = "what is this?"
generateResonse(promt)