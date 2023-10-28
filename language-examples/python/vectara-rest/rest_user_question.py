import json
import logging
import requests
from rest_create_corpus import create_corpus
from rest_upload_file import upload_file
from rest_query import query
from rest_util import _get_jwt_token

#Should write the entire transcript to output.txt at the beginning

auth_url = "https://vectara-prod-1354170844.auth.us-west-2.amazoncognito.com"
query_address = "https://api.vectara.io"
app_client_id = "7r2mq0c457jsn4t8tq6agpd5lb"
app_client_secret = "10205n0csja2j72k6oots5tq8cm5a21inea6hh04olrfe3ef3659"
customer_id = 1354170844

jwt_token = _get_jwt_token(auth_url, app_client_id, app_client_secret)

response, success = create_corpus(customer_id, auth_url, jwt_token, "cs-summary")

corpus_id = response.corpus_id

upload_file(customer_id, corpus_id, auth_url, jwt_token)

response, success = query(customer_id, corpus_id, auth_url, jwt_token, "What are garbage values?")

print(response.text)



