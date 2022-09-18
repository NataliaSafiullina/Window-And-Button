from tkinter import *
import time

# close the window and exit program
def clicked_btn1():
    #lbl.configure(text='Кнопка была нажата',font=("Arial Bold", 30))
    quit()
# hide the window for 10 seconds
def clicked_btn2():
    window.withdraw()
    time.sleep(10)
    window.deiconify()


while True:
    window = Tk()
    window.title('Окна и кнопки')
    # window size
    window.geometry('300x100')
    # message
    lbl = Label(window, text='Вы долго смотрели в монитор, \nтеперь посмотрите в окно', font=('Arial Bold', 15),
                justify='center')
    lbl.grid(column=0, row=0, columnspan=2)
    # the first button
    btn1 = Button(window, text='Закрыть навсегда', command=clicked_btn1)
    btn1.grid(column=0, row=2)
    # the second button
    btn2 = Button(window, text='Исчезнуть на 10 сек', command=clicked_btn2)
    btn2.grid(column=1, row=2)
    # loop for window
    window.mainloop()
