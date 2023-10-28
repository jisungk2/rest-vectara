""" This is an example of calling Vectara API via python using http/rest as communication protocol.
"""

import argparse
import json
import logging
import requests


def _get_query_json(customer_id: int, corpus_id: int, query_value: str):
    """ Returns a query json. """
    query = {}
    query_obj = {}

    query_obj["query"] = query_value
    query_obj["num_results"] = 10

    corpus_key = {}
    corpus_key["customer_id"] = customer_id
    corpus_key["corpus_id"] = corpus_id
    query_obj["corpus_key"] = [ corpus_key ]

    summary = {}
    summary["responseLang"] = "en"
    summary["maxSummarizedResults"] = 5
    query_obj["summary"] = [ summary ]

    query["query"] = [ query_obj ]

    return json.dumps(query)


def query(customer_id: int, corpus_id: int, query_address: str, api_key: str, query: str):
    """This method queries the data.
    Args:
        customer_id: Unique customer ID in vectara platform.
        corpus_id: ID of the corpus to which data needs to be indexed.
        query_address: Address of the querying server. e.g., api.vectara.io
        api_key: A valid API key with query access on the corpus.

    Returns:
        (response, True) in case of success and returns (error, False) in case of failure.

    """
    post_headers = {
        "customer-id": f"{customer_id}",
        "x-api-key": api_key
    }

    response = requests.post(
        f"https://{query_address}/v1/query",
        data=_get_query_json(customer_id, corpus_id, query),
        verify=True,
        headers=post_headers)

    if response.status_code != 200:
        logging.error("Query failed with code %d, reason %s, text %s",
                       response.status_code,
                       response.reason,
                       response.text)
        return response, False
        
    return response, True
