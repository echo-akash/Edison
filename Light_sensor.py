#activates light when it is dark

import Ed

Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.Drive(Ed.FORWARD, Ed.SPEED_6, Ed.DISTANCE_UNLIMITED)

while True:
    if(Ed.ReadLeftLightLevel()<100):
        activateBothLights(Ed.ON)
    else:
        activateBothLights(Ed.OFF)

def activateBothLights(stateOfLed):
    Ed.LeftLed(stateOfLed)
    Ed.RightLed(stateOfLed)
    
