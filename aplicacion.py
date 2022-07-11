from cProfile import label
from msilib.schema import TextStyle
from multiprocessing import connection
from pydoc import text
from re import A
import sqlite3
import tkinter
from tokenize import Name
from unicodedata import name
import pymysql
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random, string
from datetime import datetime

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
        ventana = tk.Tk()
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
    
    
    def generarIdEmpleado(text):
        ID = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
        return ID
    
    
    def generarContraseñaEmpleado(text):
    
        contraseña = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
        return contraseña
    
          

    entrada0 = tk.Entry(ventana2) #ID GENERADA
     
       
    
    entrada5 = tk.Entry(ventana2) #CONTRASEÑA GENERADA
    
    
    
    etiqueta1 = tk.Label(ventana2, text="Rut Empleado", bg="gray", fg="white")
    etiqueta1.place(x=70, y=80, width=160, height=30)
    entrada1 = tk.Entry(ventana2)
    entrada1.place(x=240, y=80, width=200, height=30)
    
    etiqueta2 = tk.Label(ventana2, text="Nombre Empleado", bg="gray", fg="white")
    etiqueta2.place(x=70, y=130, width=160, height=30)
    entrada2 = tk.Entry(ventana2)
    entrada2.place(x=240, y=130, width=200, height=30)

    etiqueta3 = tk.Label(ventana2, text="Email", bg="gray", fg="white")
    etiqueta3.place(x=70, y=180, width=160, height=30)
    entrada3 = tk.Entry(ventana2)
    entrada3.place(x=240, y=180, width=200, height=30)
    
    etiqueta4 = tk.Label(ventana2, text="Telefono", bg="gray", fg="white")
    etiqueta4.place(x=70, y=230, width=160, height=30)
    entrada4 = tk.Entry(ventana2)
    entrada4.place(x=240, y=230, width=200, height=30)
    
    
    def Registar():
        empleado1 = empleados(entrada1.get(), entrada2.get(), entrada3.get(), entrada4.get())
        id_empleado = generarIdEmpleado(entrada0.get())
        contraseña_empleado = generarContraseñaEmpleado(entrada5.get())
        insertarEmpleado = "INSERT INTO empleados(ID_Empleado, RUT_EMPLEADO, Nombre_empleado, Email, Telefono, Contraseña) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(id_empleado, empleado1.RUT_empleado, empleado1.Nombre_empleado, empleado1.Email, empleado1.Telefono, contraseña_empleado)
        
        def mostrarIdContraseña():
            cursor.execute("SELECT ID_Empleado, Contraseña FROM empleados WHERE ID_Empleado = '"+id_empleado+"' AND Contraseña = '"+contraseña_empleado+"'")
            filas = cursor.fetchall()
            if (len(filas) > 0):
                for fila in filas:
                    entrada0.delete(0, 'end')
                    entrada5.delete(0, 'end')
                    titulo = tk.Label(ventana2, text="Estos datos son para ingresar al sistema", fg="green", font=(NONE, 15))
                    titulo.place(x=65, y=340, width=380, height=30)
                    entrada0.insert(0, fila[0])
                    entrada5.insert(0, fila[1])
                    messagebox.showinfo(message="[!] Se ha generado una ID y una Contraseña para hacer ingreso al sistema")
            else:
                messagebox.showinfo(message="[X] Vaya algo ha fallado") 
        
        try:
            cursor.execute(insertarEmpleado)
            db.commit()
            entrada1.delete(0, 'end')
            entrada2.delete(0, 'end')
            entrada3.delete(0, 'end')
            entrada4.delete(0, 'end')
            
            messagebox.showinfo(message="Registro exitoso", title="Aviso")
        
            etiqueta0 = tk.Label(ventana2, text="ID", bg="gray", fg="white")
            etiqueta0.place(x=45, y=380, width=160, height=30)
            entrada0.place(x=210, y=380, width=200, height=30)
            
            etiqueta5 = tk.Label(ventana2, text="Contraseña", bg="gray", fg="white")
            etiqueta5.place(x=45, y=410, width=160, height=30)
            entrada5.place(x=210, y=410, width=200, height=30)
            mostrarIdContraseña()
            db.close
        except:
            db.rollback
            messagebox.showinfo(message="[X] No se pudo registrar empleado", title="Aviso")
            db.close
        
        
            
    #Boton para registrar empleado nuevo
    btnRegistrar = tk.Button(ventana2, text="Registrar", fg="black",bg="green" , command=Registar)
    btnRegistrar.place(x=135, y=500, width=200, height=30)
    
    ventana2.mainloop()


