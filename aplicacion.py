from msilib.schema import TextStyle
from pydoc import text
import tkinter
import pymysql, base_de_datos
import tkinter as tk
from tkinter import *

db = pymysql.connect(user='root',host='localhost',password='',database='hotelduermebien',port=3306)
cursor = db.cursor()

# Command = base_de_datos.Ejecutarconexion()

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

    ventana.mainloop()



ventanaLogin()


