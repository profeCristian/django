from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Persona, Producto, Alumno
from . forms import Alumno as FormAlumno

# Create your views here.
'''
class Persona:
    #rut=""
    #nombre=""
    #edad=0

    def __init__(self,rut,nombre,edad):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad

    def getRut(self):
        return self.rut

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad    

    def toString(self):
        return self.rut+", "+self.nombre+", "+str(self.edad)


p1 =  Persona("1-1","Susana",22)
p2 =  Persona("2-2","Juan",19)
p3 = Persona("3-3","Sandra",20)
personas = [p1,p2,p3]
'''

def persona_crud(request):
    print("estoy en Persona Crud...")
    context={} 
    return render(request,"personas/personas_add.html",context)


def personasAdd(request):
    print("estoy en controlador PersonasAdd...")
    context={}
    if request.method == "POST":
        print("contralador es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Editar" or opcion == "Volver":
            personas = Persona.objects.all()
            context ={'personas':personas}
            print("enviando datoa personas_edit")
            return render(request,"personas/personas_list.html",context) 
        #Agregar
        if opcion=="Agregar":
            rut=request.POST["rut"]
            nombre=request.POST["nombre"]
            edad=request.POST["edad"]
       
            if rut != "" and nombre != "" and edad !="":
                persona = Persona(rut, nombre, edad) 
                persona.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           #Agregar
        if opcion=="Actualizar":
            rut=request.POST["rut"]
            nombre=request.POST["nombre"]
            edad=request.POST["edad"]
       
            if rut != "" and nombre != "" and edad !="":
                persona = Persona(rut, nombre, edad) 
                persona.save()
                context={'persona':persona,'mensaje':"Ok, datos actualizados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}
            return render(request,"personas/personas_edit.html",context) 


    return render(request,"personas/personas_add.html",context)   


def personas_del(request, pk):
    mensajes=[]
    errores=[]
    personas = Persona.objects.all()
    try:
        persona=Persona.objects.get(rut=pk)
        context={}
        if persona:
           persona.delete()
           mensajes.append("Bien, datos eliminados...")

           context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}

           return render(request, 'personas/personas_list.html', context)

    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'personal/personas_list.html', context)

def personas_edit(request, pk):
    mensajes=[]
    errores=[]
   
    
    context={}
    personas = Persona.objects.all()
    #try:
    persona=Persona.objects.get(rut=pk)

    context={}
    if persona:
        print("Edit encontró a persona...")
        mensajes.append("Bien, datos eliminados...")

        context = {'persona': persona,  'mensajes': mensajes, 'errores':errores}

        return render(request, 'personas/personas_edit.html', context)
    '''
    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'personas/personas_list.html', context)
    '''
    '''
    if jugador:
        form = FormJugador(request.POST or None,
                            request.FILES or None, instance=jugador)
        #form = FormJugador(instance=jugador)
        print("estoy en jugador true")
        if request.method == 'POST':
            print("ingresó al POST")
            #form = FormJugador(request.POST, request.FILES)
           # print("formulario id_persona: " + form.id_persona)
            if form.is_valid():
                print("is valid...")
                jugador = form.save()
                jugador.save()
                mensajes.append("Bien!, datos grabados...")
                print("Bien!, datos grabados...")
                accion = 'tabla'
                context = {'jugadores': jugadores, 'mensajes': mensajes,
                           'errores': errores, 'accion': accion}
            else:
                errores.append("Error!, datos no grabados...del EDIT")
                print("Error!, datos no grabados... form="+str(form.errors))
                accion='tabla'
                context = {'jugadores': jugadores, 'mensajes': mensajes,
                       'errores': errores, 'accion': accion}

            return render(request, 'personal/crud_jugador.html', context)
        else:
            mensajes.append("Bien!, id existe...")
            print("entró al else form=Jugador()...")
            accion = 'form_edit'
            context = {'jugadores': jugadores, 'mensajes': mensajes,
                       'errores': errores,'form':form, 'accion': accion}
    '''               
    return render(request, 'personas/personas_list.html', context)
    '''
    else:
        print("Error, id_jugador no existe")
        errores.append("Error id no encontrado.")
        accion='tabla'
        context = {'jugadores': jugadores,  'mensajes': mensajes,
                   'errores':errores,'accion':accion}
    return render(request, 'personal/crud_jugador.html', context)
    '''

