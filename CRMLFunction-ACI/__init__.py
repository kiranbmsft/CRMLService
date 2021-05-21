import logging

import azure.functions as func
import requests
import json
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not req.params.get('data'):
        return func.HttpResponse(f"Data is not defined.")
    else:       
        headers = {'Content-Type':'application/json'}

        response = requests.post(os.getenv("web_service_url"),json.dumps({'data': req.params.get('data').split(',')}), headers=headers)
        
        print('Predictions')
        print(response)
        print(response.status_code) 

        print(response.text)
        print(json.loads(response.text))

    if response.status_code==200:
        return func.HttpResponse(f"Hello, The prediction is: " + response.text)
    else:
        return func.HttpResponse(f"Unable to get prediction")

    
