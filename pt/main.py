# from tkinter import *

# def finish():
#     root.destroy()
#     print('приложения закрыто')

# root = Tk()
# root.title("приложение")
# root.geometry("300x200")
# root.minsize(200, 100)
# # root.maxsize(300, 400)
# root.protocol("WN_DELETE_WINDOW",finish)
# # root.attributes("-fullscreen", True)
# root.attributes("-alpha", 10)

# label = Label(text="hello my friends")
# label.pack()

# clicks = 0

# def click_button():
#     global clicks
#     clicks += 1
#     btn["text"]= f"Clicks {clicks}"

# btn = Button(text='click me', command=click_button)
# btn.pack()

# def click_button1():
#     root.attributes("-fullscreen", True)
#     btn["state"] = ["disabled"]
#     btn2["state"] = ["normal"]

# def click_button2():
#     root.attributes("-fullscreen", False)
#     btn["state"] = ["disabled"]
#     btn2["state"] = ["normal"]
    
# btn = Button(text='На весь экран', command=click_button1, state=["normal"])
# btn.pack(pady=20, side=LEFT)

# btn2 = Button(text='оконый режим', command=click_button2, state=["normal"])
# btn2.pack(side=RIGHT)

# root.maxsize(300, 400)
# root.protocol("WN_DELETE_WINDOW")
# root.attributes("-fullscreen", True)
# root.attributes("-alpha", 1)



from tkinter import *

root = Tk()
root.title("приложение")
root.geometry("300x200")
root.minsize(200, 100)
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)
root.configure(bg="#ae1fd1")

txt = Label(text='делой выбор', font=('Comic Sans MS', 20, 'bold'))
txt.pack()

frame = Frame(root)
frame.pack(anchor='center')

btn1 = Button(frame, text='хлеб', font=('Comic Sans MS', 13, 'bold'), bg="#9c690c")
btn2 = Button(frame, text='моча', font=('Comic Sans MS', 13, 'bold'), bg="#ffff08")
# btn3 = Button(frame, text='menu3')
# btn4 = Button(frame, text='menu4')

btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
# btn3.grid(row=0, column=2, padx=10, pady=10)
# btn4.grid(row=0, column=3, padx=10, pady=10)


root.mainloop()