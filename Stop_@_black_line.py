#Move in White surface
#Stop when find black line



import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.LineTrackerLed(Ed.ON)

Ed.Drive(Ed.FORWARD, Ed.SPEED_7, Ed.DISTANCE_UNLIMITED)

while True:
    if(Ed.ReadLineState()==Ed.LINE_ON_BLACK):
        Ed.PlayBeep()
        Ed.Drive(Ed.STOP, Ed.SPEED_1, 0)
