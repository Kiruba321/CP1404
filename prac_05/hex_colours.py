COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff",
                "Aquamarine": "#7fffd4", "Azure": "#f0ffff", "Beige": "#f5f5dc",
                "Bisque": "#ffe4c4", "Black": "#000000", "BlanchedAlmond": "#ffebcd",
                "Blue": "#0000ff", "BlueViolet": "#8a2be2", "Brown": "#a52a2a",
                }

name_colour = input("Enter a colour name: ")
while name_colour != "":
    print(f"The code for \"{name_colour}\" is {COLOUR_CODES.get(name_colour)}")
    name_colour = input("Enter a colour name: ")