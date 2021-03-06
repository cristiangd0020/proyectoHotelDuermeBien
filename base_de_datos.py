import pymysql
import tkinter  
from tkinter import messagebox

def Ejecutarconexion ():
    try:
        messagebox.showinfo("TERMINOS Y CONDICIONES DE USO","Hotelduermebien, se reserva el derecho a exigir que cada usuario, acepte y cumpla los términos aquí expresados como condición previa y necesaria para el acceso, y utilización de los servicios y/o  contenidos brindados por la aplicacion grafica ejecutada por Python. Cuando un usuario accediere a la aplicacion cualquiera de los servicios y/o contenidos existentes, hará presumir el conocimiento del presente texto y que ha manifestado su plena aceptación con respecto a todas y cada una de las disposiciones que lo integran. El usuario que no acepte, se halle en desacuerdo, o incurriere en incumplimiento de las disposiciones fijadas por la aplicacion Hotelduermebien en estas Condiciones Generales, no contará con autorización para el uso de los servicios puedan existir en la aplicación, debiendo evitar el uso de la aplicacion  en forma inmediata, y abstenerse a hacer uso de esta aplicacion.")
        decision = input("ACEPTA LOS TERMINOS Y CONDICIONES DE USO\n SI/NO\n ")
        if decision == "SI" or decision == "si":
            #conexion y creacion de base de datos en PhpMyAdmin
            miconexion=pymysql.Connection(host="localhost",user="root",password="",db="mysql")
            micursor=miconexion.cursor()
            messagebox.showinfo("mensaje","La Conexion con el servidor ha sido exitosa ")
            micursor.execute("CREATE DATABASE IF NOT EXISTS HOTELDUERMEBIEN")
            miconexion.close()
            micursor.close()
            miconexion=pymysql.Connection(host="localhost",user="root",password="",db="HOTELDUERMEBIEN")
            micursor=miconexion.cursor()
            #tabla clientes
            micursor.execute("CREATE TABLE IF NOT EXISTS Clientes ( RUT_cliente INT(11)  PRIMARY KEY, Nombre_cliente VARCHAR(30) NOT NULL, Email VARCHAR(30), Telefono INT(9))")
            messagebox.showinfo("mensaje","La Tabla clientes se ha creado correctamente")
            # creartabla habitaciones
            micursor.execute("CREATE TABLE IF NOT EXISTS habitaciones ( Numero_habitacion INT PRIMARY KEY AUTO_INCREMENT NOT NULL, Estado_habitacion VARCHAR(30), Capacidad VARCHAR(15),Precio INT(7))")
            messagebox.showinfo("mensaje","La Tabla habitaciones se ha creado correctamente")
            #crear tabla empleados
            micursor.execute("CREATE TABLE IF NOT EXISTS Empleados (  ID_Empleado VARCHAR(5) PRIMARY KEY  NOT NULL, RUT_empleado INT(11), Nombre_empleado VARCHAR(30) NOT NULL, Email VARCHAR(30), Telefono INT(9), Contraseña VARCHAR(5))")
            micursor.execute("INSERT INTO empleados(ID_Empleado, RUT_EMPLEADO, Nombre_empleado, Telefono, Contraseña) VALUES ('ADMIN','0123456789','Admin','0','12345')")
            messagebox.showinfo("mensaje","La Tabla empleados se ha creado correctamente")
            # se crea tabla reservas con sus repectivos FOREING KEY
            micursor.execute("CREATE TABLE IF NOT EXISTS Reservas ( ID_reserva INT PRIMARY KEY AUTO_INCREMENT NOT NULL, RUT_cliente INT(11) , Numero_habitacion INT(5), ID_empleado VARCHAR(5) ,fecha date, FOREIGN KEY (RUT_cliente) REFERENCES Clientes(RUT_cliente), FOREIGN KEY (Numero_habitacion) REFERENCES Habitaciones(Numero_habitacion ), FOREIGN KEY (ID_empleado) REFERENCES Empleados(ID_empleado))")
            messagebox.showinfo("mensaje","La Tabla reservas se ha creado correctamente")
            #tabla hospedados
            micursor.execute("CREATE TABLE IF NOT EXISTS Hospedado ( ID_hospedado INT(11) PRIMARY KEY, ID_reserva INT(11), RUT_cliente INT(11), FOREIGN KEY (ID_reserva) REFERENCES Reservas(ID_reserva), FOREIGN KEY (RUT_cliente) REFERENCES Clientes(RUT_cliente))")
            messagebox.showinfo("mensaje","La Tabla hospedados se ha creado correctamente")
            miconexion.commit()
            miconexion.close()
        else:
            messagebox.showerror("ERROR","Usted no ha aceptado los terminos\n y condiciones de uso!")
    except:
        messagebox.showinfo("mensaje","Por favor revise si la base de datos HOTELDUERMEBIEN y las Tablas ya Existen ")

Ejecutarconexion()