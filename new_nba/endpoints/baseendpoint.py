import json
import pandas as pd

from new_nba.utils import check_status_code


class BaseEndpoint(object):

    def __init__(self, parent):
        """
        :param parent: API client.
        """
        self.client = parent

    def request(self, method, params={}, data={}, session=None):
        """
        :param url: NBA url to request.
        :param method: NBA API method to be used.
        :param params: Params to be used in request.
        :param data: data to be sent in request body.
        :param target: target to get from returned data, if none returns full response.
        :param session: Requests session to be used, reduces latency.
        """
        session = session or self.client.session
        request_url = '%s%s' % (self.client.url, method)
        response = session.request(
            'GET', request_url, params=params, data=json.dumps(data), headers=self.client.headers
        )
        check_status_code(response)
        return response

    @staticmethod
    def process_response(response_json, idx_val, result_name):
        """
        Parse data received from stats.nba.com endpoints

        :param json_data: data returned from requests to stats.nba.com endpoint.
        :type json_data: JSON
        :param idx_val: the index to retrieve from the returned data.
        :type idx_val: int
        :param result_name: json key to target for parsing results.
        :type result_name: str
        :returns: parsed nba data.
        :rtype: Dataframe

        """
        try:
            headers = response_json[result_name][idx_val]['headers']
            values = response_json[result_name][idx_val]['rowSet']
        except KeyError:
            headers = response_json[result_name]['headers']
            values = response_json[result_name]['rowSet']
        return pd.DataFrame(values, columns=headers)