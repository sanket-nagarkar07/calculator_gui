from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")

    if text == "=":      #condition for pressing = button
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value=eval(screen.get())   
            except Exception as e:
                print(e)
                value="Error"   

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("655x900")
root.title("Calculator BY Sanket")    # Calculator title

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucide 40 bold")
screen.pack(fill=X , ipadx=8,pady=10,padx=10)

frame=Frame(root,bg="grey" )
#create 9 number button
button=Button(frame,text="9",padx=5, pady=5,font="lucida 35 bold")
button.pack(side=LEFT , padx=5,pady=5)
button.bind("<Button-1>",click)
#create 8 number button
button=Button(frame,text="8",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create 7 number button
button=Button(frame,text="7",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create C number button
button=Button(frame,text="C",padx=3,pady=10,font="licida 30 bold")
button.pack(side=LEFT,padx=4,pady=5)
button.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="grey" )
#create 9 number button
button=Button(frame,text="6",padx=4, pady=5,font="lucida 35 bold")
button.pack(side=LEFT , padx=5,pady=5)
button.bind("<Button-1>",click)
#create 5 number button
button=Button(frame,text="5",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create 4 number button
button=Button(frame,text="4",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create * multiplication button
button=Button(frame,text="*",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)


frame.pack()

frame=Frame(root,bg="grey", padx=1)
#create 3 number button
button=Button(frame,text="3",padx=5, pady=5,font="lucida 35 bold")
button.pack(side=LEFT , padx=5,pady=5)
button.bind("<Button-1>",click)
#create 2 number button
button=Button(frame,text="2",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create 1 number button
button=Button(frame,text="1",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create / division button
button=Button(frame,text="/",padx=4,pady=4,font="licida 40 bold")
button.pack(side=LEFT,padx=4,pady=4)
button.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="grey")
#create 0 number button
button=Button(frame,text="0",padx=5, pady=5,font="lucida 35 bold")
button.pack(side=LEFT , padx=5,pady=5)
button.bind("<Button-1>",click)
#create + addition button
button=Button(frame,text="+",padx=5,pady=5,font="licida 35 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create - subtraction button
button=Button(frame,text="-",padx=5,pady=5,font="licida 37 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create = equal to  button
button=Button(frame,text="=",padx=5,pady=5,font="licida 33 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="grey" ,padx=4)
#create % percentage button
button=Button(frame,text="%",padx=9, pady=7,font="lucida 30 bold")
button.pack(side=LEFT , padx=5,pady=5)
button.bind("<Button-1>",click)
#create . dot button
button=Button(frame,text=".",padx=5,pady=5,font="licida 37 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create ( number button
button=Button(frame,text="(",padx=5,pady=5,font="licida 37 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
#create ) button
button=Button(frame,text=")",padx=5,pady=5,font="licida 37 bold")
button.pack(side=LEFT,padx=5,pady=5)
button.bind("<Button-1>",click)
frame.pack()

root.mainloop()