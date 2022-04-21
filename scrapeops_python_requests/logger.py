
import functools

## Internal
from scrapeops_python_requests.utils import RequestDataNormaliser, ResponseDataNormaliser 
from scrapeops_python_logger.normalizer.request_response import SOPSRequest, SOPSResponse

class Logger:


    @staticmethod
    def scrapeops_logger(request_func):

        @functools.wraps(request_func)
        def logger_wrapper(*args, **kwargs):

            ## Get ScrapeOps Logger 
            logger = Logger.get_logger(args)

            ## Method type - GET/POST/PUT
            methodName = request_func.__name__.upper()
            if(methodName == 'REQUEST'):                
                methodName = args[1]

 

            ## Log Request
            request_obj = SOPSRequest(
                url=RequestDataNormaliser.extract_url(args, kwargs),
                proxy_port=RequestDataNormaliser.extract_proxy_port(kwargs), 
                headers=RequestDataNormaliser.extract_headers(kwargs),
                method=methodName,
                )

            Logger.log_request(logger, request_obj)


            ## Make Request
            request_obj.get_start_time() 

            response = request_func(*args, **kwargs)
            response_obj = SOPSResponse(
                url = response.url,
                request = request_obj,
                method=methodName, 
                proxy_port=RequestDataNormaliser.extract_proxy_port(kwargs),
                status_code=ResponseDataNormaliser.status_code(response),
                bytes=ResponseDataNormaliser.response_size(response),
                body=ResponseDataNormaliser.response_body(response),
                json_res=ResponseDataNormaliser.response_json(response),
            )

            Logger.log_response(logger, response_obj)

            request_obj.get_finish_time() 

            return response
        return logger_wrapper



    @staticmethod
    def get_logger(args):
        if hasattr(args[0], 'logger'):
                return args[0].logger
        return None

    @staticmethod
    def log_request(logger, request_obj):
        if logger is not None:
            logger.log_request(request_obj)

    @staticmethod
    def log_response(logger, response_obj):
        if logger is not None:
            logger.log_response(response_obj)

