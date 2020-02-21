import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

def imprimir():
    if option.get()==0 or nombre.get()=="" or AP.get()=="" or AM.get()=="" or C.get()=="" or D.get()=="" or Ci.get()=="" or M.get()=="":
        mBox.showinfo("Atencion","Datos incompletos")
    else:
        x="Datos personales:\n"
        x=x+"Nombre: "+nombre.get()
        x=x+"\nApellido Paterno: "+AP.get()
        x=x+"\nApellido Materno: "+AM.get()
        x=x+"\nDireccion: "+D.get()
        x=x+"\nColonia: "+C.get()
        x=x+"\nCiudad: "+Ci.get()
        x=x+"\nMunicipio: "+M.get()
        x=x+"\n\nDatos extras:"
        x=x+"\nPasatiempos: "
        if option_1.get()==1:
            x=x+"\n     -Leer"
        if option_2.get()==1:
            x=x+"\n     -Peliculas"
        if option_3.get()==1:
            x=x+"\n     -Redes sociales"
        if option_1.get()==0 and option_2.get()==0 and option_3.get()==0:
            x=x+"No tienes pasatiempos"
        x=x+"\nEstado civil: "
        if option.get()==1:
            x=x+"Soltero"
        if option.get()==2:
            x=x+"Viudo"
        if option.get()==3:
            x=x+"Casado"
        x=x+"\nObjetivos de la vida: "
        if obj.get('1.0',tk.END)=="\n":
            x=x+" No tienes objetivos en la vida :("
        else:    
            x=x+obj.get('1.0',tk.END)
        mBox.showinfo("Datos Personales",x)

def funcion_click1():
    if nombre.get()=="" or AP.get()=="" or AM.get()=="" or C.get()=="" or D.get()=="" or Ci.get()=="" or M.get()=="":        
        mBox.showinfo("Atencion","Datos incompletos")
    else:
        texto8.configure(text="")
        x=""
        x=x+"Nombre: "+nombre.get()
        x=x+"\nApellido Paterno: "+AP.get()
        x=x+"\nApellido Materno: "+AM.get()
        x=x+"\nDireccion: "+D.get()
        x=x+"\nColonia: "+C.get()
        x=x+"\nCiudad: "+Ci.get()
        x=x+"\nMunicipio: "+M.get()
        mBox.showinfo("Datos Personales",x)

def funcion_click2():
    if option.get()==0:        
        mBox.showinfo("Atencion","Datos incompletos")
    else:
        texto12.configure(text="")
        x=""
        x=x+"Pasatiempos: "
        if option_1.get()==1:
            x=x+"\n     -Leer"
        if option_2.get()==1:
            x=x+"\n     -Peliculas"
        if option_3.get()==1:
            x=x+"\n     -Redes sociales"
        if option_1.get()==0 and option_2.get()==0 and option_3.get()==0:
            x=x+"No tienes pasatiempos"
        x=x+"\nEstado civil: "
        if option.get()==1:
            x=x+"Soltero"
        if option.get()==2:
            x=x+"Viudo"
        if option.get()==3:
            x=x+"Casado"
        x=x+"\nObjetivos de la vida: "
        if obj.get('1.0',tk.END)=="\n":
            x=x+" No tienes objetivos en la vida :("
        else:    
            x=x+obj.get('1.0',tk.END)
        mBox.showinfo("Datos Extras",x) 

def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

def funcion_ayuda():
    mBox.showinfo("Acerca de Sistema Escolar","Esta interface fue creada por Ivan Rosales estudiante de ISC de 4to semestre")

ventana=tk.Tk()
ventana.title("Sistema Escolar") #titulo
ventana.resizable(0,0) #dimension

barra_menu=Menu()
ventana.config(menu=barra_menu)

menu_Sistema=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="Sistema",menu=menu_Sistema)
menu_Sistema.add_command(label="Imprimir",command=imprimir)
menu_Sistema.add_command(label="Salir",command=funcion_salir)

menu_ayuda=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de ",command=funcion_ayuda)

tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Datos personales')
tabControl.pack_configure(expand=2,fill="both")
tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text="Datos extras")

texto1=ttk.Label(tab1,text="Nombre:").grid(column=0,row=0)
nombre=tk.StringVar()
Pnombre=ttk.Entry(tab1,width=20, textvariable=nombre)
Pnombre.grid(column=1,row=0)

texto2=ttk.Label(tab1,text="Apellido Paterno:").grid(column=0,row=1) 
AP=tk.StringVar()
PAP=ttk.Entry(tab1,width=20, textvariable=AP).grid(column=1,row=1)

texto3=ttk.Label(tab1,text="Apellido Materno:").grid(column=0,row=2) 
AM=tk.StringVar()
PAM=ttk.Entry(tab1,width=20, textvariable=AM).grid(column=1,row=2)

texto4=ttk.Label(tab1,text="Direccion:").grid(column=0,row=3)
D=tk.StringVar()
PD=ttk.Entry(tab1,width=20, textvariable=D).grid(column=1,row=3)

texto5=ttk.Label(tab1,text="Colonia:").grid(column=0,row=4)
C=tk.StringVar()
C=ttk.Combobox(tab1,width=19, textvariable=C)
C['values']=("","1","2","3","4")
C.grid(column=1,row=4)
C.current(0)

texto6=ttk.Label(tab1,text="Ciudad:").grid(column=0,row=5)
Ci=tk.StringVar()
Ci=ttk.Combobox(tab1,width=19, textvariable=Ci)
Ci['values']=("","1","2","3","4")
Ci.grid(column=1,row=5)
Ci.current(0)

texto7=ttk.Label(tab1,text="Municipio:").grid(column=0,row=6)
M=tk.StringVar()
M=ttk.Combobox(tab1,width=19, textvariable=M)
M['values']=("","1","2","3","4")
M.grid(column=1,row=6)
M.current(0)

ImprimirDP=ttk.Button(tab1, text="Imprimir datos personales",command=funcion_click1).grid(column=5, row=7)
texto8=ttk.Label(tab1,text="")
texto8.grid(column=1,row=7)

texto9=ttk.Label(tab2,text="Pasatiempos:").grid(column=0,row=0)
option_1=tk.IntVar()
casilla_1=tk.Checkbutton(tab2,text="Leer",variable=option_1).grid(column=0,row=1)
option_2=tk.IntVar()
casilla_2=tk.Checkbutton(tab2,text="Peliculas",variable=option_2).grid(column=1,row=1)
option_3=tk.IntVar()
casilla_3=tk.Checkbutton(tab2,text="Redes sociales",variable=option_3).grid(column=2,row=1)

texto10=ttk.Label(tab2,text="Estado civil:").grid(column=0,row=2)
option=tk.IntVar()
radio1=tk.Radiobutton(tab2,text="Soltero", variable=option,value=1).grid(column=0,row=3,sticky=tk.W)
radio2=tk.Radiobutton(tab2,text="Viudo", variable=option,value=2).grid(column=1,row=3,sticky=tk.W)
radio3=tk.Radiobutton(tab2,text="Casado", variable=option,value=3).grid(column=2,row=3,sticky=tk.W)

texto11=ttk.Label(tab2,text="Objetivo de la vida:").grid(column=0,row=4)
obj=scrolledtext.ScrolledText(tab2,width=30,height=3,wrap=tk.WORD)
obj.grid(column=0,columnspan=3)

ImprimirDE=ttk.Button(tab2, text="Imprimir datos extras",command=funcion_click2).grid(column=4, row=6)
texto12=ttk.Label(tab2,text="")
texto12.grid(column=1,row=6)

ventana.mainloop()