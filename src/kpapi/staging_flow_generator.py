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
merchant_username = config.value(['kpapi', 'ocay', 'eu-staging', 'merchant_username'])
merchant_password = config.value(['kpapi', 'ocay', 'eu-staging', 'merchant_password'])
client_username = config.value(['kpapi', 'ocay', 'eu-staging', 'client_username'])
client_password = config.value(['kpapi', 'ocay', 'eu-staging', 'client_password'])
merchant_username_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'merchant_username'])
merchant_password_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'merchant_password'])
client_username_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'client_username'])
client_password_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'client_password'])
merchant_auth = HTTPBasicAuth(merchant_username, merchant_password)
client_auth = HTTPBasicAuth(client_username, client_password)
merchant_auth_pacs = HTTPBasicAuth(merchant_username_pacs, merchant_password_pacs)
client_auth_pacs = HTTPBasicAuth(client_username_pacs, client_password_pacs)
headers = {"content-type": "application/json"}

# OCAY
create_session_endpoint = config.value(['kpapi', 'ocay', 'eu-staging', 'create_session_endpoint'])
payment_methods_endpoint = config.value(['kpapi', 'ocay', 'eu-staging', 'payment_methods_endpoint'])
authorize_endpoint = config.value(['kpapi', 'ocay', 'eu-staging', 'authorize_endpoint'])
create_order_endpoint = config.value(['kpapi', 'ocay', 'eu-staging', 'create_order_endpoint'])
create_customer_token_endpoint = config.value(['kpapi', 'ocay', 'eu-staging', 'create_customer_token_endpoint'])
create_customer_token_order_endpoint = config.value(['kpapi', 'ocay', 'eu-staging', 'create_customer_token_order_endpoint'])

# PACS
create_session_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'create_session_endpoint'])
payment_methods_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'payment_methods_endpoint'])
authorize_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'authorize_endpoint'])
create_order_endpoint_pacs = config.value(['kpapi', 'pacs', 'eu-staging', 'create_order_endpoint'])

token_ids = []
create_session_payload = open('mocks/create_session_payload.json', 'rb').read()
payment_method_payload = open('mocks/payment_method_payload.json', 'rb').read()
authorize_payload = open('mocks/authorize_payload.json', 'rb').read()
create_order_payload = open('mocks/create_order_payload.json', 'rb').read()
create_customer_token_payload = open('mocks/create_customer_token_payload.json', 'rb').read()
create_customer_token_order_payload = open('mocks/create_customer_token_order_payload.json', 'rb').read()
create_session_payload_pacs = open('mocks/create_session_payload_pacs.json', 'rb').read()
payment_method_payload_pacs = open('mocks/payment_method_payload_pacs.json', 'rb').read()
authorize_payload_pacs = open('mocks/authorize_payload_pacs.json', 'rb').read()
create_order_payload_pacs = open('mocks/create_order_payload_pacs.json', 'rb').read()


def post(auth, endpoint, payload):
    return requests.post(endpoint, headers=headers, auth=auth, data=payload)


def post_error(auth, endpoint, payload, status_code):
    response = post(auth, endpoint, json.dumps(payload))
    validate(response.status_code == status_code)


def get_json_from_payload(payload):
    return json.loads(payload.decode('utf8').replace("'", '"'))


def validate(validation):
    assert validation
    print("SUCCESS")


def trace(message, instance, max):
    print(message + ": " + str(instance) + " of " + str(max))


######### Generation Section #########

# Create Session with Bad Value
for i in range(0, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST):
    trace("Create Session with Bad Value", i, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST)
    json_payload = get_json_from_payload(create_session_payload)
    json_payload['purchase_country'] = "fake"
    post_error(merchant_auth, create_session_endpoint, json_payload, 400)

# Create Session with Bad Value at item level
for i in range(0, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST):
    trace("Create Session with Bad Value at item level", i, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST)
    json_payload = get_json_from_payload(create_session_payload)
    json_payload['order_lines'][0]['total_amount'] = 100001
    post_error(merchant_auth, create_order_endpoint, json_payload, 400)

