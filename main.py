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
def updateReadme(line):
    f = open("README.md", "a")
    write = "|" + line + "|" + "n" + "|" + "\n"
    f.write(write)
    f.close()

# Add the prototype to both README and  
def updatePrototype(prototype, name):
    # Change the readme
    README = open("README.md", "a")
    README.write(prototype)
    README.close()
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
NameList = []
for line in Lines:
    # suppress every unwanted character
    for char in Suppr:
        line = line.replace(char, "")    
    # search for file name
    if Search[0] in line:
        line = line.replace(Search[0], "")
        linePath = sys.argv[1] + '/' + line
        NameList.append(linePath)

for line in Lines:
    # suppress every unwanted character
    for char in Suppr:
        line = line.replace(char, "")
    # search for prototype list
    if Search[1] in line:
        line = line.replace(Search[1], "")
        line = line.replace("def", "def ")
        PrototypeList.append(line)
        #updatePrototype(line)##################

for i in range(len(NameList)):
    createandwrite(NameList[i])
    updateReadme(NameList[i])
    if i < len(PrototypeList):
        updatePrototype(PrototypeList[i], NameList[i])