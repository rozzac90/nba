
import requests


class BaseClient(object):
    def __init__(self):
        self.url = 'http://stats.nba.com/stats/'
        self.session = requests.Session()
        self.current_season = '2016-17'

    @property
    def headers(self):
        """Set headers to be used in API requests."""
        return {'Content-Type': 'application/json',
                'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/45.0.2454.101 Safari/537.36'),
                'referer': 'http://stats.nba.com/scores/'}
