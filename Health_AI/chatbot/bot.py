from openai import OpenAI
from decouple import config

def get_openai_response(input_text):
    openai_api_key = config('OPENAI_API_KEY')

    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "HealthPoint a diagnosis chatbot that also give precautions and only answers medical or health questions"},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message.content

