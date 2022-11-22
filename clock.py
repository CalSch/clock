#!/usr/bin/env python3
import os,math,time
from datetime import datetime

font={
"0":"""
 ## 
#  #
#  #
#  #
 ## """,
"1":"""
 ##
  #
  #
  #
 ###""",
"2":"""
 ##
#  #
  #
 #
####""",
"3":"""
### 
   #
 ## 
   #
### """,
"4":"""
   #
  ##
 # #
####
   #""",
"5":"""
####
#
###
   #
### """,
"6":"""
 ###
#
###
#  #
 ## """,
"7":"""
####
   #
  #
 #
#   """,
"8":"""
 ##
#  #
 ##
#  #
 ## """,
"9":"""
 ##
#  #
 ###
   #
 ## """,
":":"""
 ##
 ##

 ##
 ##"""
}

c_width=8
c_height=5

def padSpace(s,l):
    return s+(" "*(l-len(s)))

def printTime():
    now=datetime.now()
    time_string=now.strftime("%H:%M:%S")
    size=os.get_terminal_size()
    width=size.columns
    height=size.lines

    string=""
    for char in time_string:
        try:
            font_char=font[char]
            i=0
            for line in font_char.split('\n'):
                line=padSpace(line,4)
                line=line.replace(" ","  ").replace("#","##")
                line=line.replace("#","\x1b[46m \x1b[0m")
                string+=line
                string+="\x1b[1B\x1b["+str(c_width)+"D"
                i+=1
            #string+=padSpace(font_char,4).replace("\n","\x1b[1B\x1b[2D")
            string+="\x1b["+str(c_height+1)+"A\x1b["+str(c_width+2)+"C"
        except KeyError:
            string+="X"
    
    print("\x1b[2J\x1b[H")
    print(" "*math.floor((width-len(time_string))/2)+time_string)
    print("\n"*(math.floor((height-8)/2)-2))
    print("\n\n\n\n\n\n\n\x1b[7A")

    print((" "*math.floor((width-len(time_string)*(c_width+2))/2))+string)

    print("\n"*(math.floor((height-(c_height))/2)+2))
    

while True:
    printTime()
    time.sleep(0.5)


