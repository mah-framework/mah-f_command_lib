# https:/github.com/C0derByM4H6301
from colorama import *
import os
import sys
from pyfiglet import Figlet
f = Figlet(font='slant')
print(Fore.BLUE+f.renderText('Mah-framework'))
print(Fore.RESET)
def pwd():
    print(os.getcwd())



#input_string = Fore.LIGHTBLUE_EX+"mah-f>" + Fore.RESET+" "
input_string = "mah-f> "
while True:
    sh = input(input_string)
    cmd_list = []
    for i in sh.split(" "):
        if i != "" and i != " ":
            cmd_list.append(i)
    len_cmd_list = len(cmd_list)
    print(cmd_list)
    print(len_cmd_list)
    if len_cmd_list >= 1:
        if cmd_list[0] == "exit":
            print("goodbye!")
            break
        if cmd_list[0] == "pwd":
            pwd()
      
