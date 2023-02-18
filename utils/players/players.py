## Import for dummy API Call
import random
import numpy as np
## End Import

class Player():
    def __init__(self, id):
        self.playerInfo = self.getPlayerInfo(id)
        
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
        players = [
            {'Fname': 'John',
             'Lname': 'Smith',
             'Position': 'Center',
             'Profile' : 'https://hyunsuk-ryoo.com/img/profile.jpg',
             'PlayerId': id,
             'PhysicalInformation' : {'Height': height,'Weight': weight,'Age' : age},
             'Points': points,
             'Assists': assists
            },
            {'Fname': 'John2',
             'Lname': 'Smith2',
             'Position': 'PF',
             'Profile' : 'https://hyunsuk-ryoo.com/img/profile.jpg',
             'PlayerId': id,
             'PhysicalInformation' : {'Height': height,'Weight': weight,'Age' : age},
             'Points': points,
             'Assists': assists
            },
            {'Fname': 'John3',
             'Lname': 'Smith3',
             'Position': 'PG',
             'Profile' : 'https://hyunsuk-ryoo.com/img/profile.jpg',
             'PlayerId': id,
             'PhysicalInformation' : {'Height': height,'Weight': weight,'Age' : age},
             'Points': points,
             'Assists': assists
            }
        ]
        random.seed(id)
        selectedIndex = np.random.randint(0, len(players))
        selectedPlayer = players[selectedIndex]
        return selectedPlayer