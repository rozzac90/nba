
from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Homepage(BaseEndpoint):

    def homepageleaders(self, idx_data, LeagueID=enums.LeagueID.Default, StatCategory=enums.StatCategory.Default, Season=enums.Season.Default,
                        SeasonType=enums.SeasonType.Default, PlayerOrTeam=enums.PlayerOrTeam.Default,
                        GameScope=enums.GameScope.Default, PlayerScope=enums.PlayerScope.Default):
        """
        Get top 5 players/teams by a particular stat.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param LeagueID: league to filter for.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param StatCategory: Stat to sort leaders table by.
        :type StatCategory: nba.nba.bin.enums.StatCategory
        :param Season: Season for which to get stat leaders.
        :type Season: nba.nba.bin.enums.Season
        :param SeasonType: Regular Season or Playoffs.
        :type SeasonType: nba.nba.bin.enums.SeasonType
        :param PlayerOrTeam: whether to get individual players or by team.
        :type PlayerOrTeam: nba.nba.bin.enums.PlayerOrTeam
        :param GameScope: what games to include in the data.
        :type GameScope: nba.nba.bin.enums.GameScope
        :param PlayerScope: filter by rookies only or all players
        :type PlayerScope: nba.nba.bin.enums.PlayerScope
        :returns: data for specified filters, as defined below by idx_data.
        :rtype: Dataframe
    
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
        r = self.request(params, endpoint)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def homepagev2(self, idx_data, LeagueID=enums.LeagueID.Default, StatType=enums.StatType.Default, Season=enums.Season.Default,
                   SeasonType=enums.SeasonType.Default, PlayerOrTeam=enums.PlayerOrTeam.Default,
                   GameScope=enums.GameScope.Default, PlayerScope=enums.PlayerScope.Default):
        """
       Get top 5 players/teams by a particular stat type.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param LeagueID: league to filter for.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param StatType: Stat to sort leaders table by.
        :type StatType: nba.nba.bin.enums.StatType
        :param Season: Season for which to get stat leaders.
        :type Season: nba.nba.bin.enums.Season
        :param SeasonType: Regular Season or Playoffs.
        :type SeasonType: nba.nba.bin.enums.SeasonType
        :param PlayerOrTeam: whether to get individual players or by team.
        :type PlayerOrTeam: nba.nba.bin.enums.PlayerOrTeam
        :param GameScope: what games to include in the data.
        :type GameScope: nba.nba.bin.enums.GameScope
        :param PlayerScope: filter by rookies only or all players
        :type PlayerScope: nba.nba.bin.enums.PlayerScope
        :returns: top 5 players for given stat type, as defined below by idx_data.
        :rtype: Dataframe
    
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
        r = self.request(params, endpoint)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def leaderstiles(self, idx_data, LeagueID=enums.LeagueID.Default, Stat=enums.Stat.Default, Season=enums.Season.Default,
                     SeasonType=enums.SeasonType.Default, PlayerOrTeam=enums.PlayerOrTeam.Default,
                     GameScope=enums.GameScope.Default, PlayerScope=enums.PlayerScope.Default):
        """
        Get top 5 players/teams by a particular stat.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param LeagueID: league to filter for.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param Stat: Stat to sort leaders table by.
        :type Stat: nba.nba.bin.enums.Stat
        :param Season: Season for which to get stat leaders.
        :type Season: nba.nba.bin.enums.Season
        :param SeasonType: Regular Season or Playoffs.
        :type SeasonType: nba.nba.bin.enums.SeasonType
        :param PlayerOrTeam: whether to get individual players or by team.
        :type PlayerOrTeam: nba.nba.bin.enums.PlayerOrTeam
        :param GameScope: what games to include in the data.
        :type GameScope: nba.nba.bin.enums.GameScope
        :param PlayerScope: filter by rookies only or all players
        :type PlayerScope: nba.nba.bin.enums.PlayerScope
        :returns: data for specified filters, as defined below by idx_data.
        :rtype: Dataframe
    
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
        r = self.request(params, endpoint)
        df = self.process_response(r, idx_data, 'resultSet')
        return df
