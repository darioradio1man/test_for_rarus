import argparse
import json

import requests

with open('config.json') as conf_file:
    config = json.load(conf_file)

API_KEY = config['openai_api_key']
API_URL = config['api_url']


def request_prompt(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': config['model'],
        'messages': [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()

    if response.status_code == '200':
        return {"response": response_json['choices'][0]['message']['content']}
    else:
        return {"error": response_json.get('error', 'Unknown error occurred.')}


def main():
    parser = argparse.ArgumentParser(description="Just app.")
    parser.add_argument("--input", type=str, help="Your request", required=False)

    args = parser.parse_args()

    if args.input:
        response = request_prompt(args.input)
        print(f"{response=}")

    while True:
        user_input = input("Enter 'exit' for exit: ")
        if user_input.lower() == 'exit':
            break


if __name__ == "__main__":
    main()
