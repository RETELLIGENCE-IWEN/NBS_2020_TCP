# RETELLIGENCE IEZANOV IWEN

import json

ActionCommand = {
    "ActionNumbers": 2,
    "Actions":[
        {
            "Id": 0,                # Unit Id
            "Engine": 5,            # Engine Speed (0=R, 1=N, 2, 3, 4, 5)
            "Direction": 1,         # Steering Direction (-2, -1, 0, 1, 2)
            "Radar": 1,             # Radar On/Off
            "NavalGun": 1,          # Fire ?
            "N_FireTargetId": 3,    # Target ID
            "Missile": 0,           # Fire ?
            "M_FireTargetId": 3,    # Target ID
            "Torpedo": 0,           # Fire ?
            "T_FireTargetId": 3     # Target ID

        },
        {
            "Id": 3,
            "Engine": 5,
            "Direction": 0,
            "Radar": 1,
            "NavalGun": 0,
            "N_FireTargetId": 0,
            "Missile": 1,
            "M_FireTargetId": 0,
            "Torpedo": 0,
            "T_FireTargetId": 0          
        },
    ]
}



StatusReport = {
    'Unit_4': [      # Unit Name
        4,           # ID
        100,         # Current Health
        7130,        # Location X
        -56,         # Location Y
        False,       # Team (ally)
        True,        # Found Enemy
        9774,        # Enemy Location X
        1234,        # Enemy Location Y
        0            # Enemy ID
    ], 
    'Unit_0': [
        0,           # ID
        100,         # Current Health
        -7130,       # Location X
        56,          # Location Y
        True,        # Team (ally)
        True,        # Found Enemy
        9774,        # Enemy Location X
        123,           # Enemy Location Y
        4            # Enemy ID
    ]
}