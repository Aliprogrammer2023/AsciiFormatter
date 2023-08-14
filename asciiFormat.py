import pyfiglet
from termcolor2 import colored
try:
    text=input('Enter your text: ')
    color=input('Enter your color: ')
    ascii_format=pyfiglet.figlet_format(text)
    ascii_format=colored(ascii_format,color=color)
    print(ascii_format)
except:
    print("sorry! Something went wrong! Please try again")