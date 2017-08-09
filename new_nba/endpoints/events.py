
import pandas as pd

from new_nba.utils import clean_locals
from new_nba.endpoints.baseendpoint import BaseEndpoint


class Events(BaseEndpoint):

    def locations_getmoments(self, GameID, EventID):
        """
        ***Blocked Cannot Access***
        Get location moments for each player throughout a single game event.
    
        :param GameID: ID of the game to get location data from.
        :type GameID: str
        :param EventID: ID of specific game event.
        :type EventID: int
        :returns: location data for each snapshot in the event.
        :rtype: Dataframe
    
        """
        endpoint = 'locations_getmoments'
        params = clean_locals(locals())
        r = self.request(params, endpoint)
        if len(r) > 0:
            try:
                headers = ["TeamID", "PlayerID", "x_loc", "y_loc", "Radius", "MomentID", "GameClock", "ShotClock", "EventID"]
                player_moments = []
                moments = r['moments']
                for moment in moments:
                    for player in moment[5]:
                        player.extend((moments.index(moment), moment[2], moment[3], EventID))
                        player_moments.append(player)
                df = pd.DataFrame(player_moments, columns=headers)
            except:
                df = pd.DataFrame()
        else:
            df = pd.DataFrame()
        return df


    def locations_getallmoments(self, GameID, limit):
        """
        ***Blocked Cannot Access***
        Get location moments for all events IDs up to set limit.
    
        :param GameID: ID of the game to get location data from.
        :type GameID: str
        :param limit: depth to iterate through game events.
        :type limit: int
        :returns: location moments for all players for each event up to limit.
        :rtype: Dataframe
    
        """
        endpoint = 'locations_getmoments'
        df = pd.DataFrame()
        for i in range(1, int(limit)):
            params = {'GameID': GameID, 'EventID': str(i)}
            r = self.request(params, endpoint)
            if len(r) > 0:
                try:
                    headers = ["TeamID", "PlayerID", "x_loc", "y_loc",
                               "Radius", "MomentID", "GameClock", "ShotClock", "EventID"]
                    player_moments = []
                    moments = r['moments']
                    for moment in moments:
                        for player in moment[5]:
                            player.extend((moments.index(moment), moment[2], moment[3], i))
                            player_moments.append(player)
                    temp = pd.DataFrame(player_moments, columns=headers)
                    df = pd.concat([df, temp])
                except:
                    continue
            else:
                continue
        return df
