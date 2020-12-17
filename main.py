import os

#    _____           _                   _            _____        __                           _   _                  
#   |  __ \         | |                 | |          |_   _|      / _|                         | | (_)                 
#   | |__) |___  ___| |__   ___ _ __ ___| |__   ___    | |  _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  __ _ _   _  ___ 
#   |  _  // _ \/ __| '_ \ / _ | '__/ __| '_ \ / _ \   | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _` | | | |/ _ \
#   | | \ |  __| (__| | | |  __| | | (__| | | |  __/  _| |_| | | | || (_) | |  | | | | | | (_| | |_| | (_| | |_| |  __/
#   |_|  \_\___|\___|_| |_|\___|_|  \___|_| |_|\___| |_____|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\__, |\__,_|\___|
#                                                                                                        | |           
#   


def pas_i_os_in():
    print("\n\t\t\t\tRECHERCHE INFORMATIQUE (Dossier, extension exct...)\n")
  

show_pas_i_os_in = True
if show_pas_i_os_in == True:
    pas_i_os_in()

looking_patch = "C://"
files_patch = input("Entrez ce que vous voulez rechercher: ")

for root, dirs, files in os.walk(looking_patch):
    for file in files:
        if file == files_patch:
            print(root,'\\', str(file))
            break
