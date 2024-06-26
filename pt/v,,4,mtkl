import tkinter as tk

def open_second_window():
    main_window.withdraw()
    second_window.deiconify()

def back_to_main_window():
    main_window.deiconify()

main_window = tk.Tk()
main_window.title("Main Window")
main_window.configure(bg="#ae1fd1")
txt = tk.Label(main_window, text='Main window', font=('Comic Sans MS', 18, 'bold'))
txt.pack()

open_button = tk.Button(main_window)
open_button = tk.Button(main_window,text="Second Window", command=open_second_window)
open_button.pack(pady=20)
second_window = tk.Toplevel(main_window)
second_window.title("Second Window")
second_window.geometry("500x500")
second_window.configure(bg="#ae1fd1")
second_window.withdraw()

txt1 = tk.Label(second_window, text='Second window', font=('Comic Sans MS', 18, 'bold'), bg="#f7f700")
txt1.pack()

back_button = tk.Button(second_window, text='Second window', command=back_to_main_window)
back_button.pack(pady=20)


main_window.mainloop()