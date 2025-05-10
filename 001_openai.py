from openai import OpenAI
import os
import yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']
print("Environment variables loaded")
client = OpenAI()
response = client.completions.create(
  model='gpt-4o-mini', 
  prompt="Me responda com a frase mais popular do mundo."
)

print(response)

message = (response.choices[0].text)
print(message)

