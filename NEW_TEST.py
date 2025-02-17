import Massma
import os
import re

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

    Massma.Display.filter.set_source_length(25)
    Massma.Display.filter.set_source_compression(True)
    swapping = Massma.Filter.Swap([(os.getcwd() + "\\ONE.txt", os.getcwd() + "\\THREE.txt"), (os.getcwd() + "\\TWO.txt", os.getcwd() + "\\FOUR.txt")])
    swapping()
    ignoring = Massma.Filter.Ignore(["CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd(), "bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd()])
    ignoring("CHANGED\\bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd())
    ignoring("bedrock-samples-1.21.50.7\\CHANGED\\bedrock-samples-1.21.50.7\\" + os.getcwd())
    swapping()

    print("EXCLUDING")

    exclude = Massma.Filter.Exclude(os.getcwd() + "\\ONE.txt", ["TWO", "SIX"], test_files=[os.getcwd() + "\\TWO.txt", os.getcwd() + "\\SIX.txt"],
                                    logic_files=Massma.Logic.OR, logic_strings=Massma.Logic.OR)
    exclude(os.getcwd() + "\\ONE.txt")

    print("INPUT")

    inputting = Massma.Filter.Input(os.getcwd() + "\\ONE.txt", ["111", "222", "333", "111"], logic_inputs=Massma.Logic.XNOR)
    inputting(os.getcwd() + "\\ONE.txt", "111")

    print("ALTER")
    alter_path = os.getcwd() + "\\OTHERS - Copy"
    altering = Massma.Filter.Alter([alter_path + "\\camel.json", alter_path + "\\goat.json", alter_path + "\\sheep.json"]
                                   , [r'"is_spawnable": true', r'"is_summonable": false'], [(r'"entity_type": "minecraft:skeleton"', r'"entity_type": "minecraft:booba"'), (r'"weight": 80', r'"weight": 999')], logic_files=Massma.Logic.OR, logic_strings=Massma.Logic.OR,
                                   replace_files=alter_path + "\\spider.json")
    altering(alter_path + "\\goat.json")

    Massma.Search.full(os.getcwd() + "\\SEARCH", deep_search=True, chance_files=0.5)

except Exception as e:
    result_test.result_error(os.getcwd(), "TEST", str(e))
    print("NO DONE")