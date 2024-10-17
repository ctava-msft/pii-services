import json
import os
import requests
import time
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Initialize variables
language_endpoint = os.getenv('LANGUAGE_ENDPOINT', '')
language_key = os.getenv('LANGUAGE_KEY', '')

# Read the JSON data from the file
with open(r'.\conversation.json', 'r') as file:
    data = json.load(file)

# Make the POST request
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': language_key
}
response = requests.post(f"{language_endpoint}/language/analyze-conversations/jobs?api-version=2022-05-15-preview", headers=headers, json=data)

# Check and print the response
if response.status_code == 202:
    job_location = response.headers.get('Operation-Location')
    if job_location:
        while True:
            job_response = requests.get(job_location, headers=headers)
            if job_response.status_code == 200:
                job_result = job_response.json()
                status = job_result.get('status')
                if status == 'succeeded':
                    print("Job succeeded")
                    print(json.dumps(job_result, indent=2))
                    break
                elif status == 'failed':
                    print("Job failed")
                    print(json.dumps(job_result, indent=2))
                    break
                else:
                    print(f"Job status: {status}. Waiting for completion...")
                    time.sleep(5)  # Wait for 5 seconds before polling again
            else:
                print(f"Failed to get job status with status code {job_response.status_code}")
                print(job_response.text)
                break
    else:
        print("Failed to get job location from response headers")
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)