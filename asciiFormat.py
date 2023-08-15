import pyfiglet
from termcolor2 import colored

try:
    text=input('Enter your text: ')
    color=input('Enter your color: ')
    # Get the list of available fonts from pyfiglet
    fonts = pyfiglet.FigletFont.getFonts()
    # Print the list of fonts with numbers
    print("Here are the available fonts:")
    for i, font in enumerate(fonts):
        print(f"{i+1}. {font}")
    # Ask the user to enter a number to choose a font
    font_number = int(input("Enter a number to choose a font: "))
    # Get the corresponding font name from the list
    font_name = fonts[font_number-1]
    # Create the ASCII art with the chosen font
    ascii_format=pyfiglet.figlet_format(text, font=font_name)
    ascii_format=colored(ascii_format,color=color)
    print(ascii_format)
except:
    print("sorry! Something went wrong! Please try again")
