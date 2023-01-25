import sys

print(sys.argv[1])

fileIn = open("/root/Holberton-Python-Filename/SourceCod", "r")
Lines = fileIn.readlines()
Suppr = ["<li>","\n","<code>", "</li>"," ","</code>"]
Search = ["File:", "Prototype:"]

# Create the core of the README
def createReadme():
    f = open("README.md", "a")
    f.write("A brief description of what this project does and who it's for \n \n| FILE  | PROTOTYPE | \n | ------------- | ------------- |\n")
    f.close()

# Update the README to create a 
def updateReadme(prototype, line):
    f = open("README.md", "a")
    write = "|" + line + "|" + prototype + "|" + "\n"
    f.write(write)
    f.close()

# Add the prototype to both README and  
def updatePrototype(prototype, name):
    # Add prototype in the file
    filea = open(name, "a")
    filea.write(prototype)
    filea.close()
    
    
    
    
# Write in new files created
def createandwrite(name):
    f = open(name, "x")
    f.write("#!/usr/bin/python3\n")
    f.close()


# Main function
createReadme()
PrototypeList = []
NameListFull = []
NameList = []
for line in Lines:
    # suppress every unwanted character
    for char in Suppr:
        line = line.replace(char, "")    
    # search for file name
    if Search[0] in line:
        line = line.replace(Search[0], "")
        NameList.append(line)
        linePath = sys.argv[1] + '/' + line
        NameListFull.append(linePath)

for line in Lines:
    # suppress every unwanted character
    for char in Suppr:
        line = line.replace(char, "")
    # search for prototype list
    if Search[1] in line:
        line = line.replace(Search[1], "")
        line = line.replace("def", "def ")
        PrototypeList.append(line)

for i in range(len(NameListFull)):
    createandwrite(NameListFull[i])
    if i < len(PrototypeList):
        updatePrototype(PrototypeList[i], NameListFull[i])
        updateReadme(PrototypeList[i], NameList[i])