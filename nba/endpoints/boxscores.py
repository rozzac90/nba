
from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Boxscores(BaseEndpoint):

    def boxscore_advanced(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                          StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get advanced box score stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: data for specified filters, as defined below by idx_data.
        :rtype: Dataframe
    
        ========   ============   ==================================================
        idx_data       Name                         Description
        ========   ============   ==================================================
            0       PlayerStats   Advanced box scores on an individual player basis.
            1       TeamStats     Advanced box scores on a team basis.
        ========   ============   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscoreadvancedv2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df

    def boxscorefourfactors(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                            StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get four factors stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: four factors stats on team/player basis, as defined below by idx_data table.
        :rtype: Dataframe
    
        ========   ======================   ==================================================
        idx_data          Name                                  Description
        ========   ======================   ==================================================
            0       sqlPlayersFourFactors   Four factors stats on an individual player basis.
            1       sqlTeamsFourFactors     Four factors stats on a team basis.
        ========   ======================   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscorefourfactorsv2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df

    def boxscoremisc(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                     StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get miscellaneous stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: miscellaneous stats on team/player basis, as defined below by idx_data table.
        :rtype: Dataframe
    
        ========   ===============   ==================================================
        idx_data          Name                        Description
        ========   ===============   ==================================================
            0       sqlPlayersMisc   Miscellaneous stats on an individual player basis.
            1       sqlTeamsMisc     Miscellaneous stats on a team basis.
        ========   ===============   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscoremiscv2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df

    def boxscorescoring(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                        StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get scoring stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: scoring stats on team/player basis, as defined below by idx_data table.
        :rtype: Dataframe
    
        ========   ==================   ==================================================
        idx_data          Name                           Description
        ========   ==================   ==================================================
            0       sqlPlayersScoring   Scoring stats on an individual player basis.
            1       sqlTeamsScoring     Scoring stats on a team basis.
        ========   ==================   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscorescoringv2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df

    def boxscoretraditional(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                            StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get traditional box score stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: traditional box scores on team/player/startvsbench basis, as defined below by idx_data table.
        :rtype: Dataframe
    
        ========   ======================   ============================================================
        idx_data            Name                                    Description
        ========   ======================   ============================================================
            0       PlayerStats             Traditional box scores on an individual player basis.
            1       TeamStats               Traditional box scores on a team basis.
            2       TeamStarterBenchStats   Traditional box scores on a starter vs bench split per team.
        ========   ======================   ============================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscoretraditionalv2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df

    def boxscoreusage(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                      StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get usage stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: Usage stats on a player/team, as defined below by idx_data.
        :rtype: Dataframe
    
        ========   ================   ==================================================
        idx_data       Name                            Description
        ========   ================   ==================================================
            0       sqlPlayersUsage   Usage stats on an individual player basis.
            1       sqlTeamsUsage     Usage stats on a team basis.
        ========   ================   ==================================================
    
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscoreusagev2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df

    def boxscoresummary(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                        StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get high level game summary stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: high level game information, as defined below by idx_data table below.
        :rtype: Dataframe
    
        ========   ================   ==================================================
        idx_data       Name                             Description
        ========   ================   ==================================================
            0       GameSummary       High level overview of game information.
            1       OtherStats        Other high level game stats.
            2       Officials         Officials names and id's.
            3       InactivePlayers   Players not on roster for game.
            4       GameInfo          Date, attendance, time.
            5       LineScore         Scores by period.
            6       LastMeeting       Most recent meeting score and game info.
            7       SeasonSeries      Series results so far this season.
            8       AvailableVideo    Availability by video type.
        ========   ================   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscoresummaryv2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df

    def boxscoreplayertrack(self, GameID, idx_data, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default,
                            StartRange=enums.StartRange.Default, EndRange=enums.EndRange.Default, RangeType=enums.RangeType.Default):
        """
        Get player tracking box score stats for a given game.
    
        :param GameID: id for the game to get data for.
        :type GameID: str
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param StartPeriod: filter starting quarter to retrieve data for.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: filter upper quarter cutoff for data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :param StartRange: mandatory in url build, appear to have no effect.
        :type StartRange: nba.nba.bin.enums.StartRange
        :param EndRange: mandatory in url build, appear to have no effect.
        :type EndRange: nba.nba.bin.enums.EndRange
        :param RangeType: mandatory in url build, appear to have no effect.
        :type RangeType: nba.nba.bin.enums.RangeType
        :returns: player tracking box score stats by player or team, as defined below by idx_data table below.
        :rtype: Dataframe
    
        ========   ================   =========================================================
        idx_data       Name                                Description
        ========   ================   =========================================================
            0       PlayerTrack       Player tracking box scores on an individual player basis.
            1       PlayerTrackTeam   Player tracking box scores on a team basis.
        ========   ================   =========================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'boxscoreplayertrackv2'
        r = self.request(endpoint, params)
        df = self.process_response(r.json(), idx_data, 'resultSets')
        return df
