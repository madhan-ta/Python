infile = open("D:\programming_projects\Intellij_projects\Inputfiles\mynames.txt","r")
tofind = input("enter the string to find in the file:")
times = 0
for cnt, line in enumerate(infile):

    if (line.find(tofind)) > -1:
        times = times + 1

print("number of times ",tofind, "found:", times)