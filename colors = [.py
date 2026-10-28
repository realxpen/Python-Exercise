colors = [
    "red", "orange",
    "yellow", "green",
    "blue", "purple"
]
width = 4
for hue in colors:
    row = ""
    for i in range(width):
        row += hue + " "
    print(row)