from fireworks.client import Fireworks

def ask(prompt):
    with open('API_KEY.txt', 'r', encoding='utf-8') as file:
        API_KEY = file.read()
    client = Fireworks(api_key=API_KEY)
    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
    )   
    return response.choices[0].message.content