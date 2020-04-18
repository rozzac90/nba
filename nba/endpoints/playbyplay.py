import requests
import pandas as pd

from nba import enums
from nba.utils import clean_locals, check_status_code
from nba.endpoints.baseendpoint import BaseEndpoint


class PlayByPlay(BaseEndpoint):
    def play_by_play(
        self,
        game_id,
        start_period=enums.StartPeriod.AllQuarters,
        end_period=enums.EndPeriod.AllQuarters,
    ):
        """
        Play by play data for a given game, comments from home, away and neutral perspective.
    
        :param game_id: ID of the game to get data for.
        :type game_id: str
        :param start_period: starting period filter on the data.
        :type start_period: nba.enums.StartPeriod
        :param end_period: ending period filter on the data.
        :type end_period: nba.enums.EndPeriod
        :returns: play by play event descriptions and details of players involved
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = "playbyplayv2"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def play_by_play_detailed(self, game_id, locale="en", period="all"):
        """
        Get detailed play by play including location data from nba stats2.
        
        :param game_id: ID of the game to get data for.
        :param locale: language to return data in.
        :param period: 
        :return: 
        """
        response = requests.get(
            "http://uk.global.nba.com/stats2/game/playbyplay.json",
            {"gameId": game_id, "locale": locale, "period": period},
        )
        check_status_code(response)
        data = [
            events
            for period in response.json().get("payload", {}).get("playByPlays", {})
            for events in period.get("events", [])
        ]
        return pd.DataFrame(data[::-1])
