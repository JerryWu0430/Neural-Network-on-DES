import csv

d = open("dict.txt","r")
data = d.readlines()

for lines in (data):
    if len(lines.rstrip()) == 8:
        d.write(f"{lines}") 