from cProfile import label
#from curses.panel import top_panel
from msilib.schema import TextStyle
from multiprocessing import connection
from pydoc import text
from re import A
import sqlite3
import string
import tkinter
from tokenize import Name
from unicodedata import name
from mysqlx import Column 
import pymysql
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

db = pymysql.connect(user='root',host='localhost',password='',database='hotelduermebien')
cursor = db.cursor()



#Clases (clientes - empleados - habitaciones - hospedado - reservas)

class clientes:
    def __init__(self, RUT_cliente, Nombre_cliente, Email, Telefono):
        self.RUT_cliente = RUT_cliente
        self.Nombre_cliente = Nombre_cliente
        self.Email = Email
        self.Telefono = Telefono

class empleados:
    def __init__(self, RUT_empleado, Nombre_empleado, Email, Telefono):
        self.RUT_empleado = RUT_empleado
        self.Nombre_empleado = Nombre_empleado
        self.Email = Email
        self.Telefono = Telefono

class habitaciones:
    def __init__(self, Numero_habitacion, Estado_habitacion, Capacidad, Precio):
        self.Numero_habitacion = Numero_habitacion
        self.Estado_habitacion = Estado_habitacion
        self.Capacidad = Capacidad
        self.Precio = Precio

class hospedado:
    def __init__(self, ID_hospedado, ID_reserva, RUT_cliente):
        self.ID_hospedado = ID_hospedado
        self.ID_reserva = ID_reserva
        self.RUT_cliente = RUT_cliente

class reservas:
    def __init__(self, ID_reserva, RUT_cliente, Numero_habitacion, RUT_empleado, fecha):
        self.ID_reserva = ID_reserva
        self.RUT_cliente = RUT_cliente
        self.Numero_habitacion = Numero_habitacion
        self.RUT_empleado = RUT_empleado
        self.fecha = fecha

#abre ventana para poder registrar clientes nuevos
def registarClientes():
        ventana.withdraw()
        ventanaRegCliente = Toplevel()
        ventanaRegCliente.title("Registro clientes")
        ventanaRegCliente.geometry("550x370")
        ventana.configure(background="white")
        
        lbl_img = tkinter.Label(ventanaRegCliente).place()

        rutCliente = tk.Label(ventanaRegCliente, text="Ingrese RUT cliente", bg="gray", fg="white")
        rutCliente.place(x=70, y=80, width=160, height=30)
        entradaRut = tk.Entry(ventanaRegCliente)
        entradaRut.place(x=240, y=80, width=200, height=30)

        nombreCliente = tk.Label(ventanaRegCliente, text="Ingrese nombre cliente", bg="gray", fg="white")
        nombreCliente.place(x=70, y=130, width=160, height=30)
        entradaNomCliente = tk.Entry(ventanaRegCliente)
        entradaNomCliente.place(x=240, y=130, width=200, height=30)

        emailCliente = tk.Label(ventanaRegCliente, text="Ingrese Email ", bg="gray", fg="white")
        emailCliente.place(x=70, y=180, width=160, height=30)
        entradaEmailCliente = tk.Entry(ventanaRegCliente)
        entradaEmailCliente.place(x=240, y=180, width=200, height=30)

        telCliente = tk.Label(ventanaRegCliente, text="Ingrese Telefono", bg="gray", fg="white")
        telCliente.place(x=70, y=230, width=160, height=30)
        entradatelCliente = tk.Entry(ventanaRegCliente)
        entradatelCliente.place(x=240, y=230, width=200, height=30)
        def nuevoRegistroCliente():
            element= [entradaRut.get(),entradaNomCliente.get(),entradaEmailCliente.get(),entradatelCliente.get()]
            sql= "INSERT INTO clientes (RUT_cliente, Nombre_cliente, Email, Telefono) VALUES ('{}','{}','{}','{}')".format(element[0],element[1],element[2],element[3])
            try:
                cursor.execute(sql)
                db.commit()
                messagebox.showinfo("mensaje","El registro se ha creado correctamente")
            except pymysql.err.IntegrityError:
                messagebox.showinfo("mensaje","El rut está duplicado")
                    
        btnRegistrarCliente = tk.Button(ventanaRegCliente, text="Registrar", fg="black", bg="green", command=nuevoRegistroCliente)
        btnRegistrarCliente.place(x=70, y=280, width=200, height=30)

        btnRegresar = tk.Button(ventanaRegCliente, text="Regresar", fg="black", bg="green",command=ventanaRegCliente.destroy)
        btnRegresar.place(x=240, y=280, width=200, height=30)
   


