import os
import shutil


def Organizer(path, userSelection):

    if os.path.exists(path):
        for file in os.listdir(path):

            # we create the path of the file
            filePath = os.path.join(path, file)

            # check if it is a folder
            if os.path.isdir(filePath):
                pass

            # split the extension of the file from the root url
            filename, fileExtension = os.path.splitext(filePath)

            # check if the file extension exist in our dict of extentions
            if fileExtension in userSelection:

                # the directory we are gonna move the files to
                relocatingPath = os.path.join(
                    path, userSelection[fileExtension])

                # create a new folder if the folder doesnt exist
                if not os.path.exists(relocatingPath):
                    os.makedirs(relocatingPath)

                # exception handling incase the moving fails
                try:
                    shutil.move(filePath, relocatingPath)
                except OSError as error:
                    print('''Something unexpected happened! 
                        Error message:''', error)


if __name__ == "__main__":

    extenstionSet = {
        ".docx": "Documents",
        ".xslx": "Documents",
        ".pdf": "Documents",
        ".csv": "Documents",
        ".xlsx": "Documents",
        ".mp3": "Musics",
        ".m4a": "Musics",
        ".ogg": "Musics",
        ".wav": "Musics",
        ".jpg": "Pictures",
        ".png": "Pictures",
        ".gif": "Pictures",
        ".tif": "Pictures",
        ".mp4": "Videos",
        ".mkv": "Videos",
        ".3gp": "Videos",
        ".mpeg4": "Videos",
    }

    path = input('''\tPaste the path you want to organize 
        >>> ''')

    userSelection = {}
    userMenu = 0

    while userMenu == 0:
        userMenu = input('''
            In what way do you want to organize.
            
            1). Organize all files with same extension in the same folder.
            2). Organize files with specific extension in the same folder.
            3). Organize files of certain extensions in the same folder.
            >>> ''')

        if userMenu == '1':
            userSelection = extenstionSet

        elif userMenu == '2':
            ext = input(
                '''\n\tEnter the extension you want to organize preceeded by a period. For-example:- '.py' 
                >>> ''')

            folderName = input('''\n\tEnter a folder name for the chosen extension 
            >>> ''')

            userSelection[ext] = folderName

        elif userMenu == '3':
            ext = input('''\n\tEnter the extensions you want to organize preceeded by a period and separated by space.
            For-example:- '.py .json .csv' 
            >>> ''')

            folderName = input('''\n\tEnter a folder name for the chosen extensions 
            >>> ''')

            for i in ext.split():
                userSelection[i] = folderName
        else:
            print(f'''\n\tYou have entered an invalid input of {userMenu}.
        Please enter a valid input from the options provided. \n''')
            userMenu = 0

    Organizer(path, userSelection)
