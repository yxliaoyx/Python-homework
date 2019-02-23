import tkinter

def Analyze():
    Analyze_window = tkinter.Toplevel(root)
    
    tkinter.Label(Analyze_window, text='開始年月').pack()
    
    start_listbox = tkinter.Listbox(Analyze_window)
    for i in range(1,13,2):
        start_listbox.insert(tkinter.END, '2018/{}-{}'.format(i, i+1))
    start_listbox.pack()
    
    tkinter.Label(Analyze_window, text='結束年月').pack()
    end_listbox = tkinter.Listbox(Analyze_window)    
    for i in range(1,13,2):
        end_listbox.insert(tkinter.END, '2018/{}-{}'.format(i, i+1))
    end_listbox.pack()
    
    tkinter.Button(Analyze_window, text='開始分析').pack()
    
    tkinter.Button(Analyze_window, text='結束', command=Analyze_window.destroy).pack()


root = tkinter.Tk()
menu = tkinter.Menu(root)
Menu_menu = tkinter.Menu(menu)
menu.add_cascade(label="Menu", menu=Menu_menu)

Menu_menu.add_command(label="Analyze", command=Analyze)
Menu_menu.add_separator()
Menu_menu.add_command(label="Exit", command=root.quit)

root.config(menu=menu)
root.mainloop()

root.destroy()