def RegistrarEmpleados():
    ventana2 = tk.Tk()
    ventana2.title("Registrar Empleado Nuevo")
    ventana2.geometry("500x600")
    ventana2.configure(background="white")
    
    #Necesito insertar imagenes en esta funcion (RegistrarEmpleados) pero tira diferentes tipos de errores
    #ya que tkinter a mi alparecer es muy webiao y le pone color por tratar de pensar 2 cosas diferentes
    #Como guia pueden usar las lineas de codigo 171-176. 
    
    #Entradas RegistrarEmpleado
    etiqueta0 = tk.Label(ventana2, text="Rut Empleado", bg="gray", fg="white")
    etiqueta0.place(x=305, y=300, width=160, height=30)
    entrada0 = tk.Entry(ventana2)
    entrada0.place(x=280, y=340, width=200, height=30)
    
    etiqueta1 = tk.Label(ventana2, text="Nombre Empleado", bg="gray", fg="white")
    etiqueta1.place(x=45, y=300, width=160, height=30)
    entrada1 = tk.Entry(ventana2)
    entrada1.place(x=20, y=340, width=200, height=30)
    
    etiqueta2 = tk.Label(ventana2, text="Email", bg="gray", fg="white")
    etiqueta2.place(x=45, y=410, width=160, height=30)
    entrada2 = tk.Entry(ventana2)
    entrada2.place(x=20, y=450, width=200, height=30)
    
    etiqueta3 = tk.Label(ventana2, text="Telefono", bg="gray", fg="white")
    etiqueta3.place(x=305, y=410, width=160, height=30)
    entrada3 = tk.Entry(ventana2)
    entrada3.place(x=280, y=450, width=200, height=30)
    
    
    def Registar():
        empleado1 = empleados(entrada0.get(), entrada1.get(), entrada2.get(), entrada3.get())
        insertarEmpleado = "INSERT INTO empleados(RUT_EMPLEADO, Nombre_empleado, Email, Telefono) VALUES ('{0}','{1}','{2}','{3}')".format(empleado1.RUT_empleado, empleado1.Nombre_empleado, empleado1.Email, empleado1.Telefono)
        try:
            cursor.execute(insertarEmpleado)
            db.commit()
            messagebox.showinfo(message="Registro exitoso", title="Aviso")
            entrada0.delete(0, 'end')
            entrada1.delete(1, 'end')
            entrada2.delete(2, 'end')
            entrada3.delete(3, 'end')
            db.close
        except:
            db.rollback
            messagebox.showinfo(message="No se pudo registrar empleado", title="Aviso")
            db.close
            
    #Boton para registrar empleado nuevo
    btnRegistrar = tk.Button(ventana2, text="Registrar", fg="black",bg="green" , command=Registar)
    btnRegistrar.place(x=135, y=500, width=200, height=30)
    
    ventana2.mainloop()



def regitrarHabitaciones():
        ventana.withdraw()
        ventanaRegHabitaciones = Toplevel()
        ventanaRegHabitaciones.title("Registro Habitaciones")
        ventanaRegHabitaciones.geometry("600x500")

        marco = LabelFrame(ventanaRegHabitaciones,text="Registro de Habitaciones")
        marco.place(x=50,y=50,width=500,height=400)

        #variables
        numero_Habitacion= StringVar()
        estado_Habitacion= StringVar()
        capacidad=StringVar()
        precio=StringVar()

        #Labels
        lblnumHabitacion =Label(marco,text="Numero Habitacion").grid(column=0, row=0)
        txtnumHabitacion =Entry(marco, textvariable=numero_Habitacion).grid(column=1,row=0)

        lblestHabitacion =Label(marco,text="Estado Habitacion").grid(column=0, row=1)
        txtestHabitacion =ttk.Combobox(marco,values=["Disponible","Ocupado"],textvariable=estado_Habitacion)
        txtestHabitacion.grid(column=1,row=1)
        txtestHabitacion.current(0)

        lblcapaciHabitacion =Label(marco,text="Capacidad").grid(column=2, row=0)
        txtcapaciHabitacion =Entry(marco,textvariable=capacidad).grid(column=3,row=0)

        lblprecioHabitacion =Label(marco,text="Precio").grid(column=2, row=1)
        txtprecioHabitacion =Entry(marco,textvariable=precio).grid(column=3,row=1)

        #mensajes en la ventana
        lblmensaje = Label(marco, text="aqui van los mensajes", fg="green")
        lblmensaje.grid(column=0,row=2,columnspan=4)

        #treeview
        
        tvHabitaciones= ttk.Treeview(marco)
        tvHabitaciones.grid(column=0, row=3, columnspan=4)
        tvHabitaciones["columns"]=("Numero Habitacion","Estado habitacion", "Capacidad", "Precio",)
        tvHabitaciones.column('#0', width=0, stretch=NO)
        tvHabitaciones.column('Numero Habitacion', width=150, anchor=CENTER)
        tvHabitaciones.column('Estado habitacion', width=150, anchor=CENTER)
        tvHabitaciones.column('Capacidad', width=90, anchor=CENTER)
        tvHabitaciones.column('Precio', width=90, anchor=CENTER)
        tvHabitaciones.heading('#0', text="")
        tvHabitaciones.heading('Numero Habitacion', text='Numero Habitacion', anchor=CENTER )
        tvHabitaciones.heading('Estado habitacion', text='Estado habitacion', anchor=CENTER )
        tvHabitaciones.heading('Capacidad',text='Capacidad', anchor=CENTER )
        tvHabitaciones.heading('Precio',text='Precio', anchor=CENTER)
            
        #Botones      
        btnRegistrarHabitacion1= tk.Button(marco, text="Eliminar", fg="white", bg="green", command=lambda:eliminar())
        btnRegistrarHabitacion1.grid(column=0,row=4)

        btnRegistroHabitaciones= tk.Button(marco, text="Registrar", fg="white", bg="green",command=lambda:RegistroHabitacion())
        btnRegistroHabitaciones.grid(column=1,row=4)

        btnModificarHabitacion= tk.Button(marco, text="modificar", fg="white", bg="green", command=lambda:actualizar())
        btnModificarHabitacion.grid(column=2,row=4)

        #funciones
        def vaciar_tabla():
            filas = tvHabitaciones.get_children()
            for fila in filas:
                tvHabitaciones.delete(fila)
        #antes de rellenar se vacia la tabla primero
        # 
        def limpiar():
            numero_Habitacion.set("")
            estado_Habitacion.set("")
            capacidad.set("")
            precio.set("")
        
        def validar():
            return len(numero_Habitacion.get()) and len(capacidad.get()) and len(precio.get()) 

        def rellenarTabla():
            vaciar_tabla()
            sql = "select * from habitaciones"
            cursor.execute(sql)
            filas=cursor.fetchall()
            for fila in filas:
                Numero_habitacion = fila[0]
                tvHabitaciones.insert("", END, Numero_habitacion, text=Numero_habitacion, values=fila )
        def  eliminar():
            numero_Habitacion= tvHabitaciones.selection()[0]
            if int(numero_Habitacion)>0:
                sql="delete from habitaciones where numero_Habitacion="+numero_Habitacion
                cursor.execute(sql)
                db.commit()
                tvHabitaciones.delete(numero_Habitacion)
                lblmensaje.config(text="se ha eliminado correctamente")
            else:
                lblmensaje(text="Seleccion un registro para eliminar", fg="red")
            
        def RegistroHabitacion():
            if validar():
                element= [numero_Habitacion.get(),estado_Habitacion.get(),capacidad.get(),precio.get()]
                sql= "INSERT INTO habitaciones (Numero_habitacion, Estado_habitacion, Capacidad, Precio) VALUES ('{}','{}','{}','{}')".format(element[0],element[1],element[2],element[3])
                cursor.execute(sql)
                db.commit()
                lblmensaje.config(text="Se ha guardado el registro correctamente", fg="green")
                rellenarTabla()
                limpiar()
            else:
                lblmensaje.config(text="los campos no deben estar vacios", fg="red")

        def actualizar():
            pass
        #se ejecuta para actualizar la tabla
        rellenarTabla()


