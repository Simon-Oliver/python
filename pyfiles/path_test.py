from pathlib import Path

path = Path()

allPy = path.glob('*.py')

for file in allPy:
    print(file)
