import requests
from utilities.temp_logger import log


class Requests:

    def __init__(self):
        self.request = requests

    def get(self, url, auth=None, headers=None, data=None):
        log("*******")
        log(f'API Method: GET | URL:- {url}')
        log(f'API Body Content:- {data}')
        log(f'API Header:- {headers}')
        response = self.request.get(url=url, headers=headers, auth=auth, data=data)
        log(f"Time taken:- {response.elapsed} | Status Code:- {response.status_code}")
        log(f'API Response:- {response.text}')
        log("*******")

        return response

    def post(self, url, auth=None, headers=None, data=None):
        log("*******")
        log(f'API Method: POST | URL:- {url}')
        log(f'API Body Content:- {data}')
        log(f'API Header:- {headers}')
        response = self.request.post(url=url, auth=auth, data=data, headers=headers)
        log(f"Time taken:- {response.elapsed} | Status Code:- {response.status_code}")
        log(f'API Response:- {response.text}')
        log("*******")

        return response

    def put(self, url, auth=None, headers=None, data=None):
        log("*******")
        log(f'API Method: PUT | URL:- {url}')
        log(f'API Body Content:- {data}')
        log(f'API Header:- {headers}')
        response = self.request.put(url=url, auth=auth, data=data, headers=headers)
        log(f"Time taken:- {response.elapsed} | Status Code:- {response.status_code}")
        log(f'API Response:- {response.text}')
        log("*******")

        return response

    def delete(self, url, auth=None, headers=None, data=None):
        log("*******")
        log(f'API Method: DELETE | URL:- {url}')
        log("API Body Content:- " + str(data))
        log("API Header:- " + str(headers))
        response = self.request.delete(url=url, headers=headers, auth=auth, data=data)
        log(f"Time taken:- {response.elapsed} | Status Code:- {response.status_code}")
        log(f'API Response:- {response.text}')
        log("*******")
        return response

    @staticmethod
    def parse_response(response):
        log(f"Parsing the following response - {response}")
        return response.json()