# la funcion mopdificar no me funciona con el toplevel estoy tratando de corregir eso
def regitrarHabitaciones():
    ventanaHabitaciones=Toplevel()
    ventanaHabitaciones.title("Registro Habitaciones")
    ventanaHabitaciones.geometry("600x500")

    modificar = False
    num_Habitacion= StringVar()
    estado_Habitacion= StringVar()
    capacidad=StringVar()
    precio=StringVar()
            
    def seleccionar(event):
        num= tvHabitaciones.selection()[0]
        if int(num)>0:
            num_Habitacion.set(tvHabitaciones.item(num,"values")[0])
            estado_Habitacion.set(tvHabitaciones.item(num,"values")[1])
            capacidad.set(tvHabitaciones.item(num,"values")[2])
            precio.set(tvHabitaciones.item(num,"values")[3])

    marco = LabelFrame(ventanaHabitaciones, text="Formulario de gestion Estudiantes")
    marco.place(x=50,y=50, width=500, height=400)

    #labels entry
    lblNumHabitacion = Label(marco, text="Numero Habitacion").grid(column=0,row=0 ,pady=5, padx=5)
    txtNumHabitacion = Entry(marco, textvariable= num_Habitacion)
    txtNumHabitacion.grid(column=1, row=0)
    lblEstHabitacion = Label(marco, text="Estado Habitacion").grid(column=0,row=1, pady=5, padx=5)
    txtEstHabitacion = ttk.Combobox(marco, values=["Disponible","Ocupado"] ,textvariable= estado_Habitacion)
    txtEstHabitacion.grid(column=1, row=1)
    txtEstHabitacion.current(0)
    lblCapacidad = Label(marco, text="Capacidad").grid(column=2,row=0, pady=5, padx=5)
    txtCapacidad = Entry(marco, textvariable= capacidad)
    txtCapacidad.grid(column=3, row=0)
    lblPrecio = Label(marco, text="Precio").grid(column=2,row=1, pady=5, padx=5)
    txtPrecio = Entry(marco, textvariable= precio)
    txtPrecio.grid(column=3, row=1)
    lblmensaje = Label(marco, text="aqui van los mensajes", fg="green")
    lblmensaje.grid(column=0,row=2,columnspan=4)

    # tabla lista de --

    tvHabitaciones= ttk.Treeview(marco, selectmode=NONE)
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
    tvHabitaciones.bind("<<TreeviewSelect>>",seleccionar)

    # BOTONES DE ACCION
    btneliminar= Button(marco, text="Eliminar", command=lambda:eliminar())
    btneliminar.grid(column=1,row=4)
    btnNuevo= Button(marco, text="Guardar",command=lambda:nuevo())
    btnNuevo.grid(column=2,row=4)
    btnModificar= Button(marco, text="Seleccionar", command=lambda:actualizarhabitaciones())
    btnModificar.grid(column=3,row=4)
    
    #funciones
    def modificarFalse():
        global modificar
        modificar = False
        tvHabitaciones.config(selectmode=NONE)
        btnNuevo.config(text="Guardar")
        btnModificar.config(text="Seleccionar")
        btneliminar.config(state=DISABLED)
                
    def modificarTrue():
        global modificar
        modificar = True
        tvHabitaciones.config(selectmode=BROWSE)
        btnNuevo.config(text="Nuevo")
        btnModificar.config(text="Modificar")
        btneliminar.config(state=NORMAL)

    def validar():
        return len(num_Habitacion.get()) and len(capacidad.get()) and len(precio.get()) 

    def limpiar():
        num_Habitacion.set("")
        capacidad.set("")
        precio.set("")
      
    def vaciar_tabla():
        filas = tvHabitaciones.get_children()
        for fila in filas:
            tvHabitaciones.delete(fila)

    def llenarTabla():
        vaciar_tabla()
        sql = "select * from habitaciones"
        cursor.execute(sql)
        filas=cursor.fetchall()
        for fila in filas:
            Num= fila[0]
            tvHabitaciones.insert("", END, Num, text= Num, values=fila )
                                 
    def eliminar():
        num= tvHabitaciones.selection()[0]
        if int(num)>0:
            sql="delete from habitaciones where Numero_habitacion="+num
            cursor.execute(sql)
            db.commit()
            tvHabitaciones.delete(num)
            lblmensaje.config(text="se ha eliminado correctamente")
        else:
            lblmensaje(text="Seleccione un registro para eliminar", fg="red")

    def nuevo():
        if modificar==False:
            if validar():
                val= [num_Habitacion.get(),estado_Habitacion.get(),capacidad.get(),precio.get()]
                sql= "INSERT INTO habitaciones (Numero_habitacion, Estado_habitacion, Capacidad, Precio) VALUES ('{}','{}','{}','{}')".format(val[0],val[1],val[2],val[3])
                cursor.execute(sql)
                db.commit()
                lblmensaje.config(text="Se ha guardado un registro correctamente", fg="green")
                llenarTabla()
                limpiar()
            else:
                lblmensaje.config(text="Los campos no deben estar vacios", fg="red")
        else:
            modificarFalse()
        
    def actualizarhabitaciones():
        if modificar==True:
            if validar():
                sql= "UPDATE habitaciones SET Estado_habitacion='"+txtEstHabitacion.get()+"', Capacidad='"+txtCapacidad.get()+"', Precio='"+txtPrecio.get()+"' WHERE Numero_habitacion="+num_Habitacion.get()
                cursor.execute(sql)
                db.commit()
                lblmensaje.config(text="Se ha actualizado correctamente", fg="green")
                llenarTabla()
                limpiar()
            else:
                lblmensaje.config(text="Los campos no deben estar vacios", fg="red")
        else:
            modificarTrue()
    llenarTabla()
    ventanaHabitaciones.mainloop()
    

