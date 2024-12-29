"""
Used to color the text and background while displaying results.
The purpose of this is to help keep color consistency between programs using this import, allowing consistent and easy
reading no matter what game is using this import to randomize files
"""
# Used to better communicate how the methods effected files
# Used to make Errors displayed with result easier to find and more noticeable
RED_BACKGROUND = '\033[41m'  # Error triggered by errors in the actual code
YELLOW_BACKGROUND = '\033[43m'  # Error triggered by failing an statement
RED = '\033[31m'  # Marks the original value or trait after change or shuffle
GREEN = '\033[32m'  # Mark the new value or trait after change or shuffle
YELLOW = '\033[33m'  # Mark if value or trait is unchanged

RESET = '\033[0m'  # removes all effects

# Used to better communicate the grouping of methods effected files
# These are th colors used for color differentiation between methods,
# These are the recommend colors to be used.
METHODS = (
    # Reds
    "#FF0000",  # [1]Red
    "#FF6347",  # [2]Tomato
    "#DC143C",  # [3]Crimson
    "#CD5C5C",  # [4]IndianRed
    "#FFA07A",  # [5]LightSalmon
    "#FA8072",  # [6]Salmon
    "#FF4500",  # [7]OrangeRed
    "#FF7F50",  # [8]Coral
    # Oranges
    "#FF8C00",  # [9]DarkOrange
    "#FFA500",  # [10]Orange
    "#FFD700",  # [11]Gold
    "#FFA07A",  # [12]LightSalmon
    "#F08080",  # [13]LightCoral
    # Yellows
    "#FFFF00",  # [14]Yellow
    "#F0E68C",  # [15]Khaki
    "#EEE8AA",  # [16]PaleGoldenRod
    "#FAFAD2",  # [17]LightGoldenRodYellow
    "#9ACD32",  # [18]YellowGreen
    # Greens
    "#008000",  # [19]Green
    "#006400",  # [20]DarkGreen
    "#228B22",  # [21]ForestGreen
    "#32CD32",  # [22]LimeGreen
    "#7FFF00",  # [23]Chartreuse
    "#7CFC00",  # [24]LawnGreen
    "#00FF00",  # [25]Lime
    "#00FA9A",  # [26]MediumSpringGreen
    "#3CB371",  # [27]MediumSeaGreen
    "#2E8B57",  # [28]SeaGreen
    "#90EE90",  # [29]LightGreen
    "#98FB98",  # [30]PaleGreen
    # Cyan/Turquoise
    "#00FFFF",  # [31]Aqua
    "#7FFFD4",  # [32]Aquamarine
    "#40E0D0",  # [33]Turquoise
    "#48D1CC",  # [34]MediumTurquoise
    "#00CED1",  # [35]DarkTurquoise
    "#5F9EA0",  # [36]CadetBlue
    "#20B2AA",  # [37]LightSeaGreen
    # Blues
    "#0000FF",  # [38]Blue
    "#0000CD",  # [39]MediumBlue
    "#1E90FF",  # [40]DodgerBlue
    "#4169E1",  # [41]RoyalBlue
    "#6495ED",  # [42]CornflowerBlue
    "#87CEEB",  # [43]SkyBlue
    "#87CEFA",  # [44]LightSkyBlue
    "#4682B4",  # [45]SteelBlue
    "#191970",  # [46]MidnightBlue
    # Purples
    "#8A2BE2",  # [47]BlueViolet
    "#9932CC",  # [48]DarkOrchid
    "#BA55D3",  # [49]MediumOrchid
    "#9370DB",  # [50]MediumPurple
    "#9400D3",  # [51]DarkViolet
    "#8B008B",  # [52]DarkMagenta
    "#800080",  # [53]Purple
    "#663399",  # [54]RebeccaPurple
    "#DDA0DD",  # [55]Plum
    "#EE82EE",  # [56]Violet
    "#D8BFD8",  # [57]Thistle
    "#DA70D6",  # [58]Orchid
    # Pinks
    "#FF69B4",  # [59]HotPink
    "#FF1493",  # [60]DeepPink
    "#FFC0CB",  # [61]Pink
    "#FFB6C1",  # [62]LightPink
    "#DB7093",  # [63]PaleVioletRed
    "#C71585",  # [64]MediumVioletRed
    # Browns
    "#8B4513",  # [65]SaddleBrown
    "#A52A2A",  # [66]Brown
    "#D2691E",  # [67]Chocolate
    "#F4A460",  # [68]SandyBrown
    "#DEB887",  # [69]BurlyWood
    "#BC8F8F",  # [70]RosyBrown
    "#A0522D",  # [71]Sienna
    "#CD853F",  # [72]Peru
)

