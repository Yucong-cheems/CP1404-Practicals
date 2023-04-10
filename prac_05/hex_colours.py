"""
hex_colours
Estimate: 10 minutes
Actual:   8 minutes
"""

color = {"Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
         "AntiqueWhite2": "#eedfcc",
         "AntiqueWhite3": "#cdc0b0"}
print(color)

color_name = input("Enter a color name: ").title()

while color_name != " ":
    if color_name in color:
        print(color_name, "is", color[color_name])

    else:
        print("invalid input")

    color_code = input("Enter a color name: ").title()