def index(request):
    print("Hola estoy en index del views")

    dias =["lunes","martes","miércoles","jueves","viernes","sábado"]
  
    context={
             'nombre':'Cristián García',
             'carrera':'Analista Programador',
             'idJornada': 2,
             'dias': dias,
             
            }

    return render(request,"personas/index.html",context)

def sumar(request):
    print("estoy en sumar...")
    context={} 
    return render(request,"personas/suma.html",context)






def calcularSuma(request):
    print("estoy en calcular...")

    if request.method == "POST" :
       print("es un post...") 
       v1 = request.POST.get("valor1",'0')
       v2 = request.POST.get("valor2",'0')
       print(v1,"     ",v2)
       resultado = int(v1) + int(v2)

    context={'v1':v1, 'v2':v2,'resultado':resultado}   
    #return redirect(reverse('sumar') +"?"+str(resultado) )
    return render(request,"personas/suma.html",context)


def crud(request):
    print("estoy en crud...")
    context={}
    return render(request,"personas/crud.html",context)


def controlador(request):
    print("estoy en controlador...")
    context={}
    if request.method == "POST":
        print("contralador es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Listar":
           context={"personas":personas}
       
        #Buscar
        if opcion=="Buscar":
            rut=request.POST.get("rut","")
            if rut != "":
                for persona in personas:
                    print("entro al for con el rut ", rut)
                    if persona.getRut() == rut:
                        print("buscar encontro el rut")
                        context={'persona':persona}
                        break
            else:
                context={'mensaje':"Error, rut no debe estar vacio"}
        #Agregar
        if opcion == "Agregar":
             rut=request.POST.get("rut","")
             nombre=request.POST.get("nombre","")
             edad=int(request.POST.get("edad","0"))
            
             if rut != "" and nombre != "" and edad!="":
                nuevo = Persona(rut, nombre, edad) 
                if personas.append(nuevo) == None:
                    context={'mensaje':"Ok agregado"}
                else:
                    context={'mensaje':"Error, datos no agregado"}
             else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           
    return render(request,"personas/crud.html",context)

##################   P R O D U C T O S ######################
 
def productos_crud(request):
    print("estoy en Productos Crud...")
    context={} 
    return render(request,"personas/productos_add.html",context)

def productosAdd(request):
    print("estoy en controlador ProductosAdd...")
    context={}
    if request.method == "POST":
        print("contralador productos es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Editar" or opcion == "Volver":
            productos = Producto.objects.all()
            context ={'productos':productos}
            print("enviando datos a productos_list")
            return render(request,"personas/productos_list.html",context) 
        #Agregar
        if opcion=="Agregar":
            idProducto=request.POST["idProducto"]
            nombreProducto=request.POST["nombreProducto"]
            stock=int(request.POST["stock"])
            precio=int(request.POST["precio"])
            fotoProducto=request.FILES["fotoProducto"]

       
            if idProducto != "" and nombreProducto != "" and stock >=0 and precio >=0:

                producto = Producto(idProducto, nombreProducto, stock, precio,
                                    fotoProducto) 
                producto.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           #Agregar
        if opcion=="Actualizar":
            idProducto=request.POST["idProducto"]
            nombreProducto=request.POST["nombreProducto"]
            stock=int(request.POST["stock"])
            precio=int(request.POST["precio"])
            try:
                fotoProducto=request.FILES["fotoProducto"]
            except:
                fotoProducto=""
       
            if idProducto != "" and nombreProducto != "" and stock >=0 \
                and precio >=0:

                producto = Producto(idProducto, nombreProducto, stock, precio,
                                    fotoProducto) 
                producto.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}
            return render(request,"personas/productos_edit.html",context) 


    return render(request,"personas/productos_add.html",context)   

def productos_del(request, pk):
    mensajes=[]
    errores=[]
    productos = Producto.objects.all()
    try:
        producto=Producto.objects.get(idProducto=pk)
        context={}
        if producto:
           producto.delete()
           mensajes.append("Bien, datos eliminados...")

           context = {'productos': productos,  'mensajes': mensajes, 'errores':errores}

           return render(request, 'personas/productos_list.html', context)

    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'productos': productos,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'personal/productos_list.html', context)

