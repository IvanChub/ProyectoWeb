from config.wsgi import *
from container.erp.models import Type

#consultar tabla  select * from tabla
#query = Type.objects.all()
#print(query)

#insertar
#t = Type()
#t= Type(name='prueba2').save()

#editar
#t= Type.objects.get(id=7)
#t.name = 'Presidente2020'
#t.save()

#eliminar
#t= Type.objects.get(pk=7)
#t.delete()

#try catch para pruebas de error con mensaje
try:
    t= Type.objects.get(id=7)
    t.name = 'Presidente2020'
    t.save()
except Exception as e:
    print(e)
