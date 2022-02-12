import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style 

bg_color = '#80cc80'
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Centennial College')
        # self.geometry('500x400')        
        
        s = Style()
        s.configure('My.TFrame', background=bg_color)

        frmContainer = ttk.Frame(self, style='My.TFrame')
        frmContainer.pack(fill=BOTH, expand=True)
        frmContainer['padding'] = 10

        # when resize window, grid cell should be also resized
        frmContainer.columnconfigure(0, weight=1)
        frmContainer.columnconfigure(1, weight=1)
        frmContainer.columnconfigure(2, weight=2)

        for i in range(9):
            frmContainer.rowconfigure(i, weight=1)

        lblTitle = Label(frmContainer, text = "ICEET Student Survey", font='Helvetica 15 bold italic')
        lblTitle.config(bg=bg_color)
        lblTitle.grid(row = 0, column = 0, columnspan=3, pady = 2)

        lblFullName = Label(frmContainer, text = "Full name:")
        lblFullName.config(bg=bg_color)
        lblFullName.grid(row = 1, column = 0, sticky = W, pady = 2)

        self.fullname = StringVar()
        self.fullname.set("Narendra Pershad")
        txtFullName = Entry(frmContainer, textvariable=self.fullname)        
        txtFullName.grid(row = 1, column = 1, sticky = W, pady = 2)

        # Residency
        lblResidency = Label(frmContainer, text = "Residency:")
        lblResidency.config(bg=bg_color)
        lblResidency.grid(row = 2, column = 0, sticky = W, pady = 2)

        # radio button
        self.residency = StringVar()  
        self.residency.set("dom")

        radioDomestic = Radiobutton(frmContainer, text="Domestic", variable=self.residency, value="dom")
        radioDomestic.grid(row = 2, column = 1, sticky = W, pady = 2)
        radioDomestic.config(bg=bg_color)

        radioInternational = Radiobutton(frmContainer, text="International", variable=self.residency, value="intl")
        radioInternational.grid(row = 3, column = 1, sticky = W, pady = 2)
        radioInternational.config(bg=bg_color)

        # Program
        lblProgram = Label(frmContainer, text = "Program:")
        lblProgram.config(bg=bg_color)
        lblProgram.grid(row = 4, column = 0, sticky = W, pady = 2)

        self.program = StringVar()
        combobox = ttk.Combobox(frmContainer, textvariable=self.program)
        combobox.grid(row = 4, column = 1, sticky = W, pady = 2)

        combobox['values'] = (' Health', 
                          ' Eeating',
                          ' Learning',
                          ' Running',
                          )

        combobox.current()
        self.program.set("Health")

        # Courses
        lblCourses = Label(frmContainer, text = "lblCourses:")
        lblCourses.config(bg=bg_color)
        lblCourses.grid(row = 5, column = 0, sticky = W, pady = 2)

        self.course1 = StringVar()  
        self.course2 = StringVar()  
        self.course3 = StringVar()
        self.course1.set("COMP100")
        
        chkCourse1 = Checkbutton(frmContainer, text = "Programming I", 
                            variable = self.course1,
                            onvalue = "COMP100",
                            offvalue = ""
        )
        chkCourse1.config(bg=bg_color)
        chkCourse1.grid(row = 5, column = 1, sticky = W, pady = 2)
        
        chkCourse2 = Checkbutton(frmContainer, text = "Web Page Design",
                            variable = self.course2,
                            onvalue = "COMP213",                            
                            offvalue = "")
        chkCourse2.config(bg=bg_color)
        chkCourse2.grid(row = 6, column = 1, sticky = W, pady = 2)
        
        chkCourse3 = Checkbutton(frmContainer, text = "Software Engineering",
                            variable = self.course3,
                            onvalue = "COMP120",
                            offvalue = "")  
        chkCourse3.config(bg=bg_color)
        chkCourse3.grid(row = 7, column = 1, sticky = W, pady = 2)


        # buttons
        btnReset = Button(frmContainer, text ="Reset", command = self.onReset)
        btnReset.grid(row = 8, column=0, sticky="news", padx=2, pady = 2)

        btnOK = Button(frmContainer, text ="OK", command = self.onOK)
        btnOK.grid(row = 8, column=1, sticky="news", padx=2, pady = 2)

        btnExit = Button(frmContainer, text ="Exit", command = self.onExit)
        btnExit.grid(row = 8, column=2, sticky="news", padx=2, pady = 2)
        

    def onReset(self):
        self.fullname.set("Narendra Pershad")
        self.residency.set("dom")
        self.program.set("Health")
        self.course1.set("COMP100")
        self.course2.set("")
        self.course3.set("")
        


    def onOK(self):
        msg = f'''
            {self.fullname.get()}
            {self.residency.get()}
            {self.program.get()}
            ({self.course1.get()} {self.course2.get()} {self.course3.get()})
        '''
        messagebox.showinfo("Information", msg)

    def onExit(self):
        self.quit()


if __name__ == "__main__":
    app = App()
    app.mainloop()