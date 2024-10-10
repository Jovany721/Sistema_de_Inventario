from django.shortcuts import render,redirect
from .models import Productos
# Create your views here.


def HOME(request):
    return render(request, 'index.html')

def Consulta(request):
    datos = Productos.objects.all()
    return render(request, 'Consulta.html', {"datos":datos})





def eliminar_reg(request, producto):
    producto_a_eliminar = Productos.objects.get(producto=producto                )
    producto_a_eliminar.delete()
    return redirect('/consulta')


def search_bd(request, producto):
    producto_a_eliminar = Productos.objects.filter(producto=producto                )

    return redirect('/consulta')


