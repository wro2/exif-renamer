
import os 
import shutil
from exif import Image
from datetime import datetime


#TODO: Figure out subdirectories. Throws an error when processing subdirectory (in with-open)
#TODO: Retain file extension.
#TODO: Figure out .gif files.
#TODO: Add Logging
#TODO: Sort by Year
#TODO: Genreal cleanup and creation of functions.


def getListOfFiles(dirName):
  #Create a list of files and subdirectories in the given path.
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

  
file_list = getListOfFiles("./testdata/")
for file in file_list:    
    with open(file,"rb") as image_file:
        current_image = Image(image_file)   

    date_taken = "1977:01:01 00:00:01"
    if current_image.has_exif:       
        exif_tags = dir(current_image)
        for tag in exif_tags:
            if tag == "datetime_original":
                date_taken = current_image["datetime_original"]           

    date_time_obj = datetime.strptime(date_taken, '%Y:%m:%d %H:%M:%S') 

   
    full_dest_path = "./processed/" + + date_time_obj.strftime("%Y-%m-%d_%H%M%S") + ".jpg"
    shutil.copy(file,full_dest_path)
  

        

   
    
    






#TODO: Figure out subdirectories. Throws an error when processing subdirectory for GetLIstofFiles
#TODO: Retain file extension.
#TODO: Figure out .gif files.
#TODO: Add Logging
#TODO: Add folder by Year

def getListOfFiles(dirName):
  #Create a list of files and subdirectories in the given path.
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

  
file_list = getListOfFiles("./testdata/")
for file in file_list:    
    with open(file,"rb") as image_file:
        current_image = Image(image_file)   

    date_taken = "1977:01:01 00:00:01"
    if current_image.has_exif:       
        exif_tags = dir(current_image)
        for tag in exif_tags:
            if tag == "datetime_original":
                date_taken = current_image["datetime_original"]           

    date_time_obj = datetime.strptime(date_taken, '%Y:%m:%d %H:%M:%S') 

   
    full_dest_path = "./processed/" +  date_time_obj.strftime("%Y-%m-%d_%H%M%S") + ".jpg"
    shutil.copy(file,full_dest_path)
  

        

   
    
    



