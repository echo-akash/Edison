import Ed

Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

for i in range(10):
    Ed.PlayTone(100+(i*5), 5000)
    while Ed.ReadMusicEnd()==Ed.MUSIC_NOT_FINISHED:
        pass