#Ventana login principal!

ventana = tk.Tk()
ventana.title("Login Hotel")
ventana.geometry("500x580")
ventana.configure(background="white")

#Imagenes logos !

iconImg = tkinter.PhotoImage(file="img\imgLogin\iconLogo.png")
lbl_img = tkinter.Label(ventana, image=iconImg).place(y=-85, x=-15)
iconTilte = tkinter.PhotoImage(file="img\imgLogin\iconTitle.png")
lbl_Title = tkinter.Label(ventana, image=iconTilte).place(y=15, x=2)   
iconLogin = tkinter.PhotoImage(file="img\imgLogin\iconLogin.png")
lbl_Login = tkinter.Label(ventana, image=iconLogin).place(y=448, x=110)

#Entradas Inicio
idEmpleado = tk.Label(ventana, text="Ingrese ID Empleado", bg="gray", fg="white")
idEmpleado.place(x=170, y=250, width=160, height=30)
entradaId = tk.Entry(ventana)
entradaId.place(x=150, y=290, width=200, height=30)
    
contraseña = tk.Label(ventana, text="Ingrese Contraseña", bg="gray", fg="white")
contraseña.place(x=170, y=340, width=160, height=30)
entradaContraseña = tk.Entry(ventana)
entradaContraseña.place(x=150, y=380, width=200, height=30)


#Botones Inicio   
btnIngresar = tk.Button(ventana, text="Ingresar", fg="black", bg="green",command="")#Falta agregar la accion del command
btnIngresar.place(x=150, y=445, width=200, height=30)

btnRegistrarEmpleado = tk.Button(ventana, text="Registrar Empleado",fg="black", bg="green",command=RegistrarEmpleados)
btnRegistrarEmpleado.place(x=150, y=485, width=200, height=30)

#insertar en otra ventana o donde sea convenientes es solo de pruebas
"""btnRegistrarCliente = tk.Button(ventana, text="Registar Cliente", fg="black", bg="green",command=registarClientes)
btnRegistrarCliente.place(x=150, y=490, width=200, height=30)
"""
# se agrega el boton de registrar habitacion de momento lo pondré aqui para hacer las pruebas correspondientes
btnRegistrarHabitacion = tk.Button(ventana, text="Registar Habitación", fg="black", bg="green",command=regitrarHabitaciones)
btnRegistrarHabitacion.place(x=150, y=530, width=200, height=30)

ventana.mainloop()

