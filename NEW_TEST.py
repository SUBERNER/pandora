import Massma
import os

print(F"TESTING, HELLO THERE!")
for color in Massma.Display.Color.GROUPS:
    print(F"{color} TESTING, HELLO THERE!")

print(F"{Massma.Display.Color.RESET}{Massma.Display.Color.NOTIFY} TESTING, THIS IS A NOTIFICATION!")
print(F"{Massma.Display.Color.ERROR} TESTING, THIS IS A ERROR!")
print(F"{Massma.Display.Color.WARNING} TESTING, THIS IS A WARNING!")

result_test = Massma.Display.Result(method_color=Massma.Display.Color.GROUPS[2])

result_test.result(os.chdir(), "TESTING", 0, 1)