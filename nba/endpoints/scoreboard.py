
from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Scoreboard(BaseEndpoint):

    def scoreboard(self, GameDate, idx_data, DayOffSet=0, LeagueID=enums.LeagueID.Default):
        """
        Get the scoreboard and game data from a give date/date with offset.
    
        :param GameDate: reference date to get data for.
        :type GameDate: str('%Y-%m-%d')
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param DayOffSet: Number days prior to GameDate to get data for.
        :type DayOffSet: int
        :param LeagueID: league to retrieve data for.
        :type LeagueID: str
        :returns:
        :rtype: Dataframe
    
        ========   =======================   ======================================================
        idx_data           Name                                  Description
        ========   =======================   ======================================================
            0       GameHeader                Overview of games returned.
            1       LineScore                 Score by period on a team basis and some basic stats.
            2       SeriesStandings           Season series current standing.
            3       LastMeeting               Last game info id, time, and scores
            4       EastConfStandingsByDay    Full standings for the Eastern Conference.
            5       WestConfStandingsByDay    Full standings for the Eastern Conference.
            6       Available                 Whether video is available for each game.
            7       TeamLeaders               Top players for each team by basic stats.
            8       TicketLinks               Links to buy tickets.
            9       WinProbability            Probability of team winning, often empty.
        ========   =======================   ======================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'scoreboardV2'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    #
    # def live_scores():
    #     r = requests.get(r'http://data.nba.com/data/5s/v2015/json/mobile_teams/nba/2016/scores/00_todays_scores.json')
    #     scores_df = json_normalize(r.json().get('gs').get('g'))
    #     scores_df.loc[:, 'TIMESTAMP'] = dt.datetime.utcnow()
    #     scores_df = scores_df[
    #         ['TIMESTAMP', 'gcode', 'gid', 'st', 'stt', 'p', 'cl', 'h.tid', 'h.tc', 'h.tn', 'h.ta', 'v.tid', 'v.tc',
    #          'v.tn', 'v.ta', 'h.s', 'v.s']]
    #     scores_df.loc[:, 'SCORE_DIFF'] = scores_df['v.s'] - scores_df['h.s']
    #     scores_df.rename(columns={'gcode': 'GAMECODE', 'cl': 'TIME_REMAINING', 'gid': 'GAME_ID', 'p': 'LIVE_PERIOD',
    #                               'st': 'GAME_STATUS_ID', 'stt': 'GAME_STATUS_TEXT',
    #                               'h.tc': 'HOME_TEAM_CITY_NAME', 'v.tc': 'VISITOR_TEAM_CITY_NAME',
    #                               'h.tid': 'HOME_TEAM_ID', 'v.tid': 'VISITOR_TEAM_ID',
    #                               'h.tn': 'HOME_TEAM_NAME', 'v.tn': 'VISITOR_TEAM_NAME',
    #                               'h.ta': 'HOME_TEAM_ABBREVIATION', 'v.ta': 'VISITOR_TEAM_ABBREVIATION',
    #                               'h.s': 'HOME_TEAM_SCORE', 'v.s': 'VISITOR_TEAM_SCORE'}, inplace=True)
    #     return scores_df