import os
import shutil
import time

seconds = time.time()
print(seconds)
path = input("Write down the pathe of the folder")
days = input("Write down the amount of days after the files are deleted")

if os.path.exists(path):
    print("path exists")
    for root_folder, folders, files in os.walk(path):
       for file in files:
           filepath = os.path.join(path, file)
           print(filepath)
           ctime = os.stat(filepath).st_ctime
           if (seconds - ctime > (days * 24*60*60)):
               print("Time is greater then the days")
               os.remove(filepath)
           else:
               print("Time not greater")



    for folder in folders:
           folderpath = os.path.join(path, folder)
           print(folderpath)
           ctimef = os.stat(folderpath).st_ctime
           if (seconds - ctimef > (days * 24*60*60)):
               print("Time is greater then the days")
               shutil.rmtree(folderpath)
           else:
               print("Time not greater")    




else:
    print("Path does not exist.")
