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
        print("\n\tYour files are sorted Successfully!")


if __name__ == "__main__":

    # this is a default set of common extensions. you can add whatever you want in there.
    extenstionSet = {
        ".docx": "Documents",
        ".xslx": "Documents",
        ".pdf": "Documents",
        ".csv": "Documents",
        ".xlsx": "Documents",
        ".zip": "Compressed",
        ".rar": "Compressed",
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

    while not os.path.exists(path):
        print('''\n\tThe path you entered doesn\'t exist. Make sure there aren\'t spelling errors
        and enter the correct path. ''')

        path = input('''\n\tPaste the path you want to organize 
        >>> ''')

    userSelection = {}
    userMenu = 0

    while userMenu == 0:
        userMenu = input('''
            In what way do you want to organize.
            
            1). Organize all files in the directory.
            2). Organize files of certain extensions in the directory.

            >>> ''')

        if userMenu == '1':
            userSelection = extenstionSet

        elif userMenu == '2':
            ext = input('''\n\tEnter the extensions you want to organize preceeded by a period and separated by space.
            For-example:- '.py .json .csv' 
            >>> ''')

            folderName = input('''\n\tEnter a folder name of your choice for the selected extensions 
            >>> ''')

            for i in ext.split():
                userSelection[i] = folderName
        else:
            print(f'''\n\tYou have entered an invalid input of {userMenu}.
        Please enter a valid input from the options provided. \n''')
            userMenu = 0

    Organizer(path, userSelection)