def registroReservas():
    
    ventanaReservas=Toplevel()
    ventanaReservas.title("Registro de reservas")
    ventanaReservas.geometry("800x600")

    modificar = False
    registro_reservas= StringVar()
    rut_cliente= StringVar()
    num_habitacion=StringVar()
    id_empleado=StringVar()
    fecha=StringVar()
                
    def seleccionar(event):
        num= tvReservas.selection()[0]
        if int(num)>0:
            registro_reservas.set(tvReservas.item(num,"values")[0])
            rut_cliente.set(tvReservas.item(num,"values")[1])
            num_habitacion.set(tvReservas.item(num,"values")[2])
            id_empleado.set(tvReservas.item(num,"values")[3])
            fecha.set(tvReservas.item(num,"values")[4])
            
    marco = ttk.LabelFrame(ventanaReservas, text="Formulario de gestion Estudiantes")
    marco.place(x=50,y=50, width=700, height=400)


    def mostraridEmpleados():
        eje = cursor.execute('select ID_Empleado  from empleados')
        eje = cursor.fetchall()
        result = []
        for row in eje:
            result.append(row[0])
        return result
    #obtiene los RUT clientes que existen en la base de datos
    def mostrarrutClientes():
        eje = cursor.execute('select RUT_cliente from Clientes')
        eje = cursor.fetchall()
        result = []
        for row in eje:
            result.append(row[0])
        return result
    #obtiene los num de habitaciones que existen en la base de datos
    def mostrarnumhabitaciones():
        eje = cursor.execute('select Numero_habitacion from habitaciones')
        eje = cursor.fetchall()
        result = []
        for row in eje:
            result.append(row[0])
        return result


    #labels entry
    lblRegReservas= Label(marco, text="Registro Reservas").grid(column=0,row=0 ,pady=5, padx=5)
    txtRegReservas = Entry(marco, textvariable= registro_reservas)
    txtRegReservas.grid(column=1, row=0)

    lblRutCliente = Label(marco, text="rut cliente").grid(column=0,row=1, pady=5, padx=5)
    txtRutCliente  = ttk.Combobox(marco ,textvariable= rut_cliente)
    txtRutCliente ['value'] = mostrarrutClientes()
    txtRutCliente .grid(column=1, row=1)
    txtRutCliente .current(0)

    lblNumHabitacion = Label(marco, text="num_habitacion").grid(column=2,row=0, pady=5, padx=5)
    txtNumHabitacion= ttk.Combobox(marco, textvariable= num_habitacion)
    txtNumHabitacion['value'] = mostrarnumhabitaciones()
    txtNumHabitacion.grid(column=3, row=0)
    txtNumHabitacion.current(0)

    lblIdEmpleado = Label(marco, text="id_empleado").grid(column=2,row=1, pady=5, padx=5)
    txtIdEmpleado = ttk.Combobox(marco, textvariable= id_empleado)
    txtIdEmpleado['value'] = mostraridEmpleados()
    txtIdEmpleado.grid(column=3, row=1)
    txtIdEmpleado.current(0)

    lblFecha = Label(marco, text="fecha").grid(column=4,row=0, pady=5, padx=5)
    txtFecha=ttk.Combobox(marco, text="fecha",values=[datetime.today().strftime('%Y-%m-%d')])
    txtFecha.grid(column=5, row=0)
    txtFecha.current(0)

    lblmensaje = Label(marco, text="aqui van los mensajes", fg="green")
    lblmensaje.grid(column=0,row=2,columnspan=4)

        # tabla lista de --

    tvReservas= ttk.Treeview(marco, selectmode=NONE)
    tvReservas.grid(column=0, row=3, columnspan=6)
    lblregistroreservas =Label(ventanaReservas, text="Registro Reservas", fg="red", font=(None, 30)).place(x=250, y=5)
    tvReservas["columns"]=("Registro Reservas","RUT cliente", "Num habitaciones", "ID empleado","Fecha")
    tvReservas.column('#0', width=0, stretch=NO)
    tvReservas.column("Registro Reservas", width=150, anchor=CENTER)
    tvReservas.column("RUT cliente", width=150, anchor=CENTER)
    tvReservas.column("Num habitaciones", width=90, anchor=CENTER)
    tvReservas.column("ID empleado", width=90, anchor=CENTER)
    tvReservas.column("Fecha", width=90, anchor=CENTER)
    tvReservas.heading('#0', text="")
    tvReservas.heading('Registro Reservas', text='Registro Reservas', anchor=CENTER )
    tvReservas.heading('RUT cliente', text='RUT cliente', anchor=CENTER )
    tvReservas.heading('Num habitaciones',text='Num habitaciones', anchor=CENTER )
    tvReservas.heading('ID empleado',text='ID empleado', anchor=CENTER)
    tvReservas.heading('Fecha',text='Fecha', anchor=CENTER)
    tvReservas.bind("<<TreeviewSelect>>",seleccionar)

        # BOTONES DE ACCION
    btneliminar= Button(marco, text="Eliminar", command=lambda:eliminar())
    btneliminar.grid(column=1,row=4)
    btnNuevo= Button(marco, text="Guardar",command=lambda:nuevo())
    btnNuevo.grid(column=2,row=4)
    btnModificar= Button(marco, text="Seleccionar", command=lambda:actualizarhabitaciones())
    btnModificar.grid(column=3,row=4)
        
        #funciones
    def modificarFalse():
        global modificar
        modificar = False
        tvReservas.config(selectmode=NONE)
        btnNuevo.config(text="Guardar")
        btnModificar.config(text="Seleccionar")
        btneliminar.config(state=DISABLED)
                    
    def modificarTrue():
        global modificar
        modificar = True
        tvReservas.config(selectmode=BROWSE)
        btnNuevo.config(text="Nuevo")
        btnModificar.config(text="Modificar")
        btneliminar.config(state=NORMAL)

    def validar():
        return len(registro_reservas.get()) and len(rut_cliente.get()) and len(num_habitacion.get()) 

    def limpiar():
        registro_reservas.set("")

        
    def vaciar_tabla():
        filas = tvReservas.get_children()
        for fila in filas:
            tvReservas.delete(fila)

    def llenarTabla():
        vaciar_tabla()
        sql = "select * from reservas"
        cursor.execute(sql)
        filas=cursor.fetchall()
        for fila in filas:
            Num= fila[0]
            tvReservas.insert("", END, Num, text= Num, values=fila )
                                    
    def eliminar():
        num= tvReservas.selection()[0]
        if int(num)>0:
            sql="delete from reservas where ID_reserva="+num
            cursor.execute(sql)
            db.commit()
            tvReservas.delete(num)
            lblmensaje.config(text="se ha eliminado correctamente")
        else:
            lblmensaje(text="Seleccione un registro para eliminar", fg="red")

    def nuevo():
        if modificar==False:
            if validar(): 
                val= [registro_reservas.get(),rut_cliente.get(),num_habitacion.get(),id_empleado.get(),fecha.get()]
                sql= "INSERT INTO reservas (ID_reserva, RUT_cliente, Numero_habitacion, ID_empleado,fecha) VALUES ('{}','{}','{}','{}','{}')".format(val[0],val[1],val[2],val[3],val[4])
                cursor.execute(sql)
                db.commit()
                lblmensaje.config(text="Se ha guardado un registro correctamente", fg="green")
                llenarTabla()
                limpiar()
            else:
                lblmensaje.config(text="Los campos no deben estar vacios", fg="red")
        else:
            modificarFalse()
        

    def actualizarhabitaciones():
        if modificar==True:
            sql= "UPDATE reservas SET ID_reserva='"+rut_cliente.get()+"', Numero_habitacion='"+num_habitacion.get()+"', ID_empleado='"+id_empleado.get()+"', fecha='"+fecha.get()+"' WHERE ID_reserva="+registro_reservas.get()

            cursor.execute(sql)
            db.commit()
            lblmensaje.config(text="Se ha actualizado correctamente", fg="green")
            llenarTabla()
            limpiar()

            lblmensaje.config(text="Los campos no deben estar vacios", fg="red")
        else:
            modificarTrue()
    llenarTabla()
    ventanaReservas.mainloop()

   


