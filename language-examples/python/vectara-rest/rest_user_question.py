import json
import logging
import requests
from rest_api_key_index import index_document
from rest_api_key_queries import query

#Should write the entire transcript to output.txt at the beginning

query_address = "api.vectara.io"
customer_id = 1354170844
corpus_id = 5
api_key = "zwt_ULcB3HdLImfP3GJ7jDwL7iMTbx0yaJoJ8LLzxg"

index_document(customer_id, corpus_id, query_address, api_key)

response, success = query(customer_id, corpus_id, query_address, api_key, USER_QUERY)

print(response.text)



