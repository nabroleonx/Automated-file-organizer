import os
import shutil
from sys import platform
import threading

organise_folder = download_path = None

category = {"Audios": [".aif", ".cda", ".mid.mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl", ".midi"],
            "Compressed": [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar", ".z", ".zip", ".gz"],
            "Documents": [".bin", ".dmg", ".iso", ".toast", ".vcd", ".csv", ".dat", ".db", ".log", ".mdb", ".sav",
                          ".sql", ".tar", ".xml", ".dbf", ".email", ".eml", ".emlx", ".msg", ".oft", ".ost", ".pst",
                          ".vcf", ".asp", ".cer", ".cfm", ".cgi", ".css", ".htm", ".js", ".jsp", ".part", ".php", ".py",
                          ".rss", ".xhtml", ".fnt", ".fon", ".otf", ".ttf", ".doc", ".odt", ".pdf", ".rtf", ".tex",
                          ".txt", ".wpd", ".key", ".odp", ".pps", ".ppt", ".pptx", ".c", ".cgi", ".class", ".cpp",
                          ".cs", ".h", ".java", ".php", ".py", ".sh", ".swift", ".vb", ".ods", ".xls", ".xlsm", ".xlsx",
                          ".docx", ".aspx", ".html"],
            "Images": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".png", ".ps", ".psd", ".svg", ".tif", ".jpg", ".tiff"],
            "Videos": [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg.rm", ".swf",
                       ".vob", ".wmv", ".mpeg", ".webm"],
            "Setups": [".apk", ".bat", ".bin", ".cgi", ".com", ".exe", ".gadget", ".jar", ".msi", ".py", ".wsf"],
            "Systemfiles": [".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ico", ".ini",
                            ".lnk", ".msi",
                            ".sys", ".tmp"]}


def movers(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    try:
        shutil.move(source, destination)
    except OSError as error:
        print(str(source) + " <= File is open. Error => ", error)


def org_by_cat(path, file):
    file_path = os.path.join(path, file)
    if os.path.isdir(file_path):
        pass
    else:
        file_name, file_extension = os.path.splitext(file_path)
        for cat in category:
            cat_folder = os.path.join(path, cat)
            if file_extension in category[cat]:
                movers(file_path, cat_folder)


def org_by_ext(path, chosen_ext, destination, file):
    if os.path.isdir(file):
        pass
    else:
        file_path = os.path.join(path, file)
        file_name, file_extension = os.path.splitext(file_path)
        if destination == '':
            destination = os.path.join(path, file_extension+" files")
        if chosen_ext != []:
            if file_extension in chosen_ext:
                ext_folder = os.path.join(path, destination)
                movers(file_path, ext_folder)
        if chosen_ext == []:
            ext_folder = os.path.join(path, destination)
            for cat in category:
                if file_extension in category[cat]:
                    movers(file_path, ext_folder)


def main():
    global organise_folder, download_path
    if platform == "linux" or platform == "linux2":
        download_path = "/home/" + os.environ.get('USERNAME') + "/Downloads"
    elif platform == "win32":
        download_path = "C:\\Users\\" + \
            os.environ.get('USERNAME') + "\\Downloads"
    while True:
        print("Press Q to exit anytime.")
        path = input('''\tOrganise Custom Directory? Enter Path (default : Downloads)\n>>> ''')
        if path == "q":
            break
        elif path == "":
            organise_folder = download_path
        else:
            organise_folder = path
        if not os.path.exists(organise_folder):
            print("\nInvalid Path.")
            continue
        else:
            if os.path.isdir(organise_folder):
                break
            else:
                print("\nEntered Path not a directory.")
                continue
    while True:
        organise_type = input("\nIn what way do you want to organize.\n\t"
                              + "1) Organize files by category.\n\t"
                              + "2) Organize files by extension.\n>>> ")
        if organise_type == "q":
            break

        elif organise_type == "1":
            for file in os.listdir(organise_folder):
                threading.Thread(target=org_by_cat, args=[organise_folder, file]).start()
            print("Done")
            break

        elif organise_type == "2":
            chosen_ext = input('''\n\tEnter the extensions you want to organize preceeded by a period and separated by space.\n
            For-example:- '.py .json .csv' --- or --- hit enter to sort all files with the same extension\n>>> ''').split()

            destination = input('''\n\tWhat do you want to name the folder\n>>> ''')

            for file in os.listdir(organise_folder):
                threading.Thread(target=org_by_ext, args=[organise_folder, chosen_ext, destination, file]).start()
            print("Done")
            break


if __name__ == "__main__":
    main()
