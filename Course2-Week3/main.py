# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
data = fh.read()
print(data.strip().upper())