## Import for dummy API Call
import random
import numpy as np
## End Import

class Player():
    def __init__(self, id):
        if id == -1:
            self.playerInfo = self.getAllPlayers()
        else:
            self.playerInfo = self.getPlayerInfo(id)
        
    def getAllPlayers(self):
        mock_api_call =  [
            {
                'Name': 'Max Ryoo',
                'id': 1,
                'Team': 'UVA'
            },
            {
                'Name': 'Seth Galluzzi',
                'id': 2,
                'Team' : 'UVA'
            },
            {
                'Name': 'Cepehr Alizadeh',
                'id': 3,
                'Team' : 'UVA'
            }, 
            {
                'Name' : 'Jonathan Kropko',
                'id': 4,
                'Team' : 'UVA'
            }
        ]
        return mock_api_call

        
    def getPlayerInfo(self, id):
        ## Dummy Call for Player Information
        random.seed(id)
        height = np.random.randint(160, 240)
        random.seed(id)
        weight = np.random.randint(100, 300)
        random.seed(id)
        age = np.random.randint(18, 24)
        random.seed(id)
        ## Randomize Points Made
        points = [random.randint(5, 30) for i in range(0, 10)]
        assists = [random.randint(5, 10) for i in range(0, 10)]
        
        ## Mock
        playerList = self.getAllPlayers()
        player = [player for player in playerList if player['id'] == int(id)]
        
        selectedPlayer = {
             'Fname': player[0]['Name'].split()[0],
             'Lname': player[0]['Name'].split()[1],
             'Position': 'Center',
             'Profile' : 'https://hyunsuk-ryoo.com/img/profile.jpg',
             'PlayerId': id,
             'PhysicalInformation' : {'Height': height,'Weight': weight,'Age' : age},
             'Points': points,
             'Assists': assists
            }
        return selectedPlayer