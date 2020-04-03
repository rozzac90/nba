from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Common(BaseEndpoint):

    # def team_years(self, league_id=enums.LeagueID.Default):
    #     """
    #     Get information on when teams were playing in the league.

    #     :param league_id: define league to look at, nba.
    #     :type league_id: nba.enums.LeagueID
    #     :returns: breakdown of min and max year playing in nba by team.

    #     """
    #     params = clean_locals(locals())
    #     endpoint = 'commonTeamYears'
    #     r = self.request(endpoint, params)
    #     df = self.process_response(r, 0, 'resultSets')
    #     return df

    def all_players(
        self,
        league_id=enums.LeagueID.Default,
        season=enums.Season.Default,
        is_only_current_season=1,
    ):
        """
        Get individual player details.
        
        :param league_id: league to retrieve data for.
        :type league_id: str
        :param season: Season for which we require data.
        :type season: str('%Y-%y')
        :param is_only_current_season: define whether to only get players on a roster in current season.
        :type is_only_current_season: bool(1|0)
        :returns: player information.
        :rtype: Dataframe
        
        """
        params = clean_locals(locals())
        endpoint = "commonallplayers"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def player_info(self, player_id):
        """
        Get detailed information for a player.
        
        :param player_id: id of player to get information for.
        :type player_id: int
        :returns: detailed player information.
        :rtype: Dataframe
        
        """
        params = clean_locals(locals())
        endpoint = "commonplayerinfo"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def play_off_series(
        self, league_id=enums.LeagueID.Default, season=enums.Season.Default
    ):
        """
        Get playoff series match ups for a given season.
    
        :param league_id: league to retrieve data for.
        :type league_id: str
        :param season: Season for which we require data.
        :type season: str('%Y-%y')
        :returns: match up by home/away team id and series id.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = "commonplayoffseries"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def team_roster(self, team_id, idx_data, season=enums.Season.Default):
        """
        Get team roster breakdown.
    
        :param team_id: id of the team whose roster to retrieve
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param season: season for which we require data.
        :type season: str('%Y-%y')
        :returns: roster breakdown of player details.
        :rtype: Dataframe
        
        ========   ==================   ====================================================================
        idx_data         Name                             Description
        ========   ==================   ====================================================================
            0       Players              Players roster.
            1       Coaches              Coaching staff roster.
        ========   ==================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = "commonteamroster"
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, "resultSets")
        return df

    # def team_info(self, team_id, league_id=enums.LeagueID.Default, season=enums.Season.Default,
    #               season_type=enums.SeasonType.Default):
    #     """
    #     Get high level team data.

    #     :param team_id: id of team for which to get data.
    #     :type team_id: int
    #     :param league_id: id of league in which team plays.
    #     :type league_id: nba.enums.LeagueID
    #     :param season: season for which we require data.
    #     :type season: str('%Y-%y')
    #     :param season_type: playoff or regular season specification.
    #     :type season_type: nba.enums.SeasonType
    #     :returns: team information and season record.
    #     :rtype: Dataframe

    #     """
    #     params = clean_locals(locals())
    #     endpoint = 'teaminfocommon'
    #     r = self.request(endpoint, params)
    #     df = self.process_response(r, 0, 'resultSets')
    #     return df
