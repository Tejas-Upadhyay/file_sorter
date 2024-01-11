import os
import glob
import shutil

user = input("Do you want to move, delete, or copy? ")

if user == "copy":
    source = input("What is the name of the file(s) that you want to move? ")
    destination = input("Where do you want to store this? ")

    dest = shutil.copy(source, destination, copy_function = shutil.copytree)
elif user == "move":
    print("What is the name of the file(s) that you want to move?")
    source = input()
    print("Where do you want to store this?")
    destination = input()

    dest = shutil.move(source, destination, copy_function = shutil.copytree)
elif user == "delete":
    wasd = bool = False
    while wasd == False:
        print("Do you want to delete a folder or a folder or a file")
        typeDelete = input()
        wasd = bool = typeDelete == "folder" or typeDelete == "file"
    if typeDelete == "file":
        print("What do you want to delete?")
        os.remove(input())
    elif typeDelete == "folder":
        os.removedirs(input())
elif user == "Organizer":
    extensions = {
    "jpg": "images", "png": "images", "ico": "images", "gif": "images", "svg": "images", # images
    "sql": "sql", "sqlite3": "sql", # SQL
    "exe": "programs", "msi": "programs", "dmg" : "Programs", # Programs
    "pdf": "pdf", #pdf
    "rar": "archive", "zip": "archive", "gz": "archive", "tar": "archive", # Archive
    "txt": "text",
    "torrent": "torrent", "torr" : "torrent", # torrent 
    "ipynb": "python", "py": "python", # python
    "xlsx": "excel", "csv": "excel", # excel
    "pptx": "powerpoint", "ppt": "powerpoint", # powerpoint
    "doc": "word", "dox":"word", #word
    "mp3": "audio", "wav": "audio", # audio
    "mp4": "video", "m3u8": "video", "webm": "video", "ts": "video", "mkv" : "video", "m4a" : "video", # Video
    "json": "json", # json
    "css": "web", "js": "web", "html": "web", # web
    "apk": "apk", # apk
    "blend" : "3d_Model", "obj" : "3d_Model", "glb" : "3d_Model", # 3D model
    "sb3" : "scratch", # scratch
    "ova" : "VM", # VM
    "jar" : "java", # java
    "pub" : "SSH_key", "key" : "SSH_key", # SSH_key
    }
    dir = input("Put the name of the dir you want to orginize: ")
    path = dir
        # setting verbose to 1 (or True) will show all file moves
        # setting verbose to 0 (or False) will show basic necessary info
    verbose = 0
    for extension, folder_name in extensions.items():
        # get all the files matching the extension
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        print(f"[*] Found {len(files)} files with {extension} extension")
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            # create the folder if it does not exist before
            print(f"[+] Making {folder_name} folder")
            os.mkdir(os.path.join(path, folder_name))
        for file in files:
            # for each file in that extension, move it to the correponding folder
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
            if verbose:
                print(f"[*] Moving {file} to {dst}")
            shutil.move(file, dst)

else:
    print("Try having all the word in lower case")