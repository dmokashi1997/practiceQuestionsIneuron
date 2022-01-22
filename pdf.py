import tkinter as tkk
import os
from pprint import pprint
from PyPDF2 import PdfFileMerger, PdfFileReader


def pdfmereger(count,dirlist):
    # Call the PdfFileMerger
    mergedObject = PdfFileMerger()

    for i in dirlist:
        mergedObject.append(PdfFileReader(i),'rb')
    # Write all the files into a file which is named as shown below
    mergedObject.write("mergedfilesoutput.pdf")



def findls():
    try:
        name=dir_name.get()
        print("dir name is: "+name)
        dirlist = os.listdir(name)
        pprint(dirlist)
        os.chdir(name)
        count = 0
        for i in dirlist:
            if (i[len(i)-3:len(i)]=="pdf"):
                count+=1
        if count>1:
            pdfmereger(count,dirlist)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # create a GUI window
    gui = tkk.Tk()
    dir_name = tkk.StringVar()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Pdf Merger")

    # set the configuration of GUI window
    gui.geometry("270x150")

    dir_label = tkk.Label(gui, text='Enter Dir Name', font=('calibre', 10, 'bold'))
    dir_entry = tkk.Entry(gui, textvariable=dir_name, font=('calibre', 10, 'normal'))
    sub_btn = tkk.Button(gui, text='Submit', command=findls)

    dir_label.grid(row=0, column=0)
    dir_entry.grid(row=0, column=1)
    sub_btn.grid(row=2, column=1)

    gui.mainloop()
