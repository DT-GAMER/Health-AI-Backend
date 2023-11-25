from openai import OpenAI

def get_openai_response(input_text):
  
  client = OpenAI(api_key="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")

  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
    {"role": "system", "content": "HealthPoint a diagnosis chatbot that also give precautions and only answers medical or health questions"},
    {"role": "user", "content": input_text}
    ]
  )
  return response.choices[0].message.content