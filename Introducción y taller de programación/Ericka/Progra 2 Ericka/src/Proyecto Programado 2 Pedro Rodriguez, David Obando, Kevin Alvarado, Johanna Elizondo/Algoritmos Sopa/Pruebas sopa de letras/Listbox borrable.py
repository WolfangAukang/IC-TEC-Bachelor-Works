import Tkinter as tk

def main():
    mainWindow = tk.Tk()
    v = tk.StringVar()
    entryBox = tk.Entry(mainWindow, textvariable=v).grid(column=1, row=1)
    def test():
        entryBox.delete(0,20)
    testButton = tk.Button(mainWindow, text='Go!', command=test, padx=10).grid(row=2, column=1) 
    tk.mainloop()
main()
