import os
import json
from base.request import Requests
from utilities.temp_logger import log
from utilities.generic_method import GenericMethod


class Conversation(Requests):
    def __init__(self):
        # Object initialisation
        super(Conversation, self).__init__()
        self.generic_method = GenericMethod()

        # Class level variables
        self.env = os.getenv("environment")
        self.header = {'Authorization': f'Bearer {os.getenv("jwt_token")}',
                       'Content-Type': 'application/json'}
        self.base_url = {
            "dev": "https://api.nexmo.com/",
            "production": "https://nexmo.com/"
        }

    def create_conversation(self, input_data, new_api_version=False, parse=False):
        # Fetching Base payload structure
        payload = self.generic_method.get_api_body_json('../json_schema/create_conversation')

        # Updating the base structure with provided input
        if input_data:
            payload = self.generic_method.custom_payload_updater(payload=payload, input_param=input_data)

        # Verifying if the api payload update is successful or not
        if not payload:
            log("API payload construction failed")
            return False

        # API URL construction based on the environment and it's version
        url = f'{self.base_url[self.env]}v0.1/conversations'
        if new_api_version:
            url = f'{self.base_url[self.env]}v0.2/conversations'

        # Hitting the actual API
        response = super(Conversation, self).post(url=url, headers=self.header, data=json.dumps(payload))

        # Returning the results
        if parse and response.status_code == 200:
            response = super(Conversation, self).parse_response(response)
            log(f'Returning the conversation ID after successful creation')
            return response['id']
        elif parse:
            log(f'Conversation creation failed due to - {response.text}')
            return False
        return response

    def list_conversation(self, new_api_version=True, parse=False):

        # API URL construction based on the environment and it's version
        url = f'{self.base_url[self.env]}v0.1/conversations'
        if new_api_version:
            url = f'{self.base_url[self.env]}v0.2/conversations'

        # Hitting the actual API
        response = super(Conversation, self).get(url=url, headers=self.header)

        # Returning the results
        if parse and response.status_code == 200:
            response = super(Conversation, self).parse_response(response)
            log(f'Returning the conversation array')
            return response['_embedded']['data']['conversations']
        elif parse:
            log(f'List conversation action failed due to - {response.text}')
            return False
        return response

    def update_conversation(self, input_data, conversation_id=None, new_api_version=False, parse=False):
        # Fetching Base payload structure
        payload = self.generic_method.get_api_body_json('../json_schema/update_conversation')

        # Updating the base structure with provided input
        if input_data:
            payload = self.generic_method.custom_payload_updater(payload=payload, input_param=input_data)

        # Verifying if the api payload update is successful or not
        if not payload:
            log("API payload construction failed")
            return False

        # API URL construction based on the environment and it's version
        url = f'{self.base_url[self.env]}v0.1/conversations/{conversation_id}'
        if new_api_version:
            url = f'{self.base_url[self.env]}v0.2/conversations/{conversation_id}'

        # Hitting the actual API
        response = super(Conversation, self).put(url=url, headers=self.header, data=json.dumps(payload))

        # Returning the results
        if parse and response.status_code == 200:
            response = super(Conversation, self).parse_response(response)
            log(f'Returning the conversation ID after successful update')
            return response['id']
        elif parse:
            log(f'Conversation update failed due to - {response.text}')
            return False
        return response

    def retrieve_conversation(self, conversation_id=None, new_api_version=False, parse=False):
        # API URL construction based on the environment and it's version
        url = f'{self.base_url[self.env]}v0.1/conversations/{conversation_id}'
        if new_api_version:
            url = f'{self.base_url[self.env]}v0.2/conversations/{conversation_id}'

        # Hitting the actual API
        response = super(Conversation, self).get(url=url, headers=self.header)

        # Returning the results
        if parse and response.status_code == 200:
            response = super(Conversation, self).parse_response(response)
            log(f'Returning the conversation id after verification')
            return response['uuid']
        elif parse:
            log(f'Conversation retrieval failed due to - {response.text}')
            return False
        return response

    def delete_conversation(self, conversation_id=None, new_api_version=False, parse=False):
        # API URL construction based on the environment and it's version
        url = f'{self.base_url[self.env]}v0.1/conversations/{conversation_id}'
        if new_api_version:
            url = f'{self.base_url[self.env]}v0.2/conversations/{conversation_id}'

        # Hitting the actual API
        response = super(Conversation, self).delete(url=url, headers=self.header)

        # Returning the results
        if parse and response.status_code == 200:
            log(f'Returning True after successful Deletion')
            return True
        elif parse:
            log(f'Conversation delete action failed due to - {response.text}')
            return False
        return response

    def record_conversation(self, input_data=None, conversation_id=None, new_api_version=False, parse=False):
        # Fetching Base payload structure
        payload = self.generic_method.get_api_body_json('../json_schema/record_conversation')

        # Updating the base structure with provided input
        if input_data:
            payload = self.generic_method.custom_payload_updater(payload=payload, input_param=input_data)

        # Verifying if the api payload update is successful or not
        if not payload:
            log("API payload construction failed")
            return False

        # API URL construction based on the environment and it's version
        url = f'{self.base_url[self.env]}v0.1/conversations/{conversation_id}'
        if new_api_version:
            url = f'{self.base_url[self.env]}v0.2/conversations/{conversation_id}'

        # Hitting the actual API
        response = super(Conversation, self).put(url=url, headers=self.header, data=json.dumps(payload))

        # Returning the results
        if parse and response.status_code == 200:
            log(f'Returning the conversation ID after successful recording')
            return True
        elif parse:
            log(f'Conversation update failed due to - {response.text}')
            return False
        return response
