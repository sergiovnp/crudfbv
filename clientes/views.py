from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from django.http import HttpResponse
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.views.generic import View



def lista(request):
    buscar = request.GET.get('buscar', None)

    if buscar:
        clientes = Cliente.objects.all()
        clientes = clientes.filter(apellido__icontains=buscar)
        cantidad = clientes.filter(apellido__icontains=buscar).count()

    else:
        clientes = Cliente.objects.all()
        cantidad = Cliente.objects.all().count()

    
    page = request.GET.get('page', 1)
    paginator = Paginator(clientes, 9)
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

    return render (request, "clientes/lista.html", {'clientes':clientes, 'cantidad':cantidad} )

def eliminar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista')

    return render(request, "clientes/eliminar.html", {'cliente':cliente})

def detalle(request, id):
    clientes = Cliente.objects.all()
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, "clientes/detalle.html", {'cliente':cliente, 'clientes':clientes})

def crear(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, "clientes/crear.html", {'form':form})

def editar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, "clientes/editar.html", {'form':form})
