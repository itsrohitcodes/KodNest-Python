# Work with Different File Modes

file = open("report.txt", "w")

print(file.mode)

file.close

file = open("report.txt", "a")

print (file.mode)

file.close

file = open("report.txt", "r")

print(file.mode)

file.close()