import logging
import os
import azure.functions as func
import requests
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not req.params.get('data'):
        return func.HttpResponse(f"Data is not defined.")
    else:       
    
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ os.getenv("api_key"))}

        test_sample = json.dumps({'data': [[1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1]]})
        test_sample = bytes(test_sample,encoding = 'utf8')

        response = requests.post(os.getenv("web_service_url"), test_sample, headers=headers)

        print('Predictions')
        print(response)
        print(response.status_code) 
        print(response.text)
        print(json.loads(response.text))

    if response.status_code==200:
        return func.HttpResponse(f"Hello, The prediction is: " + response.text)
    else:
        return func.HttpResponse(f"Unable to get prediction")