#Ventana login principal!
def app():
    ventana = tk.Tk()
    ventana.title("Hotel")
    ventana.geometry("500x200")
    ventana.configure(background="white")
    #Imagenes logos !
  
    #iconImg = tkinter.PhotoImage(file="img\imgLogin\iconLogo.png")
    #lbl_img = tkinter.Label(ventana, image=iconImg).place(y=40, x=-15)
    #iconTilte = tkinter.PhotoImage(file="img\imgLogin\iconTitle.png")
    #lbl_Title = tkinter.Label(ventana, image=iconTilte).place(y=15, x=2)   
    #iconLogin = tkinter.PhotoImage(file="img\imgLogin\iconLogin.png")
    #lbl_Login = tkinter.Label(ventana, image=iconLogin).place(y=448, x=110)

    #Botones Inicio   
    #btnIngresar = tk.Button(ventana, text="Iniciar sesion", fg="black", bg="green",command=login)#Falta agregar la accion del command
    #btnIngresar.place(x=150, y=445, width=200, height=30)

    btnRegistrarEmpleado = tk.Button(ventana, text="Registrar Empleado",fg="black", bg="green",command=RegistrarEmpleados)
    btnRegistrarEmpleado.place(x=150, y=30, width=200, height=30)

    #insertar en otra ventana o donde sea convenientes es solo de pruebas
    btnRegistrarCliente = tk.Button(ventana, text="Registar Cliente", fg="black", bg="green",command=registarClientes)
    btnRegistrarCliente.place(x=150, y=70, width=200, height=30)

    # se agrega el boton de registrar habitacion de momento lo pondré aqui para hacer las pruebas correspondientes
    btnRegistrarHabitacion = tk.Button(ventana, text="Registar Habitación", fg="black", bg="green",command=regitrarHabitaciones)
    btnRegistrarHabitacion.place(x=150, y=110, width=200, height=30)

    btnRegistroReservas= tk.Button(ventana, text="Registar Reservas", fg="black", bg="green",command=registroReservas)
    btnRegistroReservas.place(x=150, y=150, width=200, height=30)
    
    ventana.mainloop()


