## Internal
from scrapeops_python_requests.requests_wrapper import RequestsWrapper 
from scrapeops_python_requests.utils import ResponseDataNormaliser 

from scrapeops_python_logger.scrapeops_logger import ScrapeOpsLogger
from scrapeops_python_logger.normalizer.request_response import SOPSResponse

class ScrapeOpsRequests:

    def __init__(self, **kwargs):
        self.logger = ScrapeOpsLogger(**kwargs)


    def RequestsWrapper(self):
        return RequestsWrapper(self.logger)

    def item_scraped(self, item=None, response=None):
        response_obj = SOPSResponse(
                url = response.url,
                method=ResponseDataNormaliser.method(response),  
                status_code=ResponseDataNormaliser.status_code(response),
                bytes=ResponseDataNormaliser.response_size(response),
            )
        self.logger.item_scraped(item=item, response=response_obj)




    







