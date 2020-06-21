with open("file.txt",'r') as reader:
    content = reader.readlines()
    reversed(content)
with open("file.txt",'w') as writer:
    for line in reversed(content):
        writer.write(line)