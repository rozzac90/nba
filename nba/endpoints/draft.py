from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Draft(BaseEndpoint):
    def combine_drill_results(
        self, league_id=enums.LeagueID.Default, season_year="2016-17"
    ):
        """
        Combine drill results for a given year.
    
        :param league_id: define league to look at, nba.
        :type league_id: nba.enums.LeagueID
        :param season_year: draft season.
        :type season_year: str('%Y-%y')
        :returns: Combine drill results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = "draftcombinedrillresults"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def combine_stationary_shooting(
        self, league_id=enums.LeagueID.Default, season_year="2016-17"
    ):
        """
        Moving shooting scores broken down by movement type.
    
        :param league_id: define league to look at, nba.
        :type league_id: nba.enums.LeagueID
        :param season_year: draft season.
        :type season_year: str('%Y-%y')
        :returns: Movement shooting results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = "draftcombinenonstationaryshooting"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def combine_player_anthropology(
        self, league_id=enums.LeagueID.Default, season_year="2016-17"
    ):
        """
        Detailed breakdown of players measurements and physical stats.
    
        :param league_id: define league to look at, nba.
        :type league_id: nba.enums.LeagueID
        :param season_year: draft season.
        :type season_year: str('%Y-%y')
        :returns: Measurements and physical information by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = "draftcombineplayeranthro"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def combine_spot_shooting(
        self, league_id=enums.LeagueID.Default, season_year="2016-17"
    ):
        """
        Get raw and pct shooting results from draft combine for a given year.
    
        :param league_id: define league to look at, nba.
        :type league_id: nba.enums.LeagueID
        :param season_year: draft season.
        :type season_year: str('%Y-%y')
        :returns: Combine shooting results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = "draftcombinespotshooting"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def combine_stats(self, league_id=enums.LeagueID.Default, season_year="2016-17"):
        """
        Get combine results for a draft year.
    
        :param league_id: define league to look at, nba.
        :type league_id: nba.enums.LeagueID
        :param season_year: draft season.
        :type season_year: str('%Y-%y')
        :returns: Combine results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = "draftcombinestats"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df

    def history(self, league_id=enums.LeagueID.Default):
        """
        Breakdown of pick number and player data for historical drafts.
    
        :param league_id: define league to look at, nba.
        :type league_id: nba.enums.LeagueID
        :returns: Player pick numbers for historic drafts.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = "drafthistory"
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, "resultSets")
        return df
