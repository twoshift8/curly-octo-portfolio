
def main():
    ext = input("File name: ").strip().lower()
    ending = ext[ext.rfind(".")+1:] if "." in ext else ""
    if ext.endswith(('.gif', '.png', '.jpg', '.jpeg')):
        return print(f"image/{ending}")
    if ext.endswith(('.jpeg')):
        return print(f"image/.jpg")
    elif ext.endswith('.pdf'):
        return print(f"application/.pdf")
    elif ext.endswith('.txt'):
        return print(f"text/plain")
    elif ext.endswith(('.zip')):
        return print(f"application/.zip")
    else:
        return print("File Name: application/octet-stream")



'''
using library/dictionary
def main():
    ext = input("File name: ").strip().lower()
    ending = ext[ext.rfind(".")+1:] if "." in ext else ""
    types = {"gif": "image/gif",
         "png": "image/png",
         "jpeg": "image/jpeg",
         "jpg": "image/jpeg",
         "pdf": "application/pdf",
         "htm": "text/html",
         "html": "text/html",
         "txt": "text/plain",
         "md": "text/markdown",
         "css": "text/css",
         "csv": "text/csv",
         "doc": "application/msword",
         "epub": "application/epub+zip",
         "zip": "application/zip",
         "mp3": "audio/mpeg",
         "mp4": "video/mpeg"

             }
    print(types.get(ending,"application/octet-stream"))
'''


main()

#submit50 cs50/problems/2022/python/extensions
