""""This script allows a computer user to take a break from
the continuous usage of his or her computer.
It opens a webpage at every time interval. The time nterval varies  depending on the user.

"""
import time
import webbrowser


def breaktime():

    for i in range(1, 5):  #This determines the number of times the
        # program has to run in a given day.
        time.sleep(3)  #This builtin function takes in value in seconds.
        webbrowser.open('http://www.twitter.com')  #This function takes in a webpage as a string

breaktime()