from .logger import Logger
from .file_writer import FileWriter
from .safe_division import SafeDivision
from pathlib import Path

ASSETS = Path(__file__).parent.parent / 'assets'

with Logger():
    print("something...")

# Wyjątek nie jest tłumiony - zatrzymanie programu
with FileWriter(ASSETS / 'text-ex-2.txt') as f:
    f.write("Some test text")
    raise ValueError("Testowy wyjątek w trakcie zapisu!")

print("Program działa dalej")


with SafeDivision() as sd:
    print(sd.divide(10, 2))
    print(sd.divide(5, 0))

print("Program działa dalej")