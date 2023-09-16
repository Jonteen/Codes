import os
import shutil

def sort_files():
    # Skapa en mapp för sorterade filer om den inte redan finns
    sorted_folder = 'Sorterat'
    if not os.path.exists(sorted_folder):
        os.makedirs(sorted_folder)
    
    # Flytta filerna till den sorterade mappen baserat på filtyp
    for file_name in os.listdir(os.getcwd()):
        if os.path.isfile(file_name):
            file_extension = file_name.split('.')[-1]
            destination_folder = os.path.join(os.getcwd(), sorted_folder, file_extension)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            source_path = os.path.join(os.getcwd(), file_name)
            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(source_path, destination_path)

sort_files()
