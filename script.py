import hashlib
import sys

import requests
import os

bot_token = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

def fetch_and_save_file(project_name, name, password, user, host, port: int, api: str):

    token_data = f"{host}:{project_name}:{user}:{name}"

    payload = {
        'project_name': project_name,
        'name': name,
        'password': password,
        'user': user,
        'host': host,
        'port': port,
        'auth_token': hashlib.sha256(token_data.encode('utf-8')).hexdigest()
    }
    res = requests.request('POST', api, data=payload,)

    if res.status_code != 200:
        requests.request(
            'POST',
            f'https://api.telegram.org/bot{bot_token}/sendMessage',
            data={
                'chat_id': chat_id,
                'text':  f'PROYEKT {project_name} \nERROR: {str(res.text)}\n'
            },
        )


if __name__ == "__main__":
    if len(sys.argv) != 8:
        sys.exit(1)

    fetch_and_save_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]), sys.argv[7])
