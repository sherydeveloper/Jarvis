from openai import OpenAI

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-None-qMRNz6mkBqJvCO1WDhUUT3BlbkFJL2Syh1GNusaRU45p640g",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant, named Jarvis skilled in general tasks like Alexa and google cloud."},
    {"role": "user", "content": "what is codding"}
  ]
)

print(completion.choices[0].message)