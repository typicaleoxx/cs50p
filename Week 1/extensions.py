#accepts the name of file
#output the files media type if file's name ends with
#.gif .jpg .jpeg .png .pdf .txt .zip

def main():
    user=input("Enter the file name :")
    file=user.lower().strip()
    print(filetype(file))

def filetype(x):

        if x.endswith(".gif"):
            return ("image/gif")
        elif x.endswith(".jpg"):
            return("image/jpeg")
        elif x.endswith(".jpeg"):
            return("image/jpeg")
        elif x.endswith(".png"):
            return("image/png")
        elif x.endswith(".pdf"):
            return("application/pdf")
        elif x.endswith(".txt"):
            return("text/plain")
        elif x.endswith(".zip"):
            return("application/zip")
        else:
            return("application/octet-stream")
main()