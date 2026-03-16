from openai import OpenAI
import user_config
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

client = OpenAI(api_key=user_config.openai_key)

# Messages to send
messages = [
    {"role": "system", "content": "You are AIVA, a helpful AI assistant."},
    {"role": "user", "content": "Hello, AIVA!"}  # Example question
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

answer = response.choices[0].message.content
print(answer)
speak(answer)
