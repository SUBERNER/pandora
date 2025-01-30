import os


class Color:
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


class Result:
    # formats for how the file location is displayed
    # 0 = full: full file directory
    # 1 = limited: 2 directories deep
    # 2 = file: only file
    _file_format = None
    # enabled or disabled displaying relevant information
    _display_results = None
    # the minimum amount of space given to the source file section of a result
    _source_length = 0
    # the color used in method section to identify what method is being used
    _method_color = None
    # stops the script while running if an error_result is displayed
    _error_quit = True
    # the amounts of edits (FOR FUN)
    _count = 0

    def __init__(self, file_format: int, display_results: bool, method_color: str = f"\033[38;2;{255};{255};{255}m"):
        """
        Initializes the display settings for method outputs.

        Parameter:
            file_format (int): Determines the format used when displaying file paths.
                - 0: Full path
                - 1: Limited path (last 3 directory components)
                - 2: File name only

            display_results (bool): Enables or disables displaying results.

            method_color (str): Hex color code or ANSI escape sequence for method labels. Defaults to white.
        """
        try:
            self._file_format = file_format
            self._display_results = display_results
            self._method_color = self.set_color(method_color)
        except Exception as e:
            self.error_result(f"None", "display", str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def get_count(self):
        """
        Displays total edits displayed by results.
        """
        try:
            self._source_length = 0
            self.result(f"None", "edits", self._count, 0)
        except Exception as e:
            self.error_result(f"None", "display", str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def set_format(self, format: int = None):
        """
        Updates or retrieves the format used for displaying file paths.

        Parameter:
            format (int, optional): The desired file format for display.
                - 0: Full path
                - 1: Limited path (last 3 directory components)
                - 2: File name only

        Return:
            int: The current or updated file format.
        """
        try:
            if format is not None:
                self._file_format = format
            return self._file_format
        except Exception as e:
            self.error_result(f"None", "display", str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def set_color(self, hex_color: str = None):
        """
        Updates or retrieves the ANSI escape sequence for method labels.

        Parameter:
            hex_color (str, optional): Hexadecimal color code (e.g., "#FF0000" for red).
                - If None, retains the current color setting.

        Return:
            str: The ANSI escape sequence representing the current or updated color.
        """
        try:
            if hex_color is not None:
                hex_color = hex_color.lstrip("#")
                r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
                self._method_color = f"\033[38;2;{r};{g};{b}m"
            return self._method_color
        except Exception as e:
            self.error_result(f"None", "display", str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def set_length(self, file: str):
        """
        Adjusts the minimum width for displaying file paths to improve readability.

        Parameter:
            file (str): A sample file path (preferably the longest) to determine display length.

        Return:
            int: The calculated or updated length for file path display.
        """
        try:
            if self._file_format == 1:  # limited
                limited_parts = file.split(os.sep)[-3:]
                self._source_length = len(os.path.join(*limited_parts))
            elif self._file_format == 2:  # file
                self._source_length = len(file.split("\\")[-1])
            else:  # full
                self._source_length = len(file)
            return self._source_length
        except Exception as e:
            self.error_result(f"None", "display", str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def set_error(self, quiting: bool = None):
        """
        Updates or retrieves the behavior for handling errors.

        Parameter:
            quiting (bool, optional): Whether to quit the program on encountering an error.
                - True: Quit on error.
                - False: Continue execution.

        Return:
            bool: The current or updated error handling behavior.
        """
        try:
            if quiting is not None:
                self._error_quit = quiting
            return self._error_quit
        except Exception as e:
            self.error_result(f"None", "display", str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def set_display(self, display: bool = None):
        """
        Updates or retrieves the display setting for method results.

        Parameter:
            display (bool, optional): Whether to display method results.
                - True: Enable result display.
                - False: Disable result display.

        Return:
            bool: The current or updated display setting.
        """
        try:
            if display is not None:
                self._display_results = display
            return self._display_results
        except Exception as e:
            self.error_result(f"None", "display", str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def result(self, source: str, method: str, updated_value, original_value):
        """
        Displays the output of a method that alters files or folders.

        Parameter:
            source (str): The target file or folder's directory or location.

            method (str): The name of the method or action performed.

            updated_value: The value of the file or folder after the alteration.

            original_value: The value of the file or folder before the alteration.
        """
        try:
            if self._file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif self._file_format == 2:  # file
                source = source.split("\\")[-1]

            if original_value != updated_value:
                print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|>   altered <|> [{Color.RED}{original_value}{Color.RESET}] --> [{Color.GREEN}{updated_value}{Color.RESET}]")
                self._count += 1 # updated total edits
            else:
                print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|> unaltered <|> [{Color.YELLOW}{updated_value}{Color.RESET}]")
        except Exception as e:
            self.error_result(f"{source:>{self._source_length}}", method, str(e.args))
            if self._error_quit:
                quit()  # ends running code

    def error_result(self, source: str, method: str, error: str):
        """
        Displays an error message for a method that failed.

        Parameter:
            source (str): The target file or folder's directory or location.

            method (str): The name of the method or action performed.

            error (str): Description of the error encountered.
        """
        try:
            if self._file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif self._file_format == 2:  # file
                source = source.split("\\")[-1]
            print(f"{Color.RED_BACKGROUND}{source:>{self._source_length}} <|> {method} <|>     ERROR <|> {error}{Color.RESET}")
            if self._error_quit:
                quit()  # ends running code

        except Exception as e:
            print(f"{Color.RED_BACKGROUND}{source:>{self._source_length}} <|> {method}<|>     ERROR <|> {e.args}{Color.RESET}")
            if self._error_quit:
                quit()  # ends running code

    def warning_result(self, source: str, method: str, warning: str):
        """
        Displays a warning message for a method that encountered a non-critical issue.

        Parameter:
            source (str): The target file or folder's directory or location.

            method (str): The name of the method or action performed.

            warning (str): Description of the warning encountered.
        """
        try:
            if self._file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif self._file_format == 2:  # file
                source = source.split("\\")[-1]
            print(f"{Color.YELLOW_BACKGROUND}{source:>{self._source_length}} <|> {method} <|>   WARNING <|> {warning}{Color.RESET}")

        except Exception as e:
            print(f"{Color.RED_BACKGROUND}{source:>{self._source_length}} <|> {method}<|>   WARNING <|> {e.args}{Color.RESET}")
            if self._error_quit:
                quit()  # ends running code

        # the delay after an error until processes can run again


# Used to display results from methods
outer = Result(1, True, Color.METHODS[14])
inner = Result(1, True, Color.METHODS[18])
image = Result(1, True, Color.METHODS[1])
methods = Result(1, True, Color.METHODS[12])
search = Result(1, True, Color.METHODS[8])
audio = Result(1, True, Color.METHODS[38])
