#Write Edison by using edison robot

import Ed
Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_VERY_FAST

round_button = False
PAUSE_LENGTH = 2

def buttonEvent():
    global round_button
    round_button = True

def waitToRoundButton():
    global round_button
    round_button = False
    Ed.PlayTone(15289,100)
    while round_button == False:
        pass
    Ed.PlayTone(7644,100)
    Ed.TimeWait(PAUSE_LENGTH, Ed.TIME_SECONDS);

Ed.RegisterEventHandler(Ed.EVENT_KEYPAD_ROUND, "buttonEvent");

# >> E <<
Ed.PlayTone(7644,100)
Ed.TimeWait(PAUSE_LENGTH, Ed.TIME_SECONDS);
Ed.DriveRightMotor(Ed.BACKWARD,Ed.SPEED_1,Ed.DISTANCE_UNLIMITED)
Ed.DriveLeftMotor(Ed.BACKWARD,Ed.SPEED_9
                  ,Ed.DISTANCE_UNLIMITED)
Ed.TimeWait(1500, Ed.TIME_MILLISECONDS);
Ed.Drive(Ed.STOP,1,1);
waitToRoundButton()
Ed.Drive(Ed.BACKWARD,1,15);
waitToRoundButton()

# >> d <<
Ed.Drive(Ed.SPIN_LEFT,1,180);
Ed.Drive(Ed.STOP,1,1);
Ed.TimeWait(500, Ed.TIME_MILLISECONDS);
Ed.Drive(Ed.BACKWARD,1,24);
waitToRoundButton()

# >> i <<
Ed.Drive(Ed.BACKWARD,1,15);
waitToRoundButton()
Ed.Drive(Ed.BACKWARD,1,1);
waitToRoundButton()

# >> s <<
Ed.Drive(Ed.SPIN_LEFT,1,90);
Ed.Drive(Ed.BACKWARD,1,7);
waitToRoundButton()
Ed.Drive(Ed.SPIN_RIGHT,1,90);
waitToRoundButton()

# >> o <<
Ed.Drive(Ed.SPIN_LEFT,1,360);
waitToRoundButton()

# >> n <<
Ed.Drive(Ed.BACKWARD,1,14);
waitToRoundButton()
Ed.Drive(Ed.SPIN_RIGHT,1,90);
waitToRoundButton()
Ed.Drive(Ed.BACKWARD,1,7);
waitToRoundButton()
