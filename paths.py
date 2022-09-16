from pathlib import Path

path  = Path(".")
path2 = Path("mail")
# path2.mkdir()
# path2.rmdir()
print(path.exists())

for files in path.glob("*.py"):
    print(files)