import requests

token = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'


def get_user_updates():
    get_updates = requests.get(f'https://api.telegram.org/bot{token}/getUpdates', params={'timeout': 1}).json()
    json_data = get_updates['result']
    print(len(json_data))
    if json_data:
        user_id = json_data[-1]['message']['from']['id']
        text = json_data[-1]['message']['text']
        # print(json_data[-1]['message'])
        send_to_user(user_id, text)


def send_to_user(user_id, text):
    requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage',
        data={'chat_id': user_id, 'text': text}
    )


def main():
    while True:
        get_user_updates()


if __name__ == '__main__':
    main()
