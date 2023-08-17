# Import the os module to create and write files
import os
# Import the PIL module to convert text to image
from PIL import Image, ImageDraw, ImageFont
# Import pyfiglet and termcolor2 modules to create ASCII art
import pyfiglet
from termcolor2 import colored
import termcolor2
# Import the time module to create delays between each frame of animation
import time
# Import the curses module to control the terminal output
import curses

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
    # Ask the user if they want to save the ASCII art as a file
    save = input("Do you want to save the ASCII art as a file? (y/n): ")
    # If yes, ask the user for the file name and format
    if save.lower() == "y":
        file_name = input("Enter the file name: ")
        file_format = input("Enter the file format (txt or png): ")
        # If txt, create a text file and write the ASCII art to it
        if file_format.lower() == "txt":
            with open(file_name + ".txt", "w") as f:
                f.write(ascii_format)
            print(f"Your ASCII art is saved as {file_name}.txt")
        # If png, create an image file and draw the ASCII art on it
        elif file_format.lower() == "png":
            # Create a blank image with white background
            image = Image.new("RGB", (800, 600), (255, 255, 255))
            # Create a draw object to draw on the image
            draw = ImageDraw.Draw(image)
            # Create a font object with a different font name and size
            # You can change this to any TrueType font file you have or download one from [here]
            font = ImageFont.truetype("arial.ttf", 32)
            # Draw the ASCII art on the image with black color
            draw.text((10, 10), ascii_format, (0, 0, 0), font=font)
            # Save the image as png file
            image.save(file_name + ".png")
            print(f"Your ASCII art is saved as {file_name}.png")
        else:
            print("Invalid file format. Please try again.")
    else:
        print("OK")
    # Ask the user if they want to create animated ASCII art
    animate = input("Do you want to create animated ASCII art? (y/n): ")
    # If yes, ask the user for the number of frames and the speed of animation
    if animate.lower() == "y":
        frames = int(input("Enter the number of frames: "))
        speed = float(input("Enter the speed of animation (in seconds): "))
        # Initialize the curses module and get a window object
        stdscr = curses.initscr()
        # Turn on color support
        curses.start_color()
        # Define some color pairs using RGB values
        # You can change these values or add more pairs as you like
        curses.init_color(1, 1000, 0, 0) # Red
        curses.init_color(2, 0, 1000, 0) # Green
        curses.init_color(3, 0, 0, 1000) # Blue
        curses.init_color(4, 1000, 1000, 0) # Yellow
        curses.init_color(5, 1000, 0, 1000) # Magenta
        curses.init_color(6, 0, 1000, 1000) # Cyan
        curses.init_color(7, 1000, 1000, 1000) # White
        
        # Associate each color with a number from 1 to 7
        curses.init_pair(1, 1, curses.COLOR_BLACK) # Red on black background
        curses.init_pair(2, 2, curses.COLOR_BLACK) # Green on black background
        curses.init_pair(3, 3, curses.COLOR_BLACK) # Blue on black background
        curses.init_pair(4, 4, curses.COLOR_BLACK) # Yellow on black background
        curses.init_pair(5, 5, curses.COLOR_BLACK) # Magenta on black background
        curses.init_pair(6, 6, curses.COLOR_BLACK) # Cyan on black background
        curses.init_pair(7, 7, curses.COLOR_BLACK) # White on black background
        
        # Turn off echoing of keys and enable keypad mode
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        # Clear the screen and hide the cursor
        curses.curs_set(0)
        stdscr.clear()
        # Loop through each frame of animation
        for i in range(frames):
            # Create a new ASCII art with the chosen font
            ascii_format=pyfiglet.figlet_format(text, font=font_name)
            # Get the attribute value for the color pair corresponding to the frame number
            attr = curses.color_pair((i % 7) + 1)
            # Add the ASCII art to the window object at position (0, 0) with the color attribute
            stdscr.addstr(0, 0, ascii_format, attr)
            # Refresh the window object to show the changes
            stdscr.refresh()
            # Wait for a specified amount of time before moving to the next frame
            time.sleep(speed)
        # Restore the terminal settings and close the window object
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        print("Your animated ASCII art is done.")
    else:
        print("OK. Have a nice day.")
except:
    print("sorry! Something went wrong! Please try again")


