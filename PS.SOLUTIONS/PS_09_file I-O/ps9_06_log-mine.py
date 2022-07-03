content=True
line=1

with open("ps9_06_log-file.txt")as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)        
            print(f"python is present on line {line}")
        line += 1