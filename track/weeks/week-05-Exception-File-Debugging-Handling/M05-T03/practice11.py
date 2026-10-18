# Append New Records Without Removing Existing Data

file = open("employees.txt", "a")

file.write("\n103,Kabir")
file.write("\n104,Riya")

file.close()