import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


def corrige(sentence):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {'role':'system', 'content':'Correct all the errors in the following sentence if you find any, as well as the sentence structure. Simply respond with the corrected sentence: '},
      {"role": "user", "content": sentence},    
    ],
  )
  return f"FIXE: {completion.choices[0].message.content}"


def chatgpt_answer(sentence):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Don't say your are an AI language model. Act like a person in a full-fledged conversation who wants to know more about the person they are talking to. Be short, between 10 and 40 words."},
      {"role": "user", "content": f"Answer to the next sentence and ask question or be dynamic!: {sentence}"},    
    ],
    temperature=0.4,
  )
  return completion.choices[0].message.content


fixed = corrige("Actually, i learn a lot about Docker and some tools like gitlab CI/CD and a little bit about Kuberbetes by its too complicate for me right now.")
print(fixed)
answer = chatgpt_answer(fixed)
print(answer)
    
    
 




