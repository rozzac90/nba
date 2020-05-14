import requests
from requests.adapters import HTTPAdapter


class BaseClient(object):
    def __init__(self):
        self.url = "http://stats.nba.com/stats/"
        self.session = requests.Session()
        self.session.mount("http://stats.nba.com", HTTPAdapter(max_retries=1))
        self.current_season = "2019-20"

    @property
    def headers(self):
        """Set headers to be used in API requests."""
        return {
            "Content-Type": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/81.0.4044.129 Safari/537.36"
            ),
            "Host": "stats.nba.com",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "x-nba-stats-origin": "stats",
            "x-nba-stats-token": "true",
        }
