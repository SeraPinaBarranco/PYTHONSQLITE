from tkinter import *
import ctypes #modulo estandar para la resolucion

ventana = Tk() #instanciar una ventana tkinter
ventana.title ("Primera Ventana") #estblecer el titulo

myFrame = Frame(ventana)
myFrame.pack(fill="both", expand=1) #rellenar el frame al ancho de la ventana
myFrame.config(bg="#c29f9f") #dar color al frame


#guardar la resolución de la pantalla
user32 = ctypes.windll.user32 
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

tamano = "" + str(int(ancho/2)) + "x" + str(int(alto/2)) + ""

ventana.geometry(tamano)

label1 = Label(myFrame,text="Hola", bg="#c29f9f", fg="#8cf584")
label1.config(font=("Verdana",24, "italic")) #estable la fuente, tamaño y negrita
label1.grid(column=2, row= 2, padx=8, pady=8)#establece posicion en celda y margen con el contenedor

label2 = Label(myFrame,text="Hola2",bg="#c29f9f", fg="#8cf584")
label2.config(font=("Verdana",24, "bold"))
label2.grid(column=3, row= 2)

boton1 = Button(myFrame, text="Salir" ,bg="#c29f9f", fg="#8cf584", font=("Verdana 16 bold"))

boton1.grid(column=4, row=3)

ventana.mainloop()