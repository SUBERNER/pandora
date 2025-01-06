import Buffle
import os

base = os.getcwd()
unchanged_base = base + "\\UNCHANGED\\bedrock-samples-1.21.50.7"
changed_base = base + "\\CHANGED"

changed_base = Buffle.copy(unchanged_base, changed_base)
changed_base = Buffle.redo_name(changed_base, "RANDOMIZER")