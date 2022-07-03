def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile("ps_1_01.txt")
readFile("ps_1_02.txt")
readFile("ps_1_03.txt")