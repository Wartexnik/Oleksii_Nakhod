import requests
import json
from os.path import dirname, join


class Request():
    def __init__(self):
        self.url = None
        self.headers = None
        self.data = None

    def to_json(self, key):
        self.headers[key] = json.dumps(self.headers[key])
        return self

    def get(self):
        return requests.get(url=self.url, headers=self.headers, data=self.data)

    def post(self):
        return requests.post(url=self.url, headers=self.headers, data=self.data)
    

class RequestBuilder:
    def __init__(self):
        self.request = Request()
        self.request.headers = {}
        self.request.headers['Authorization'] = 'Bearer sl.BVOf294pphV0fkIVPCZjugiBPo9XoYFRoMQ1NAsG-nLeDGiDwuGkARM7ho-7JDR8CKpvZ6WeNN9xcAWxMa4ai-RafEL4w8pM6njGOE_KFNicv9fJGEDY7Wy8Rruh5hurRe6jM-w'

    def set_url(self, url):
        self.request.url = url
        return self

    def set_headers(self, headers):
        self.request.headers.update(headers)
        return self

    def set_data(self, data):
        self.request.data = data
        return self

    def build(self):
        return self.request


def upload_file():
    url = 'https://content.dropboxapi.com/2/files/upload'
    headers = {'Dropbox-API-Arg': {'autorename': False,
                                   'mode': 'overwrite',
                                   'mute': True,
                                   'path': '/python.png',
                                   'strict_conflict': False},
               'Content-Type': 'application/octet-stream'}
    with open(join(dirname(__file__), 'python.png'), 'rb') as file:
        data = file
        request = RequestBuilder() \
            .set_url(url) \
            .set_headers(headers) \
            .set_data(data) \
            .build()
        response = request.to_json('Dropbox-API-Arg').post()
        return response


def get_metadata():
    url = 'https://api.dropboxapi.com/2/files/get_metadata'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'include_deleted': False,
                       'include_has_explicit_shared_members': False,
                       'include_media_info': False,
                       'path': '/python.png'})
    request = RequestBuilder() \
        .set_url(url) \
        .set_headers(headers) \
        .set_data(data) \
        .build()
    response = request.post()
    return response


def delete_file():
    url = 'https://api.dropboxapi.com/2/files/delete_v2'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'path': '/python.png'})
    request = RequestBuilder() \
        .set_url(url) \
        .set_headers(headers) \
        .set_data(data) \
        .build()
    response = request.post()
    return response
