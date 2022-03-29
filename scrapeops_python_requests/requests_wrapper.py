import requests
from scrapeops_python_requests.logger import Logger


class SOSession(requests.Session): 

    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    # @Logger.scrapeops_logger 
    # def request(self, method, url, **kwargs):
    #     kwargs.setdefault('allow_redirects', True)
    #     return self.request(method, url, **kwargs)

    @Logger.scrapeops_logger 
    def get(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    @Logger.scrapeops_logger 
    def post(self, url, data=None, json=None, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)

    @Logger.scrapeops_logger 
    def put(self, url, data=None, **kwargs):
        return self.request('PUT', url, data=data, **kwargs)

    @Logger.scrapeops_logger 
    def patch(self, url, data=None, **kwargs):
        return self.request('PATCH', url, data=data, **kwargs)

    @Logger.scrapeops_logger 
    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)

    def options(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.request('OPTIONS', url, **kwargs)

    def head(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', False)
        return self.request('HEAD', url, **kwargs)



class RequestsWrapper: 

    def __init__(self, passedInSOLogger=None):
        self.logger = passedInSOLogger


    @Logger.scrapeops_logger 
    def request(self, *args, **kwargs):
        return requests.request(*args, **kwargs)
    
    @Logger.scrapeops_logger 
    def get(self, *args, **kwargs):
        return requests.get(*args, **kwargs)
    
    @Logger.scrapeops_logger 
    def post(self, *args, **kwargs):
        return requests.post(*args, **kwargs)
    
    @Logger.scrapeops_logger 
    def put(self, *args, **kwargs):
        return requests.put(*args, **kwargs)
    
    @Logger.scrapeops_logger 
    def delete(self, *args, **kwargs):
        return requests.delete(*args, **kwargs)
    
    def head(self, *args, **kwargs):
        return requests.head(*args, **kwargs)
    
    def options(self, *args, **kwargs):
        return requests.options(*args, **kwargs)
  
    def Session(self):
        return SOSession(self.logger)