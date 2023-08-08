from django.shortcuts import render

# Create your views here.

# views.py

import requests
from django.shortcuts import render
from django.http import JsonResponse
from activecampaign.client import Client
import json
from django.http import HttpResponse

# Replace 'YOUR_URL' and 'YOUR_API_KEY' with your actual ActiveCampaign URL and API key
url = 'https://ayareriya6.api-us1.com'
api_key = '2e6b13303c74f183bbd7fb1c9dea62a5d5fecb2dded6ea5815364c9871287b397cea1738'

client = Client(url, api_key)

def create_contact_automation_send_email(request):
    
    # Data for creating the contact
    
    contact_data = {
        "contact": {
            "email": "niketshah71@gmail.com",
            "firstName": "Recipient",
            "lastName": "Example",
            "phone": "7223224241"
        }
    }
    
    response = client.contacts.create_a_contact(contact_data)
    

    print("Response Data Type:", type(response))
    print("Response Content:", response)

    
    contact_id = response.get('contact', {}).get('id')

    
    # contact_id = response.json()['contact']['id']
    
    # email = contact_data['contact']['email']
    # response = client.contacts.list_all_contacts(email=email)
    # print(response)
    # contact_id = response.json()
    # # contact_list = json.dumps(response['contacts'])
    # print(dict(contact_list))
    # abc=dict(contact_list[0])
    # print(abc)
    # contact_id = abc['id']
    
    # return HttpResponse(contact_id)
    # return HttpResponse(response)

    

    
    contact_list_data = {
        "contactList":{
            'list': "1",
            'contact': contact_id,
            'status': "1"
        }
    }
    
    response = client.contacts.update_list_status_for_a_contact(contact_list_data)
    
    
    return JsonResponse(response)






