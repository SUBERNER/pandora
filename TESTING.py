import random
import Buffle
import os

base = os.getcwd()
zipped_path = base + "\\bedrock-samples-1.21.50.7.zip"

Buffle.Display.methods.set_delay(1)

unzipped_path = Buffle.unzip(zipped_path)
Buffle.delete(zipped_path)

TEST_path = Buffle.move(unzipped_path, base + "\\TEST")

zipped_path = Buffle.zip(TEST_path, ".zip")
zipped_path = Buffle.rename(zipped_path, "RANDOMIZED.mcpack")
#Buffle.delete(TEST_path)

Buffle.dump(zipped_path)






