import tkinter
class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        super(MainWindow, self). __init__(parent)
        self.parent = parent
        
    def quit(self, event=None):
        self.parent.destroy()
        
application = tkinter.Tk()
application.title('test')
window = MainWindow(application)        
application.protocol('delete',window.quit)
application.mainloop()