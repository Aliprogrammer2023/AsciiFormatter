import pyfiglet
from termcolor2 import colored
# Import the os module to create and write files
import os
# Import the PIL module to convert text to image
from PIL import Image, ImageDraw, ImageFont

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
            # Create a font object with the chosen font name and size
            font = ImageFont.truetype(font_name + ".flf", 32)
            # Draw the ASCII art on the image with black color
            draw.text((10, 10), ascii_format, (0, 0, 0), font=font)
            # Save the image as png file
            image.save(file_name + ".png")
            print(f"Your ASCII art is saved as {file_name}.png")
        else:
            print("Invalid file format. Please try again.")
    else:
        print("OK. Have a nice day.")
except:
    print("sorry! Something went wrong! Please try again")
