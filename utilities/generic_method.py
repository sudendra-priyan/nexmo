import os
import json
import dpath.util
from random import randint
from utilities.temp_logger import log


class GenericMethod:
    @staticmethod
    def get_api_body_json(file_path):
        """
        Fetch the Json file
        Args:
            file_path: File path to fetch the json
        """

        my_path = os.path.abspath(os.path.dirname(__file__))
        user_detail_file_path = os.path.join(my_path, file_path)
        with open(user_detail_file_path, "r") as read_file:
            return json.load(read_file)

    @staticmethod
    def custom_payload_updater(payload, input_param):
        """
        Alters the default payload based on the given input

        Args:
            payload: Original Payload
            input_param: Key value pair which needs to be updated

        Returns:
            Updated payload for successful attempt, False in case of failure

        """

        for input_key in input_param:
            if len(dpath.util.search(payload, input_key)) != 0:
                dpath.util.set(payload, input_key, input_param[input_key])
            else:
                log('Could not update input key ===> ' + input_key)
                return False
        log("Generated Payload is: " + str(payload))
        return payload

    @staticmethod
    def get_random_name(name):
        """
        Returns Random Name
        @author: sudendra.priyan
        """
        return f'{name}_{randint(100000, 999999)}'
