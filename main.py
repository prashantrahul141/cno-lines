a = '''
    This was created by chief141(chief141.github.io).
    This file's repo link : https://github.com/chief141/count_no_of_lines
    Do whatever you want to do with this, I dont give a F, just remember
    I dont take any reponsibility(s) of this piece of code.

'''
b = '''
    How to use?
    just enter the location of the folder, it will search through
    all the subfolders and files.
    example of a location - C:/Users/chief/Desktop/python/Web_Application
'''

print(a)
print(b)


import os

# Taking path as input
while True:
    path = input("Enter Location of folder : ")
    if os.path.isdir(path):
        print()
        break;
    print()
    print(" Enter a valid location.")
    print()


try:
    #Extensions of file which is not to be read
    with open(' Not_to_read_extensions.txt','r') as f:
        data = f.read().split(',')
        not_to_read_extensions = [str(i) for i in data]
        print();print(" Total no. of file extensions NOT to read : {}".format(len(not_to_read_extensions)));print()
except:
    print(' not_to_read_extensions.txt file didnt find')
    print(' please keep the not_to_read_extensions.txt file in the same directory as this file is.')

#Folder to ignore
ignore_folder = ["desktop.ini", ".git"]


r = 0  #Total number of lines
d = 0  #Total number of subfolder
f = 0  #Total number of files
fr = 0  #Total number of files read
extns_to_add = []   #A list which will save extension which cant be read

#Function to add number of lines from a file to r varible
def count_lines(file):
    global r, fr
    name = file.split("/")[-1] #name of file
    try:
        extension = name.split('.')[-1].lower()                 #extension of file
        if not extension in not_to_read_extensions:         #checking if extention is in 'not_to_read_extensions'
            len_of_extn = len([i for i in extension])       #length of extension

            if not len_of_extn:
                len_of_extn = ''

            if len_of_extn <= 16 and len_of_extn > 0 :          #dont read if len of extension is less than 1 or more than 15
                try:
                    with open(file, 'r',  encoding="utf8") as f:
                        data = f.read()                              #reading file
                except:
                    with open(file, 'r') as f:
                        data = f.read()

                lines = len(data.split("\n"))                    #counting lines
                r += lines                                          #adding lines to r variable
                fr += 1
                fake_lines = str(lines)
                fake_lines = [i for i in fake_lines]
                len_of_fake_lines = len(fake_lines)
                if len_of_fake_lines == 1: spaces = "    "
                elif len_of_fake_lines == 2: spaces = "   "
                elif len_of_fake_lines == 3: spaces = "  "
                else: spaces = " "
                print(" Read   {}{}lines in   {}".format(lines,spaces, name))


    except Exception as e:
        if not extension in extns_to_add and not extension in not_to_read_extensions:
            not_to_read_extensions.append(extension)
            extns_to_add.append(extension)
        print(e)
        print(" Failed to read {}".format(name))
        print()


#A recursive function to go inside each folder
def flow(path):
    global d,f
    try:
        smol_items = os.listdir(path)
        for i in smol_items:
            actual_path = path + '/' + i
            if not i in ignore_folder:
                if os.path.isdir(actual_path):
                    d += 1
                    flow(actual_path)
                else:
                    f += 1
                    count_lines(actual_path)
    except Exception as e:
        print(e)

#main function
def main(path):
    global r, f, fr, d
    flow(path)
    print()
    print(' Done..................')
    print(' Total no of lines         : {}'.format(r))
    print(' Total no of files present : {}'.format(f))
    print(' Total no of files read    : {}'.format(fr))
    print(' Total no of subfolders    : {}'.format(d))
    print()

'''
l = os.listdir(path)
for i in l[1:]:
    main(path + '/' + i)
'''
main(path) #running main

if len(extns_to_add) > 0 :
    print(' Writing.... not_to_read_extensions file')
    with open(' Not_to_read_extensions.txt' ,'a') as f:
        for i in extns_to_add:
            f.write(',' + str(i))
print(" Finished...................")