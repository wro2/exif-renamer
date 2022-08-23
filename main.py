
import os 
import shutil
from exif import Image
from datetime import datetime
import random
import dateutil.parser


#TODO: Figure out subdirectories. Throws an error when processing subdirectory (in with-open)
#TODO: Add Logging
#TODO: Add Config Options
#TODO: Gen cleanup and creation of functions.

 #Create a list of files and subdirectories in the given path.
 
def get_file_list(dirName):
    allFiles = list()   
    for dir_, _, files in os.walk(dirName):
         for file_name in files:           
            rel_file = os.path.join(dir_, file_name)
            allFiles.append(rel_file)

    return allFiles
        


def move_to_error_directory(file):
    file_name_parts = os.path.splitext(file)    
    full_dest_path = "./error/" + os.path.basename(file)
    shutil.copy(file,full_dest_path)

#Extracts exif date-time from file
def get_exif_data(file):      
    with open(file,"rb") as image_file:
        current_image = Image(image_file)   

    #Set Default date if no exif data exists for date taken.
    date_taken = "1977:01:01 00:00:01"
    if current_image.has_exif:       
        exif_tags = dir(current_image)
        for tag in exif_tags:
            if tag == "datetime_original":
                date_taken = current_image["datetime_original"]           
        
    
    #TODO: Need to write more verbose code to handle custom date formats
    try:
            date_time_obj = dateutil.parser.parse(date_taken)
    except:
            date_time_obj = dateutil.parser.parse("1977:01:01 00:00:01")
    return date_time_obj  

def rename_and_move(file,date_taken):
    file_year = date_taken.strftime("%Y")   
    if not os.path.exists("./processed/"+file_year):        
         os.makedirs("./processed/"+file_year)  

    file_name_parts = os.path.splitext(file)
    full_dest_path = "./processed/" + file_year + "/" +  str(date_taken.strftime("%Y-%m-%d")) + "_" + str(random.randint(1,100000)) + file_name_parts[1]
    shutil.copy(file,full_dest_path)



#-------------------------  
#Main Execution
#-------------------------
file_list = get_file_list("./testdata/")
for file in file_list:
  #  print ("processing:  " + file)
    if file.endswith("gif") or file.endswith("psd") or file.endswith("xcf") :
        move_to_error_directory(file)
    else:
        date_taken = get_exif_data(file)
        rename_and_move(file,date_taken)
    


  
