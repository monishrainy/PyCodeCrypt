# Author - MOHD MONISH RAINY

from tkinter import *
import base64

root = Tk ()

root.geometry('500x300')
root.resizable(0,0)
root.title("PyCodeCrypt - Message Encode and Decode")
root['bg'] = 'green'



Label(root, text ='CodeCrypt', font = 'Harrington 30 bold', background= 'green').pack()
Label(root, text ='Enocde & Decode', font = 'Harrington 30 bold', background= 'green').pack(side = BOTTOM)



Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()



def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)



def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


def Exit():
    root.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")



Label(root, font= 'Harington 15 bold', text='MESSAGE', background = 'green').place(x= 60,y=60)
Entry(root, font = 'Harington 10 italic bold', textvariable = Text, bg = 'white', fg = 'blue').place(x=290, y = 60)
Label(root, font = 'Harington 15 bold', text ='KEY',  background = 'green').place(x=60, y = 90)
Entry(root, font = 'Harington 10 italic bold', textvariable = private_key , bg ='white', fg = 'blue').place(x=290, y = 90)
Label(root, font = 'Harington 15 bold', text ='MODE(e-encode, d-decode)',  background = 'green').place(x=60, y = 120)
Entry(root, font = 'Harington 10 italic bold', textvariable = mode , bg= 'white', fg = 'blue').place(x=290, y = 120)
Entry(root, font = 'Harington 10 bold italic bold', textvariable = Result, bg ='white', fg = 'blue').place(x=290, y = 150)
Label(root, font = 'Harington 15 bold', text = 'RESULT', bg ='green',  background = 'green').place(x=60, y = 150)
Button(root, font = 'Harington 10 bold' ,text ='RESET' ,width =10, command = Reset,bg = 'green', padx=2, pady = 6,  background = 'green').place(x=60, y = 210)
Button(root, font = 'Harington 10 bold',text= 'EXIT' , width = 10, command = Exit,bg = 'green', padx=2, pady=6,  background = 'green').place(x=290, y = 210)
root.mainloop()




