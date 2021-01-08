from __future__ import absolute_import
import requests
from flowycart import api_url


class Resource(object):
    data = None

    def get(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    @staticmethod
    def request(api_key, query, variables, operation):

        data = {
            'query': query,
            'variables': variables,
            'operation': operation
        }

        return requests.post(
            url=api_url,
            json=data,
            headers={
                'content-type': 'application/json',
                'authorization': api_key
            }
        )
