import base64
import requests
from getRequesterEmail import getRequesterEmail

user = 'yawanxu@gmail.com' # agent user
pw = 'd36f62d9277c1294a001f05765eda5276f78eca3d95d5236536efbf2122ff2ba'
base_url = 'https://bundleeats.gorgias.com/api/'

# replies to a ticket using the Gorgias REST API
def autoReplier(user, pw, ticket_id, txt):
    url = base_url + 'tickets/{ticket_id}/messages'.format(ticket_id=ticket_id)

    # Basic authentication
    auth = user + ':' + pw
    auth_bytes = auth.encode('ascii')
    auth64 = base64.b64encode(auth_bytes)
    auth_full = 'Basic {}'.format(auth64.decode())

    payload = {
        "source": {
            "from": {
                "address": user,
            },
            "to": [{
                "address": getRequesterEmail(ticket_id),
            }],

        },
        "via": "email",
        "from_agent": True,
        "channel": "email",
        "body_text": txt
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": auth_full
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    # print(response.text)

autoReplier(user, pw, '21799703', 'testing autoReplier')