# Create Session with Bad Value Order Amount
for i in range(0, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST):
    trace("Create Session with Bad Value Order Amount", i, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST)
    json_payload = get_json_from_payload(create_session_payload)
    json_payload['order_amount'] = "100009999"
    create_session_response = post(merchant_auth, create_session_endpoint, json.dumps(json_payload))
    post_error(merchant_auth, create_session_endpoint, json_payload, 400)

# Create Session with Bad Value Order Tax Amount
for i in range(0, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST):
    trace("Create Session with Bad Value Order Tax Amount", i, AMOUNT_CREATE_SESSION_WITH_BAD_REQUEST)
    json_payload = get_json_from_payload(create_session_payload)
    json_payload['order_tax_amount'] = "10"
    post_error(merchant_auth, create_order_endpoint, json_payload, 400)

# Create Session without Categories
for i in range(0, AMOUNT_CREATE_SESSION_WITHOUT_CATEGORIES):
    trace("Create Session without Categories", i, AMOUNT_CREATE_SESSION_WITHOUT_CATEGORIES)
    json_payload = get_json_from_payload(create_session_payload)
    json_payload['purchase_country'] = "DE"
    json_payload['purchase_currency'] = "EUR"
    create_session_response = post(merchant_auth, create_session_endpoint, json.dumps(json_payload))
    validate(len(create_session_response.json()['payment_method_categories']) == 0)

# Get Payment Methods without methods
for i in range(0, AMOUNT_GET_PAYMENTS_METHODS_WITHOUT_METHODS):
    trace("Get Payment Methods without methods", i, AMOUNT_GET_PAYMENTS_METHODS_WITHOUT_METHODS)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    json_payload = get_json_from_payload(payment_method_payload)
    json_payload['payment_method_categories'] = ['fake']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), json.dumps(json_payload))
    validate(payment_methods_response.json()['internal']['status'] == 'no_methods')

# Authorize with Card Submission required
for i in range(0, AMOUNT_AUTHORIZE_WITH_CARD_SUBMISSION_REQUIRED):
    trace("Authorize with Card Submission required", i, AMOUNT_AUTHORIZE_WITH_CARD_SUBMISSION_REQUIRED)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), payment_method_payload)
    json_payload = get_json_from_payload(authorize_payload)
    json_payload['selected_payment_method']['type'] = 'card'
    authorize_response = post(client_auth, authorize_endpoint.replace("{{session_id}}", session_id), json.dumps(json_payload))
    validate(authorize_response.json()['internal']['status'] == 'card_submission_required')

# Authorize with Payment Method Mismatch
for i in range(0, AMOUNT_AUTHORIZE_WITH_PAYMENT_METHOD_MISMATCH):
    trace("Authorize with Payment Method Mismatch", i, AMOUNT_AUTHORIZE_WITH_PAYMENT_METHOD_MISMATCH)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), payment_method_payload)
    json_payload = get_json_from_payload(authorize_payload)
    json_payload['selected_payment_method']['type'] = 'pix'
    authorize_response = post(client_auth, authorize_endpoint.replace("{{session_id}}", session_id), json.dumps(json_payload))
    validate(authorize_response.json()['internal']['status'] == 'payment_method_mismatch')

# Create Order with Bad Value
for i in range(0, AMOUNT_CREATE_ORDER_WITH_BAD_REQUEST):
    trace("Create Order with Bad Value", i, AMOUNT_CREATE_ORDER_WITH_BAD_REQUEST)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), payment_method_payload)
    authorize_response = post(client_auth, authorize_endpoint.replace("{{session_id}}", session_id), authorize_payload)
    authorization_token = authorize_response.json()['external']['authorization_token']
    json_payload = get_json_from_payload(create_order_payload)
    json_payload['purchase_country'] = "fake"
    post_error(merchant_auth, create_order_endpoint.replace("{{authorization_token}}", authorization_token), json.dumps(json_payload), 400)