def productos_edit(request, pk):
    mensajes=[]
    errores=[]
   
    
    context={}
    productos = Producto.objects.all()
    #try:
    producto=Producto.objects.get(idProducto=pk)

    context={}
    if producto:
        print("Edit encontró a producto...")
        mensajes.append("Bien, datos eliminados...")

        context = {'producto': producto,  'mensajes': mensajes, 'errores':errores}

        return render(request, 'personas/productos_edit.html', context)
    
    return render(request, 'personas/productos_list.html', context)
  



  #**********************  CRUD ALUMNO   ******************************

def crud_alumno(request):

    print("hola  estoy en crud_alumnos...")
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos,'accion': 'tabla'}
    return render(request, 'personas/crud_alumno.html', context)

def cargar_formulario_alumno(request):
    context = {}
    mensajes = []
    errores = []
    accion = 'tabla'
    if request.method == 'POST':
        print("Alumno Post")
        form = FormAlumno(request.POST or None, request.FILES or None)
        print("Alumno Post 2")
        if form.is_valid():
            print("Alumno Post is_valid")

            alumno = form.save()
            #alumno.save()
            mensajes.append("Bien!, datos grabados...")
            print("Bien!, datos grabados...")
            alumnos=Alumno.objects.all()
            context = {'form':form, 'mensajes': mensajes,'accion': accion,'alumnos':alumnos}
            return render(request,'personas/crud_alumno.html', context)
        else:
            errores.append( form)
            print("No pasó el is_valid ", form.is_valid())    

    else:
        print("Mostrando formulario alumno...")
        form = FormAlumno()
        accion = 'form_add'

    context = {'form':form, 'mensajes': mensajes,'accion': accion,'errores':errores}
    return render(request,'personas/crud_alumno.html', context)



def del_alumno(request, pk):
    mensajes=[]
    errores=[]
    alumnos = Alumno.objects.all()
    try:
        alumno=Alumno.objects.get(rut=pk)
        context={}
        if alumno:
           alumno.delete()
           mensajes.append("Bien, datos eliminados...")
           accion = 'tabla'
           context = {'alumnos': alumnos,  'mensajes': mensajes,'accion':accion, 'errores':errores}
           
           return render(request, 'personas/crud_alumno.html', context)

    except:
        print("Error, eliminar rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'alumnos': alumnos,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'personas/crud_alumno.html', context)


def editar_alumno(request, pk):
    mensajes=[]
    errores=[]
    alumnos = Alumno.objects.all()
    alumno =  get_object_or_404(Alumno, rut=pk)

    if alumno:
        form = FormAlumno(request.POST or None,
                            request.FILES or None, instance=alumno)
        #form = Formalumno(instance=alumno)
        print("estoy en alumno true")
        if request.method == 'POST':
            print("ingresó al POST")
            #form = Formalumno(request.POST, request.FILES)
           # print("formulario id_persona: " + form.id_persona)
            if form.is_valid():
                print("is valid...")
                alumno = form.save()
                alumno.save()
                mensajes.append("Bien!, datos grabados...")
                print("Bien!, datos grabados...")
                accion = 'tabla'
                context = {'alumnos': alumnos, 'mensajes': mensajes,
                           'errores': errores, 'accion': accion}
            else:
                errores.append("Error!, datos no grabados...del EDIT")
                print("Error!, datos no grabados... form="+str(form.errors))
                accion='tabla'
                context = {'alumnos': alumnos, 'mensajes': mensajes,
                       'errores': errores, 'accion': accion}

            return render(request, 'personas/crud_alumno.html', context)
        else:
            mensajes.append("Bien!, id existe...")
            print("entró al else form=alumno()...")
            accion = 'form_edit'
            context = {'alumnos': alumnos, 'mensajes': mensajes,
                       'errores': errores,'form':form, 'accion': accion}
            return render(request, 'personas/crud_alumno.html', context)

    else:
        print("Error, id_alumno no existe")
        errores.append("Error id no encontrado.")
        accion='tabla'
        context = {'alumnos': alumnos, 'mensajes': mensajes,
                   'errores': errores, 'accion':accion}
        return render(request, 'personas/crud_alumno.html', context)