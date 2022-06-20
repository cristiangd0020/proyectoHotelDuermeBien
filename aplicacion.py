
from msilib.schema import TextStyle
from pydoc import text
from re import A
import tkinter 
import pymysql
import tkinter as tk
from tkinter import *
import base_de_datos as bd
from tkinter import messagebox

db = pymysql.connect(user='root',host='localhost',password='',database='hotelduermebien')
cursor = db.cursor()

#Command = base_de_datos.Ejecutarconexion()

#Clases (clientes - empleados - habitaciones - hospedado - reservas)

class clientes:
    def __init__(self, RUT_cliente, Nombre_cliente, Email, Telefono):
        self.RUT_cliente = RUT_cliente
        self.Nombre_cliente = Nombre_cliente
        self.Email = Email
        self.Telefono = Telefono

class empleados:
    def __init__(self, RUT_empleado, Nombre_empleado, Email, telefono):
        self.RUT_empleado = RUT_empleado
        self.Nombre_empleado = Nombre_empleado
        self.Email = Email
        self.telefono = telefono

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



def ventanaLogin():
    ventana = tk.Tk()
    ventana.title("Login Hotel")
    ventana.geometry("500x580")
    ventana.configure(background="white")

   
    #Creacion Iconos
    iconImg = tkinter.PhotoImage(file="img\iconLogo.png")
    lbl_img = tkinter.Label(ventana, image=iconImg).place(y=-85, x=-15)

    
    iconTilte = tkinter.PhotoImage(file="img\iconTitle.png")
    lbl_Title = tkinter.Label(ventana, image=iconTilte).place(y=15, x=2)
    
    iconLogin = tkinter.PhotoImage(file="img\iconLogin.png")
    lbl_Login = tkinter.Label(ventana, image=iconLogin).place(y=448, x=110)
    
    
    #abre ventana para poder registrar clientes nuevos
    def registarClientes():
            ventana.withdraw()
            ventanaRegCliente = Toplevel()
            ventanaRegCliente.title("Registro clientes")
            ventanaRegCliente.geometry("550x370")
            lbl_img = tkinter.Label(ventanaRegCliente, image=iconImg).place()

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
                    entradaRut.set("")
                    entradaNomCliente.set("")
                    entradaEmailCliente.set("")
                    entradatelCliente.set("")
                except pymysql.err.IntegrityError:
                    messagebox.showinfo("mensaje","El rut está duplicado")
              
            



            btnRegistrarCliente = tk.Button(ventanaRegCliente, text="Registrar", fg="black", bg="green", command=nuevoRegistroCliente)
            btnRegistrarCliente.place(x=70, y=280, width=200, height=30)

            btnRegresar = tk.Button(ventanaRegCliente, text="Regresar", fg="black", bg="green",command=ventanaRegCliente.destroy)
            btnRegresar.place(x=240, y=280, width=200, height=30)
   


    
    
    idEmpleado = tk.Label(ventana, text="Ingrese ID Empleado", bg="gray", fg="white")
    idEmpleado.place(x=170, y=250, width=160, height=30)
    entradaId = tk.Entry(ventana)
    entradaId.place(x=150, y=290, width=200, height=30)
    
    contraseña = tk.Label(ventana, text="Ingrese Contraseña", bg="gray", fg="white")
    contraseña.place(x=170, y=340, width=160, height=30)
    entradaContraseña = tk.Entry(ventana)
    entradaContraseña.place(x=150, y=380, width=200, height=30)
   
    btnIngresar = tk.Button(ventana, text="Ingresar", fg="black", bg="green",command="")#Falta agregar la accion del command
    btnIngresar.place(x=150, y=445, width=200, height=30)


    #insertar en otra ventana o donde sea convenientes es solo de pruebas
    btnRegistrarCliente = tk.Button(ventana, text="Registar Cliente", fg="black", bg="green",command=registarClientes)
    btnRegistrarCliente.place(x=150, y=490, width=200, height=30)

    



    ventana.mainloop()


ventanaLogin()


