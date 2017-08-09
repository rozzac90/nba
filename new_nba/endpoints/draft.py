

from new_nba import enums
from new_nba.utils import clean_locals
from new_nba.endpoints.baseendpoint import BaseEndpoint


class Common(BaseEndpoint):
    
    def draftcombinedrillresults(self, LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
        """
        Combine drill results for a given year.
    
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param SeasonYear: draft season.
        :type SeasonYear: str('%Y-%y')
        :returns: Combine drill results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'draftcombinedrillresults'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def draftcombinenonstationaryshooting(self, LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
        """
        Moving shooting scores broken down by movement type.
    
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param SeasonYear: draft season.
        :type SeasonYear: str('%Y-%y')
        :returns: Movement shooting results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'draftcombinenonstationaryshooting'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def draftcombineplayeranthro(self, LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
        """
        Detailed breakdown of players measurements and physical stats.
    
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param SeasonYear: draft season.
        :type SeasonYear: str('%Y-%y')
        :returns: Measurements and physical information by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'draftcombineplayeranthro'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def draftcombinespotshooting(self, LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
        """
        Get raw and pct shooting results from draft combine for a given year.
    
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param SeasonYear: draft season.
        :type SeasonYear: str('%Y-%y')
        :returns: Combine shooting results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'draftcombinespotshooting'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def draftcombinestats(self, LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
        """
        Get combine results for a draft year.
    
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :param SeasonYear: draft season.
        :type SeasonYear: str('%Y-%y')
        :returns: Combine results by player.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'draftcombinestats'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def drafthistory(self, LeagueID=enums.LeagueID.Default):
        """
        Breakdown of pick number and player data for historical drafts.
    
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :returns: Player pick numbers for historic drafts.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'drafthistory'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def franchisehistory(self, idx_data, LeagueID=enums.LeagueID.Default):
        """
        Breakdown of each franchise's record in the NBA.
    
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param LeagueID: define league to look at, nba.
        :type LeagueID: nba.nba.bin.enums.LeagueID
        :returns: franchise information.
        :rtype: Dataframe
    
        ========   =================   ==================================================
        idx_data          Name                        Description
        ========   =================   ==================================================
            0       FranchiseHistory   Win/Loss Record and Titles Info for franchises.
            1       DefunctTeams       Franchises no longer in NBA.
        ========   =================   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'franchisehistory'
        r = self.request(params, endpoint)
        df = self.process_response(r, idx_data, 'resultSets')
        return r
