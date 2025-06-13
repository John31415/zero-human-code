from fireworks.client import Fireworks

def ask(prompt):
    with open('API_KEY.txt', 'r', encoding='utf-8') as file:
        API_KEY = file.read()
    client = Fireworks(api_key=API_KEY)
    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p3-70b-instruct",
        # model="accounts/fireworks/models/deepseek-r1", 
        # model="accounts/fireworks/models/mistral-7b-instruct-v3",
        # model="accounts/fireworks/models/deepseek-ai/deepseek-v3",
        # model="accounts/fireworks/models/llama-v3p2-3b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        top_p=0.9,
    )
    return response.choices[0].message.content