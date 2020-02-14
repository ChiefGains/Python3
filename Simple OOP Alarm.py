#alarm that uses OOP rather than functional or procedural programming

#first, import the modules to check time and play sound
from time import strftime as now
from playsound import playsound as play

#set the time you'd like to wake up
time1 = '7:00:00'

#now, select a song to play
song1 = r'Generic_filepath.mp3'
#the rawstring ('r') prevents unicode escape from the windows filepath

#We must make a class as a blueprint for our alarm
class Alarm:
    def __init__(self, time, song):
        self.time = time
        self.song = song

    def check_alarm(self):
        while True:
            if self.time == now('%H:%M:%S'):
                play(self.song)

#Let's instantiate an object named "alarm1" that takes time1 and song1 as its __init__() arguments
alarm1 = Alarm(time1, song1)

#Now, let's call the function in the alarm that checks the time and plays the song
alarm1.check_alarm()
