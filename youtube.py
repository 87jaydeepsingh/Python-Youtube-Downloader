from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter.ttk import Progressbar
import time
import threading
MAX=300
root=Tk()
F1=Frame(root)
F2=Frame(root)
La=Label(root)
ls=Label(root)
L1=Label(root,text="Downloader",pady=30,font="verdana").pack(side="top")
F1.pack()
L2=Label(F1,text="URL:")
E1=Entry(F1,width="70")
E2=Entry(F2,width="70")
def choose():
    file=filedialog.askdirectory()
    E2.insert(0,file)
photo=PhotoImage(file="file1.png")
F2.pack()
B1=Button(F2,width=30,height=30,command=choose,image=photo,bd="0",padx=-10,pady=-20)
Lbl=Label(root,text="\nNo File Downloading\n",font="verdana")
L2.pack(side="left")
E1.pack(side="right")
E2.pack(side="left")
B1.pack(side="right")
def down():
    global str1
    t1 = threading.Thread(target=download)
    t1.start()
def download():
    global str1
    try:
        global MAX
        Lbl['text']="\nDownloading......\n"
        progress_var=DoubleVar()
        progress=Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate',variable=progress_var, maximum=MAX).pack()
        for i in range(0,300,1):
            root.update_idletasks()
            progress_var.set(i)
        str1=YouTube(E1.get()).streams.first().download(E2.get())
        La=Label(root,font="arial",anchor=W)
        La['text']="\nStatus:\nFile Downloaded:"+str1+"\nSaved TO:"+E2.get()+"\n"
        La.pack(side="left")
        Lbl['text']="\n"+"File Downloaded and Saved Sucessfully"+"\n"
    except:
        Lbl['text']="\nError or no Internet Connection\n"
B2=Button(root,text="Download",command=down,width="30",height="2")
B2.pack(side="bottom")
Lbl.pack()
root.mainloop()

