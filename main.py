import sys

print(sys.argv[1])

fileIn = open("/root/Holberton-Python-Filename/SourceCod", "r")
Lines = fileIn.readlines()
Suppr = ["<li>","\n","<code>", "</li>"," ","</code>"]
Search = "File:"

# Create the core of the README
def createReadme():
    f = open("README.md", "a")
    f.write("A brief description of what this project does and who it's for \n \n| FILE  | PROTOTYPE | \n | ------------- | ------------- |")
    f.close()

# update the README to create a 
def updateReadme(line):
    f = open("README.md", "a")
    write = "|" + line + "|" + "a" + "|" + "\n"
    f.write(write)
    f.close()

    
# Write in new files created
def createandwrite(name):
    f = open(name, "x")
    f.write("#!/usr/bin/python3")
    f.close()


# Main function
createReadme()
for line in Lines:
    for char in Suppr:
        line = line.replace(char, "")
    if Search in line:
        line = line.replace(Search, "")
        linePath = sys.argv[1] + '/' + line
        createandwrite(linePath)
        updateReadme(line)