# Create customer tokens with Bad Value
for i in range(0, AMOUNT_CUSTOMER_TOKEN_INTERNAL_ERROR):
    trace("Create customer tokens with Bad Value", i, AMOUNT_CUSTOMER_TOKEN_INTERNAL_ERROR)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), payment_method_payload)
    authorize_response = post(client_auth, authorize_endpoint.replace("{{session_id}}", session_id), authorize_payload)
    authorization_token = authorize_response.json()['external']['authorization_token']
    json_payload = get_json_from_payload(create_customer_token_payload)
    json_payload['purchase_country'] = "fake"
    post_error(merchant_auth, create_customer_token_endpoint.replace("{{authorization_token}}", authorization_token), json.dumps(json_payload), 400)

# Regular purchases with invoice in OCAY
for i in range(0, AMOUNT_OF_PURCHASES):
    trace("Regular purchases with invoice in OCAY", i, AMOUNT_OF_PURCHASES)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), payment_method_payload)
    authorize_response = post(client_auth, authorize_endpoint.replace("{{session_id}}", session_id), authorize_payload)
    authorization_token = authorize_response.json()['external']['authorization_token']
    create_order_response = post(merchant_auth, create_order_endpoint.replace("{{authorization_token}}", authorization_token), create_order_payload)
    validate(create_order_response.json()['order_id'] is not None)

# Regular purchases with pix in OCAY
for i in range(0, AMOUNT_OF_PURCHASES):
    trace("Regular purchases with pix in OCAY", i, AMOUNT_OF_PURCHASES)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), payment_method_payload)
    json_payload = get_json_from_payload(authorize_payload)
    json_payload['selected_payment_method']['id'] = '4094'
    json_payload['selected_payment_method']['type'] = 'pix'
    authorize_response = post(client_auth, authorize_endpoint.replace("{{session_id}}", session_id), json.dumps(json_payload))
    authorization_token = authorize_response.json()['external']['authorization_token']
    create_order_response = post(merchant_auth, create_order_endpoint.replace("{{authorization_token}}", authorization_token), create_order_payload)
    validate(create_order_response.json()['order_id'] is not None)

# Create customer tokens
for i in range(0, AMOUNT_OF_TOKENS):
    trace("Create customer tokens", i, AMOUNT_OF_PURCHASES)
    create_session_response = post(merchant_auth, create_session_endpoint, create_session_payload)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth, payment_methods_endpoint.replace("{{session_id}}", session_id), payment_method_payload)
    authorize_response = post(client_auth, authorize_endpoint.replace("{{session_id}}", session_id), authorize_payload)
    authorization_token = authorize_response.json()['external']['authorization_token']
    create_customer_token_response = post(merchant_auth, create_customer_token_endpoint.replace("{{authorization_token}}", authorization_token), create_customer_token_payload)
    token_id = create_customer_token_response.json()['token_id']
    token_ids.append(token_id)
    validate(token_id is not None)

# Create recurring orders
for token_id in token_ids:
    trace("Create recurring orders", i, len(token_ids))
    create_customer_token_order_response = post(merchant_auth, create_customer_token_order_endpoint.replace("{{customer_token}}", token_id), create_customer_token_order_payload)
    validate(create_customer_token_order_response.json()['order_id'] is not None)

# Regular purchases with invoice in PACS
for i in range(0, AMOUNT_OF_PURCHASES):
    trace("Regular purchases with invoice in PACS", i, AMOUNT_OF_PURCHASES)
    create_session_response = post(merchant_auth_pacs, create_session_endpoint_pacs, create_session_payload_pacs)
    session_id = create_session_response.json()['session_id']
    payment_methods_response = post(client_auth_pacs, payment_methods_endpoint_pacs.replace("{{session_id}}", session_id), payment_method_payload_pacs)
    authorize_response = post(client_auth_pacs, authorize_endpoint_pacs.replace("{{session_id}}", session_id), authorize_payload_pacs)
    authorization_token = authorize_response.json()['external']['authorization_token']
    create_order_response = post(merchant_auth_pacs, create_order_endpoint_pacs.replace("{{authorization_token}}", authorization_token), create_order_payload_pacs)
    validate(create_order_response.json()['order_id'] is not None)
