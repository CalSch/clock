#!/usr/bin/env python3
import os,math,time,argparse
from datetime import datetime


colors={
    "red":"41",
    "green":"42",
    "yellow":"43",
    "blue":"44",
    "magenta":"45",
    "cyan":"46",
    "white":"47"
}

parser = argparse.ArgumentParser(
    prog = 'Clock',
    description = 'A clock app',
    epilog = 'Source code at https://github.com/CalSch/clock')
parser.add_argument('-f','--format',default="%I:%M:%S %p",help="The time format of the clock")
parser.add_argument('-c','--color',default='cyan',help="The color of the clock")
parser.add_argument('-r','--refresh',metavar="SECONDS",default='0.5',help="The seconds between refreshing the clock, values below 0.02 may cause the clock to flicker based on the terminal's speed",type=float)

args = parser.parse_args()



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
 ##
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
 ##""",
"A":"""
 ##
#  #
####
#  #
#  #""",
"P":"""
###
#  #
###
#
#   """,
"M":"""
#   #
## ##
# # #
#   #
#   #""",
"-":"""


 ##

""",
" ":"""




"""
}

c_width=10
c_height=5

def padSpace(s,l):
    return s+(" "*(int(l)-len(s)))

def printTime():
    now=datetime.now()
    time_string=now.strftime(args.format)
    size=os.get_terminal_size()
    width=size.columns
    height=size.lines

    string=""
    for char in time_string:
        try:
            font_char=font[char]
            i=0
            for line in font_char.split('\n'):
                line=padSpace(line,c_width/2)
                line=line.replace(" ","  ").replace("#","##")
                line=line.replace("#","\x1b["+colors[args.color]+"m \x1b[0m")
                string+=line
                string+="\x1b[1B\x1b["+str(c_width)+"D"
                i+=1
            #string+=padSpace(font_char,4).replace("\n","\x1b[1B\x1b[2D")
            string+="\x1b["+str(c_height+1)+"A\x1b["+str(c_width)+"C"
        except KeyError:
            string+="X"
    
    print("\x1b[2J\x1b[H")
    print(" "*int((width-len(time_string))/2)+time_string)
    print("\n"*(int((height-8)/2)-2))
    print("\n\n\n\n\n\n\n\x1b[7A")

    print((" "*int((width-len(time_string)*(c_width+2))/2))+string)

    print("\n"*(int((height-(c_height))/2)+2))
    

while True:
    printTime()
    time.sleep(float(args.refresh))