ventanaLogin = tk.Tk()
ventanaLogin.title("Login Hotel")
ventanaLogin.geometry("500x640")
ventanaLogin.configure(background="white")


iconImg = tkinter.PhotoImage(file="img\imgLogin\iconLogo.png")
lbl_img = tkinter.Label(ventanaLogin, image=iconImg).place(y=0, x=-15)
iconTilte = tkinter.PhotoImage(file="img\imgLogin\iconTitle.png")
lbl_Title = tkinter.Label(ventanaLogin, image=iconTilte).place(y=0, x=2)   

#Entradas Login
idEmpleado = tk.Label(ventanaLogin, text="Ingrese ID Empleado", bg="grey", fg="black")
idEmpleado.place(x=170, y=430, width=160, height=30)
entradaId = tk.Entry(ventanaLogin)
entradaId.place(x=150, y=470, width=200, height=30)
    
contraseña = tk.Label(ventanaLogin, text="Ingrese Contraseña", bg="grey", fg="black")
contraseña.place(x=170, y=510, width=160, height=30)
entradaContraseña = tk.Entry(ventanaLogin)
entradaContraseña.place(x=150, y=550, width=200, height=30)

def verificarDatos():
    id_verify = entradaId.get()
    contraseña_verify = entradaContraseña.get()
    cursor.execute("SELECT * FROM empleados WHERE ID_Empleado = '"+id_verify+"' AND Contraseña = '"+contraseña_verify+"' ")
    if cursor.fetchall():
        messagebox.showinfo(title="Login Correcto", message="[!] ID_Empleado y contraseña correctas")
        app()
    else:
        messagebox.showerror(title="Login Incorrecto", message="[X] ID_Empleado y contraseña Incorrecta !")
    cursor.close()
    
btnLogin = tk.Button(ventanaLogin, text="Logearse",fg="black", bg="green",command=verificarDatos)
btnLogin.place(x=150, y=600, width=200, height=30)

ventanaLogin.mainloop()

