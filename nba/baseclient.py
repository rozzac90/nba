
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
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                               'AppleWebKit/537.36 (KHTML, like Gecko)'
                               'Chrome/60.0.3112.90 Safari/537.36'),
                'referer': 'http://stats.nba.com/scores/',
                'host': 'stats.nba.com',
                "cache-control": "max-age=0",
                'connection': 'keep-alive',
                "accept-encoding": "Accepflate, sdch",
                'accept-language': 'he-IL,he;q=0.8,en-US;q=0.6,en;q=0.4'}
