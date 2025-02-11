import Massma
import os

result_test = Massma.Display.Result()
try:
    print(F"TESTING, HELLO THERE!")
    for color in Massma.Display.Color.GROUPS:
        print(f"{color}TESTING, HELLO THERE!{Massma.Display.Color.RESET}")

    result_test.set_source_length("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd())

    print(f"{Massma.Display.Color.NOTIFY}TESTING, THIS IS A NOTIFICATION!{Massma.Display.Color.RESET}")
    print(f"{Massma.Display.Color.ERROR}TESTING, THIS IS A ERROR!{Massma.Display.Color.RESET}")
    print(f"{Massma.Display.Color.WARNING}TESTING, THIS IS A WARNING!{Massma.Display.Color.RESET}")

    result_test.result("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NORMAL", 0, 1)
    result_test.result("CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NORMAL", 20, 0)
    result_test.result("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NORMAL", 5, 5)
    result_test.result_warning("CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "WARN", "this is a warning\nMORE WARNINGS")
    result_test.result_notify("CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "NOTI", "have a good day")
    print("YES DONE")

except Exception as e:
    result_test.result_error(f"None", "display", e)
    print("NO DONE")