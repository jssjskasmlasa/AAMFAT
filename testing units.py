#import the module
from tkinter import *



#vreate a window
window = Tk()

#change  title
window.title('Collatz Conjecture')

#change the chape of the window
window.geometry('300x300')

#add a label(text)
text_label = Label(window,text='insert a number',fg='green')
text_label.config(font=('Courier',30))
text_label.pack()


#take input from user
data=Entry(window,fg='green')
data.pack()

def excute():
    data=data.pack()
    print(data)
    text.insert(0.0,print(data))

#add the enter button
bt = Button(window,text='enter',padx=29,command=excute)
bt.pack()


text = Text(window,width=10,height=10,wrap=WORD)
text.pack()




window.mainloop()




#collats logical calculator
n = int(input("Enter Starting Number: "))

print(n)

cycle = 0

while n != 1:
    cycle+=1

    print('iteration:',cycle)

    if (n % 2 == 0):

        n = n/2

        print(n)
    elif n %3 ==0:
         n = (n*3)+1

    elif n !=1:
        print(n ,'not = to one')