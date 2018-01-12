from ..utils.class_or_instance import class_or_instance
from ..utils import commons, async_to_sync

__all__ = ['QueryClass']  # specifies what to import

@async_to_sync
class QueryClass(astroquery.BaseQuery):

    server = SERVER()

    def __init__(self, *args):
        """ set some parameters """
        # do login here
        pass

    @class_or_instance
    def query_region_async(self, *args, get_query_payload=False):

        request_payload = self._args_to_payload(*args)

        response = commons.send_request(self.server, request_payload, TIMEOUT)

        # primarily for debug purposes, but also useful if you want to send
        # someone a URL linking directly to the data
        if get_query_payload:
            return request_payload

        return response

    @class_or_instance
    def get_images_async(self, *args):
        image_urls = self.get_image_list(*args)
        return [get_readable_fileobj(U) for U in image_urls]
        # get_readable_fileobj returns need a "get_data()" method?

    @class_or_instance
    def get_image_list(self, *args):

        request_payload = self.args_to_payload(*args)

        result = requests.post(url, data=request_payload)

        return self.extract_image_urls(result)

    def _parse_result(self, result):
        # do something, probably with regexp's
        return astropy.table.Table(tabular_data)

    def _args_to_payload(self, *args):
        # convert arguments to a valid requests payload

        return dict
