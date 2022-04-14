from urllib.parse import urlencode


class RequestDataNormaliser:

    def __init__(self):
        pass
    
    @staticmethod
    def extract_url(args, kwargs):
        if len(args) < 1:
            return None
        if kwargs.get('params') is not None:
            return args[1] + '?' +  urlencode(kwargs.get('params')) 
        if(args[1] == 'POST' or args[1] == 'GET' or args[1] == 'REQUEST'):
            return args[2]
        return args[1]

    @staticmethod
    def extract_proxy_port(kwargs):
        proxy_dict = kwargs.get('proxies')
        if isinstance(proxy_dict, dict):
            for k, v in proxy_dict.items():
                return v
        return None
    
    @staticmethod
    def extract_headers(kwargs):
        return kwargs.get('headers')





class ResponseDataNormaliser:

    def __init__(self):
        pass
    
    @staticmethod
    def status_code(response):
        return response.status_code

    @staticmethod
    def response_size(response):
        try:
            return len(response.content)
        except:
            return 0
    
    @staticmethod
    def method(response):
        if hasattr(response, 'request'):
            if hasattr(response.request, 'method'):
                return response.request.method
        return 'Unknown'

    @staticmethod
    def response_body(response):
        try:
            return response.text
        except:
            return None

    @staticmethod
    def response_json(response):
        try:
            json_body = response.json()
            return json_body
        except:
            return None



