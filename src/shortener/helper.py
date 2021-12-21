from django.http import Http404, JsonResponse


class CustomJsonResponse(JsonResponse):
    """CustomJsonResponse

    An HTTP response class that inherits JsonResponse
    :param res: A named_tuple imported from ci_admin.results.code_n_msg
                and passed to pay_load.
    :param data: A dictionary of kwargs passed to pay_load.
    :param pagination: The response of ci_admin.pagination.CustomPagination

    """
    def __init__(self, return_code = '0000', return_message = '', result_data = {}, pagination = {}, **kwargs):

        self.data = self.set_payload(return_code, return_message, result_data, pagination)

        super(CustomJsonResponse, self).__init__(
            data=self.data,
            **kwargs
        )


    def set_payload(self, return_code = '0000', return_message = '', result_data = {}, pagination = {}):
        payload = {
            'return_code': return_code,
            'return_message': return_message,
            'result_data': result_data
        }
        
        if pagination:
            payload['pagination'] = pagination
        return payload
