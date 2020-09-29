import json
import requests_oauthlib

def secure():
    path = '.../secret/'
    # Load Twitter API secrets from a json file
    secrets = json.loads(open(path + 'secrets.json').read())
    api_key = secrets['API_key']
    api_secret_key = secrets['API_secret_key']
    access_token = secrets['access_token']
    access_token_secret = secrets['access_token_secret']
    my_auth = requests_oauthlib.OAuth1(api_key, api_secret_key, access_token, access_token_secret)

    return my_auth
