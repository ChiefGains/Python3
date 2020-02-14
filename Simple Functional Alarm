#!/user/bin/env Python3

from time import strftime as now
#imports the module that returns the current time

from playsound import playsound as play
#imports the module to play music

alarm_time = str(7:00:00)
#sets the alarm for 7am. Can have the user set alarm using input() or with GPIO, but that falls outside of the scope of this program

song = r'C:\\generic_filepath.mp3'
#tells the program what song to play for the alarm

while True:
  if alarm_time == now:
    play(song)
    break
    #this loop will continually check the time until it's time for the alarm to go off,
    #at which time it will play the song and close the program
    
    
#at some point I'll add more support for cross-platform use (for instance, many unix systems don't like the playsound modue),
#but that falls outside of the scope of this simple program
