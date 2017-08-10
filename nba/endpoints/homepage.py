
from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Homepage(BaseEndpoint):

    def leaders(self, idx_data, league_id=enums.LeagueID.Default, stat_category=enums.StatCategory.Default,
                season=enums.Season.Default, season_type=enums.SeasonType.Default,
                player_or_team=enums.PlayerOrTeam.Default, game_scope=enums.GameScope.Default,
                player_scope=enums.PlayerScope.Default):
        """
        Get top 5 players/teams by a particular stat.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: league to filter for.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param stat_category: Stat to sort leaders table by.
        :type stat_category: nba.nba.bin.enums.StatCategory
        :param season: Season for which to get stat leaders.
        :type season: nba.nba.bin.enums.Season
        :param season_type: Regular Season or Playoffs.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param player_or_team: whether to get individual players or by team.
        :type player_or_team: nba.nba.bin.enums.PlayerOrTeam
        :param game_scope: what games to include in the data.
        :type game_scope: nba.nba.bin.enums.GameScope
        :param player_scope: filter by rookies only or all players
        :type player_scope: nba.nba.bin.enums.PlayerScope
        :returns: data for specified filters, as defined below by idx_data.
        :rtype: DataFrame
    
        ========   ================   ==================================================
        idx_data        Name                         Description
        ========   ================   ==================================================
            0       HomePageLeaders   Top 5 players/teams by stat specified.
            1       LeagueAverage     League average of the stat specified.
            2       LeagueMax         League max of each stat column.
        ========   ================   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'homepageleaders'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def other_leaders(self, idx_data, league_id=enums.LeagueID.Default, stat_type=enums.StatType.Default,
                      season=enums.Season.Default, season_type=enums.SeasonType.Default,
                      player_or_team=enums.PlayerOrTeam.Default, game_scope=enums.GameScope.Default,
                      player_scope=enums.PlayerScope.Default):
        """
       Get top 5 players/teams by a particular stat type.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: league to filter for.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param stat_type: Stat to sort leaders table by.
        :type stat_type: nba.nba.bin.enums.StatType
        :param season: Season for which to get stat leaders.
        :type season: nba.nba.bin.enums.Season
        :param season_type: Regular Season or Playoffs.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param player_or_team: whether to get individual players or by team.
        :type player_or_team: nba.nba.bin.enums.PlayerOrTeam
        :param game_scope: what games to include in the data.
        :type game_scope: nba.nba.bin.enums.GameScope
        :param player_scope: filter by rookies only or all players
        :type player_scope: nba.nba.bin.enums.PlayerScope
        :returns: top 5 players for given stat type, as defined below by idx_data.
        :rtype: DataFrame
    
        ========   ===============   ==================================================================
        idx_data        Name                                   Description
        ========   ===============   ==================================================================
            0       HomePageStat1     Traditional=PTS, Advanced=OFF_RATING, Tracking=DIST_MILES
            1       HomePageStat2     Traditional=REB, Advanced=DEF_RATING, Tracking=AST_POINTS_CREATED
            2       HomePageStat3     Traditional=AST, Advanced=NET_RATING, Tracking=DRIVES
            3       HomePageStat4     Traditional=STL, Advanced=PIE, Tracking=NUM_TOUCHES
            4       HomePageStat5     Traditional=FG_PCT, Advanced=REB_PCT, Tracking=POST_TOUCHES
            5       HomePageStat6     Traditional=FT_PCT, Advanced=AST_PCT, Tracking=REB_CONTEST
            6       HomePageStat7     Traditional=FG3_PCT, Advanced=TS_PCT, Tracking=CATCH_SHOOT_PTS
            7       HomePageStat8     Traditional=BLK, Advanced=EFG_PCT, Tracking=PULL_UP_PTS
        ========   ===============   ==================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'homepagev2'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def leaders_tiles(self, idx_data, league_id=enums.LeagueID.Default, stat=enums.Stat.Default,
                      season=enums.Season.Default, season_type=enums.SeasonType.Default,
                      player_or_team=enums.PlayerOrTeam.Default, game_scope=enums.GameScope.Default,
                      player_scope=enums.PlayerScope.Default):
        """
        Get top 5 players/teams by a particular stat.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: league to filter for.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param stat: Stat to sort leaders table by.
        :type stat: nba.nba.bin.enums.Stat
        :param season: Season for which to get stat leaders.
        :type season: nba.nba.bin.enums.Season
        :param season_type: Regular Season or Playoffs.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param player_or_team: whether to get individual players or by team.
        :type player_or_team: nba.nba.bin.enums.PlayerOrTeam
        :param game_scope: what games to include in the data.
        :type game_scope: nba.nba.bin.enums.GameScope
        :param player_scope: filter by rookies only or all players
        :type player_scope: nba.nba.bin.enums.PlayerScope
        :returns: data for specified filters, as defined below by idx_data.
        :rtype: DataFrame
    
        ========   ==================   ====================================================
        idx_data        Name                         Description
        ========   ==================   ====================================================
            0       LeadersTiles         Top 5 players/teams by stat specified with id info.
            1       AllTimeSeasonHigh    Details of the all time high of the stat specified.
            2       LastSeasonHigh       Details of prior seasons high of stat specified.
            3       LastSeasonHigh       Details of prior seasons low of stat specified.
        ========   ==================   ====================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'leaderstiles'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSet')
        return df
