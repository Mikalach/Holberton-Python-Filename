fileIn = open("SourceCod", "r")
Lines = fileIn.readlines()
Suppr = ["<li>","\n","<code>", "</li>"," ","</code>"]
Search = "File:"

def createandwrite(name):
    f = open(name, "x")
    f.write("#!/usr/bin/python3")
    f.close()

for line in Lines:
    for char in Suppr:
        line = line.replace(char, "")
    if Search in line:
        line = line.replace(Search, "")
        createandwrite(line)