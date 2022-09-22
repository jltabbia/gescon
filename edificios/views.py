from django.shortcuts import render, redirect
from django.views.generic import View
from modelos.models import Edificios
from usuarios.models import Usuario

# Create your views here.

def EdificiosHomeView(request):    
    user=request.user
    edificios=Edificios.objects.filter(administrador=user.id)
    return render(request, 'edificios/index.html',{'edificios':edificios})        

class AgregarView(View):
    def get(self,request,*args, **kwargs):
        
        usuarios=Usuario.objects.all()
        context={
            'usuarios':usuarios,
        }
        return render(request,'edificios/agregar.html',context)   

    def post(self,request,*args,**kwargs):
        user=request.user
        print(user)
        edificio=Edificios()
        edificio.nombre=request.POST.get('nombre')
        edificio.domicilio=request.POST.get('domicilio')
        edificio.administrador=user.id
        edificio.save()
        return redirect('edificios:home')
            
def eliminar(request, id):
    edificio=Edificios.objects.get(id=id)
    edificio.delete()
    
    return redirect('edificios:home')

def editar(request, id):
    
    edificio=Edificios.objects.get(id=id) 
    
    if request.method=="POST":

        edificio.nombre=request.POST.get('nombre')
        edificio.domicilio=request.POST.get('domicilio')
        edificio.save()
        return redirect('edificios:home')

    context = {
        'edificio':edificio,
    }
    return render(request, 'edificios/editar.html',context)  

