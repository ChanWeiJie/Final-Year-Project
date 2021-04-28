#Button GUI

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Buttons")
root.geometry("200x350")

app = Frame(root) #hold widgets
app.grid() #put into grid
buttonDA = Button(app, text = " Click to go to A ")
buttonDA.config( height = 5, width = 30 )
buttonDA.grid() #put button into grid

buttonDB = Button(app, text = " Click to go to B ")
buttonDB.config( height = 5, width = 30 )
buttonDB.grid() #put button into grid

buttonDC = Button(app, text = " Click to go to C ")
buttonDC.config( height = 5, width = 30 )
buttonDC.grid() #put button into grid

buttonDD = Button(app, text = " Click to go to D ")
buttonDD.config( height = 5, width = 30 )
buttonDD.grid() #put button into grid




#define methods


#start the event
root.mainloop()
