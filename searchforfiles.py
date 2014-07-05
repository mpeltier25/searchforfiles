#This program will pick a root directory and search through all subfolders until it finds the file that the user is looking for.
import os
def searchforfiles():
    #Prompt the user for the root directory they wish to search
    directory=input("Enter the directory you wish to search ex. /home/name/Desktop/test folder\n")
    #Prompt the user to enter in the file that they are looking for (including the extension, be careful when using picture files, that jpg and jpeg are different extensions when using this program)
    nameoffile=input("Please enter in the name of the file you are looking for ex hello.txt:\n")
    for currentdir, alldirs, allfiles in os.walk(directory):
        #For the filename in the allfiles in the directory, it will search all the files and subfolders which are files for the name of the file you are looking for.
        for filename in allfiles:
        #If the file was found, it will print the name of the file as well as the filename and the directory it was located in.
            if filename==nameoffile:
               print ("The file", filename, "was found here:\n", (os.path.join(currentdir,filename)))
            else:
                #Else, it will print the directory it searched and will report that the file was not located.
                for subcurrentdir in alldirs:
                    print("The file you were looking for was not found in this directory:", (os.path.join(currentdir, subcurrentdir)))
searchforfiles()
