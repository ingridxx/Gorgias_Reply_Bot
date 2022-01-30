import base64
import requests

user = 'yawanxu@gmail.com'
pw = 'd36f62d9277c1294a001f05765eda5276f78eca3d95d5236536efbf2122ff2ba'
base_url = 'https://bundleeats.gorgias.com/api/'


# replies to a ticket using the Gorgias REST API
def autoInternalNote(user, pw, ticket_id, internal_note):
    url = base_url + 'tickets/{ticket_id}/messages'.format(ticket_id=ticket_id)

    # Basic authentication
    auth = user + ':' + pw
    auth_bytes = auth.encode('ascii')
    auth64 = base64.b64encode(auth_bytes)
    auth_full = 'Basic {}'.format(auth64.decode())

    payload = {
        "sender": {"email": user},
        "via": "internal-note",
        "from_agent": True,
        "channel": "internal-note",
        "body_text": internal_note
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": auth_full
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    # print(response.text)


autoInternalNote(user, pw, '21799703', 'testing internal note')
