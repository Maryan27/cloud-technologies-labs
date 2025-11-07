from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "maryan": "pass"
}

@auth.verify_password
def verify(username, password):
    if username in users and users[username] == password:
        return username
    return None

