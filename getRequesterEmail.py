import base64
import requests

user = 'yawanxu@gmail.com'
pw = 'd36f62d9277c1294a001f05765eda5276f78eca3d95d5236536efbf2122ff2ba'
base_url = 'https://bundleeats.gorgias.com/api/'

# retrieves requester's email given the ticket ID
def getRequesterEmail (ticket_id):
    url = base_url+'tickets/'+str(ticket_id)

    # Basic authentication
    auth = user + ':' + pw
    auth_bytes = auth.encode('ascii')
    auth64 = base64.b64encode(auth_bytes)
    auth_full = 'Basic {}'.format(auth64.decode())

    headers = {
        "Accept": "application/json",
        "Authorization": auth_full
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    return data['requester']['email']

