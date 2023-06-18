from os import path
#Libreria
from notifypy import Notify

#Objeto
notificacion = Notify()
notificacion.title = "Recetario XiKi"
notificacion.message= "Retire sus medicamentos!"
icono="Ca.png"
direccion = path.abspath(path.dirname(__file__))
notificacion.icon = path.join(direccion, icono)

notificacion.send ()