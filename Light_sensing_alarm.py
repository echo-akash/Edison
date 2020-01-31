import Ed

Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

while Ed.ReadLeftLightLevel()<100:
    pass
while True:
    Ed.PlayBeep()
    
