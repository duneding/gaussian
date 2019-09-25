import requests
import json
from requests.auth import HTTPBasicAuth
from random import randrange
import configuration.config as config

config = config.Config()

# Params for cases amount
AMOUNT_OF_PURCHASES = randrange(100, 500)
AMOUNT_OF_TOKENS = randrange(100, 500)
AMOUNT_OF_PURCHASES_WITH_TOKENS = randrange(100, 500)
AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST = randrange(100, 500)
AMOUNT_CREATE_SESSION_WITHOUT_CATEGORIES = randrange(100, 500)
AMOUNT_GET_PAYMENTS_METHODS_WITHOUT_METHODS = randrange(100, 500)
AMOUNT_AUTHORIZE_WITH_CARD_SUBMISSION_REQUIRED = randrange(100, 500)
AMOUNT_AUTHORIZE_WITH_PAYMENT_METHOD_MISMATCH = randrange(100, 500)
AMOUNT_CREATE_ORDER_WITH_BAD_REQUEST = randrange(100, 500)
AMOUNT_CUSTOMER_TOKEN_INTERNAL_ERROR = randrange(100, 500)


# Params for request
merchant_username_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'merchant_username'])
merchant_password_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'merchant_password'])
client_username_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'client_username'])
client_password_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'client_password'])
merchant_auth_pacs = HTTPBasicAuth(merchant_username_pacs, merchant_password_pacs)
client_auth_pacs = HTTPBasicAuth(client_username_pacs, client_password_pacs)
headers = {"content-type": "application/json"}

# PACS
create_session_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'create_session_endpoint'])
payment_methods_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'payment_methods_endpoint'])
authorize_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'authorize_endpoint'])
create_order_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-playground', 'create_order_endpoint'])

create_session_payload_pacs = open('mocks/create_session_payload_pacs.json', 'rb').read()
payment_method_payload_pacs = open('mocks/payment_method_payload_pacs.json', 'rb').read()
authorize_payload_pacs = open('mocks/authorize_payload_pacs.json', 'rb').read()
create_order_payload_pacs = open('mocks/create_order_payload_pacs.json', 'rb').read()


def post(endpoint, payload):
    return requests.post(endpoint, headers=headers, data=payload, auth=merchant_auth_pacs)


def get_json_from_payload(payload):
    return json.loads(payload.decode('utf8').replace("'", '"'))


def validate(validation):
    assert validation
    print("SUCCESS")


def trace(message, instance, max):
    print(message + ": " + str(instance) + " of " + str(max))


######### Generation Section #########


# Regular purchases with invoice in PACS
for i in range(0, AMOUNT_OF_PURCHASES):
    trace("Regular purchases with invoice in PACS", i, AMOUNT_OF_PURCHASES)
    create_session_response = post(create_session_endpoint_pacs, create_session_payload_pacs)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(payment_methods_endpoint_pacs.replace("{{session_id}}", session_id), payment_method_payload_pacs)
    authorize_response = post(authorize_endpoint_pacs.replace("{{session_id}}", session_id), authorize_payload_pacs)
    authorization_token = authorize_response.json()['external']['authorization_token']
    create_order_response = post(create_order_endpoint_pacs.replace("{{authorization_token}}", authorization_token), create_order_payload_pacs)
    validate(create_order_response.json()['order_id'] is not None)
