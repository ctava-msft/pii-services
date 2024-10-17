import os
import requests
import json
import re
from faker import Faker
from dotenv import load_dotenv
load_dotenv()

# Initialize Faker
fake = Faker()

# Set environment variables
language_endpoint = os.getenv('LANGUAGE_ENDPOINT', '')
language_key = os.getenv('LANGUAGE_KEY', '')
print(language_endpoint)
print(language_key)

# Read the JSON data from the file
with open(r'.\lang.json', 'r') as file:
    data = json.load(file)
    print(data)

# Make the POST request
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': language_key
}
response = requests.post(f"{language_endpoint}/language/:analyze-text?api-version=2022-05-01", headers=headers, json=data)

# Check if the request was successful
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
    exit()
print(response)

# Function to replace text using offset and length
def replace_text(text, offset, length, replacement):
    return text[:offset] + replacement + text[offset + length:]

# Parse the response
response_data = response.json()
documents = response_data.get('results', {}).get('documents', [])

# Print the response data
print(response_data)

# Iterate through documents and replace phone numbers and emails
for document in documents:
    original_text = document.get('redactedText', '')
    entities = document.get('entities', [])
    
    for entity in entities:
        if entity['category'] == 'PhoneNumber':
            fake_phone = fake.phone_number()
            original_text = replace_text(original_text, entity['offset'], entity['length'], fake_phone)
        elif entity['category'] == 'Email':
            fake_email = fake.email()
            original_text = replace_text(original_text, entity['offset'], entity['length'], fake_email)


# Using regex to find 3-digit CVV
cvv_pattern = re.compile(r'\b(?!.*-)\d{3}\b') #re.compile(r'\b\d{3}\b')
cvv_matches = cvv_pattern.finditer(original_text)
for match in cvv_matches:
    print(f"CVV match: {match.group()} at position {match.start()} to {match.end()}")
    original_text = original_text[:match.start()] + '***' + original_text[match.end():]

# Print the modified text
print(original_text)
