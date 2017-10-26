
import datetime
import pandas as pd

from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Misc(BaseEndpoint):
    
    def play_off_picture(self, idx_data, league_id=enums.LeagueID.Default, season_id=enums.Season.Default):
        """
        Get information on how current playoff matchups and conference standings are.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: league to filter for.
        :type league_id: nba.enums.LeagueID
        :param season_id: Season for which to get stat leaders.
        :type season_id: nba.enums.Season
        :returns: A view of playoff or standings, as show in idx_data table breakdown below.
        :rtype: DataFrame
    
        ========   =======================   ==================================================================
        idx_data           Name                                   Description
        ========   =======================   ==================================================================
            0       EastConfPlayoffPicture    Breakdown of how East Conference playoff matchups currently look.
            1       WestConfPlayoffPicture    Breakdown of how West Conference playoff matchups currently look.
            2       EastConfStandings         Current standing for East Conference.
            3       WestConfStandings         Current standing for West Conference.
            4       EastConfRemainingGames    Breakdown of games remaining in East Conference.
            5       WestConfRemainingGames    Breakdown of games remaining in East Conference.
        ========   =======================   ==================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playoffpicture'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def video_status(self, game_date=datetime.datetime.today().strftime('%Y-%m-%d'), league_id=enums.LeagueID.Default):
        """
        Breakdown of which games are available on video on a given date.
    
        :param game_date: date to check.
        :type game_date: str('%Y-%m-%d')
        :param league_id: league to filter for.
        :type league_id: nba.enums.LeagueID
        :returns: games on the given date and whether they are available on video.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'videoStatus'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def rotowire_player_news(self):
        """
        Get player news and updates from rotowire.
        
        :return: News updates.
        """
        url = r'http://stats-prod.nba.com/wp-json/statscms/v1/rotowire/player'
        r = self.request(None, request_url=url)
        df = pd.DataFrame(r.get('ListItems', []))
        return df
