# if file does not exist
try:
    with open("sample.txt", "rt") as f:
        print("Reading file content:")
        for i, line in enumerate(f, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

#if file exist

file = open("sample1.txt", "wt")
file.write("This is a sample text file.\n")
file.write("it contains multiple lines.\n")
file.close()
with open("sample1.txt", "rt") as file:
    print(file.read())

try:
    with open("sample1.txt", "rt") as z:
        print("Reading file content:")
        for y, line in enumerate(z, start=1):
            print(f"Line {y}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample1.txt' was not found.")