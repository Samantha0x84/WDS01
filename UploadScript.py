import cgi
import os 
import win32com.client
from distutils.dir_util import copy_tree
from pathlib import Path
import shutil
import glob

# Create instance of FieldStorage
form = cgi.FieldStorage()
fileitems = form['filename[]']


#####################
# define checkboxes #
#####################
screen1, screen2, screen3, screen4 = form.getvalue('screen1'), form.getvalue('screen2'), form.getvalue('screen3'), form.getvalue('screen4')
screen5, screen6, screen7, screen8 = form.getvalue('screen5'), form.getvalue('screen6'), form.getvalue('screen7'), form.getvalue('screen8')
screen9, screen10, screen11, screen12 = form.getvalue('screen9'), form.getvalue('screen10'), form.getvalue('screen11'), form.getvalue('screen12')
screen13, screen14, screen15, screen16 = form.getvalue('screen13'), form.getvalue('screen14'), form.getvalue('screen15'), form.getvalue('screen16')
screen17, screen18, screen19, screen20 = form.getvalue('screen17'), form.getvalue('screen18'), form.getvalue('screen19'), form.getvalue('screen20')

#make list of files uploaded
try:
    for fileitem in fileitems:
        if fileitem.filename:
            currentdir = os.path.dirname(os.path.realpath(__file__))
            # strip the leading path from the file name 
            filename = os.path.basename(fileitem.filename) 
            open(filename, 'wb').write(fileitem.file.read())
    print ("HTTP/1.0 200 OK\n")
    print("""

    <html>
    <head>
    <meta charset="utf-8">
    <title>Digital Signage</title>
    <link rel="stylesheet" href="../metro-all.min.css">
    </head>
    
    <body style="margin:0px"> 

    <br><br><br>


        <div style="text-align:center">
        <h1> files uploaded</h1>
        </div>
    </body>
    """)

except:
    print ("HTTP/1.0 200 OK\n")
    print("Error: You must select at least two images.")



# move files out of the python directory into the upload directory, 
# we don't need to do this but I'd prefer not to run delete operations inside the python folder itself
def movetouploaddir():
    currentdir = os.path.dirname(os.path.realpath(__file__))
    targetdirectory = str(Path(currentdir)) + "\\uploads\\"
    path = currentdir
    filepath= targetdirectory
    #move files
    files = glob.iglob(os.path.join(path, "*.jpg"))
    for file in files:
        if os.path.isfile(file):
            shutil.move(file,targetdirectory)
    
# copy the files uploaded into the web folders              
def sendtoWWWdirs(screenNumber):
            currentdir = os.path.dirname(os.path.realpath(__file__))
            targetdirectory = str(Path(currentdir).parent) +"\\wwwroot\\screens\\"+screenNumber+"files\\"
            try:
                currentdir = os.path.dirname(os.path.realpath(__file__))
                path = currentdir+"\\uploads\\"
                filepath= targetdirectory + "img\\"
                copy_tree (path,filepath)
                
            except:
                print ("HTTP/1.0 200 OK\n")
                print("Error in UploadScript.py function: def sendtoWWWdirs")
                
# generate file list for javascript based slideshow player
def listfiles(screenNumber):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    wwwscreen_folder = str(Path(currentdir).parent) +"\\wwwroot\\screens\\"+screenNumber+"files\\"
    


    listfiles = os.listdir(wwwscreen_folder+"\\img")
    listfiles = ','.join(listfiles)
    imagelistfile= wwwscreen_folder+"\\filelist.txt"
    f = open (imagelistfile,"w")
    f.write (listfiles)
    f.close()

def cleanup_uploaded():
    currentdir = os.path.dirname(os.path.realpath(__file__))
    uploadedfiles = str(Path(currentdir)) + "\\uploads\\"
    #delete files
    for root, dirs, files in os.walk(uploadedfiles):
        for file in files:
           os.remove(os.path.join(root, file))

def cleanup_www_images(screenNumber):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    wwwimages = str(Path(currentdir).parent) +"\\wwwroot\\screens\\"+screenNumber+"files\\img\\"
    try:
        for root, dirs, files in os.walk(wwwimages):
            for file in files:
               os.remove(os.path.join(root, file))        

        
    except:
        print ("HTTP/1.0 200 OK\n")
        print("Error in UploadScript.py function: def cleanup_www_images")


movetouploaddir()

if screen1 == "true":
    cleanup_www_images("1")
    sendtoWWWdirs("1")
    listfiles("1")

if screen2 == "true":
    cleanup_www_images("2")
    sendtoWWWdirs("2")
    listfiles("2")

if screen3 == "true":
    cleanup_www_images("3")
    sendtoWWWdirs("3")
    listfiles("3")
if screen4 == "true":
    cleanup_www_images("4")
    sendtoWWWdirs("4")
    listfiles("4")
if screen5 == "true":
    cleanup_www_images("5")
    sendtoWWWdirs("5")
    listfiles("5")
if screen6 == "true":
    cleanup_www_images("6")
    sendtoWWWdirs("6")
    listfiles("6")
if screen7 == "true":
    cleanup_www_images("7")
    sendtoWWWdirs("7")
    listfiles("7")
if screen8 == "true":
    cleanup_www_images("8")
    sendtoWWWdirs("8")
    listfiles("8")
if screen9 == "true":
    cleanup_www_images("9")
    sendtoWWWdirs("9")
    listfiles("9")
if screen10 == "true":
    cleanup_www_images("10")
    sendtoWWWdirs("10")
    listfiles("10")
if screen11 == "true":
    cleanup_www_images("11")
    sendtoWWWdirs("11")
    listfiles("11")
if screen12 == "true":
    cleanup_www_images("12")
    sendtoWWWdirs("12")
    listfiles("12")
if screen13 == "true":
    cleanup_www_images("13")
    sendtoWWWdirs("13")
    listfiles("13")
if screen14 == "true":
    cleanup_www_images("14")
    sendtoWWWdirs("14")
    listfiles("14")
if screen15 == "true":
    cleanup_www_images("15")
    sendtoWWWdirs("15")
    listfiles("15")
if screen16 == "true":
    cleanup_www_images("16")
    sendtoWWWdirs("16")
    listfiles("16")
if screen17 == "true":
    cleanup_www_images("17")
    sendtoWWWdirs("17")
    listfiles("17")
if screen18 == "true":
    cleanup_www_images("18")
    sendtoWWWdirs("18")
    listfiles("18")
if screen19 == "true":
    cleanup_www_images("19")
    sendtoWWWdirs("19")
    listfiles("19")
if screen20 == "true":
    cleanup_www_images("20")
    sendtoWWWdirs("20")
    listfiles("20")



cleanup_uploaded()
