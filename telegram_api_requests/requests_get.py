from pprint import pprint

import requests

# GET, POST, PUT
# r = requests.get("https://api.github.com/events")
# print(r.status_code)
# print(dir(r))
# data = r.json()
# print(data[0]['actor']['display_login'])
# print(type(r.text))


token = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'
my_id = 591250245
get_me = requests.get(f'https://api.telegram.org/bot{token}/getMe')
get_updates = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
post_message = requests.post(
    f'https://api.telegram.org/bot{token}/sendMessage',
    data={'chat_id': my_id, 'text': 'Salom'}
)
print(post_message)
# print(get_me.status_code)
# print(get_updates.status_code)
# pprint(get_me.json())
# pprint(get_updates.json())











