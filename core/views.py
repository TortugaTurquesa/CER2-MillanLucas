from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import LugarPatrimonial, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Inicia sesión automáticamente tras registrarse
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})

@login_required
def home(request):
    lugares_recientes = LugarPatrimonial.objects.all().order_by('-id')[:4]
    categorias = Categoria.objects.all()
    return render(request, 'core/home.html', {'lugares': lugares_recientes, 'categorias': categorias})

@login_required
def catalogo(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    if categoria_id:
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
    else:
        lugares = LugarPatrimonial.objects.all()
    return render(request, 'core/catalogo.html', {'lugares': lugares, 'categorias': categorias, 'selected_categoria': categoria_id})

@login_required
def detalle_lugar(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, pk=lugar_id)
    return render(request, 'core/detalle_lugar.html', {'lugar': lugar})

# Área de gestión protegida (RF10, RF11, RF12)
@login_required
@user_passes_test(lambda u: u.is_staff) # Solo usuarios con acceso al admin / staff
def gestion_lugares(request):
    lugares = LugarPatrimonial.objects.all()
    return render(request, 'core/gestion_lugares.html', {'lugares': lugares})

@login_required
@permission_required('core.add_lugarpatrimonial', raise_exception=True)
def agregar_lugar(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        ubicacion = request.POST.get('ubicacion')
        anio_construccion = request.POST.get('anio_construccion')
        imagen = request.POST.get('imagen')
        categoria_id = request.POST.get('categoria')
        nueva_categoria_nombre = request.POST.get('nueva_categoria')

        # Si el usuario escribió una categoría nueva, la creamos al instante
        if nueva_categoria_nombre and nueva_categoria_nombre.strip():
            cat, _ = Categoria.objects.get_or_create(
                nombre=nueva_categoria_nombre.strip(),
                defaults={'descripcion': f'Categoría {nueva_categoria_nombre}'}
            )
            categoria_id = cat.id
        
        LugarPatrimonial.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            ubicacion=ubicacion,
            anio_construccion=anio_construccion,
            imagen=imagen,
            categoria_id=categoria_id
        )
        return redirect('gestion_lugares')
    return render(request, 'core/agregar_lugar.html', {'categorias': categorias})

@login_required
@permission_required('core.change_lugarpatrimonial', raise_exception=True)
def editar_lugar(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, pk=lugar_id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        lugar.nombre = request.POST.get('nombre')
        lugar.descripcion = request.POST.get('descripcion')
        lugar.ubicacion = request.POST.get('ubicacion')
        lugar.anio_construccion = request.POST.get('anio_construccion')
        lugar.imagen = request.POST.get('imagen')
        
        categoria_id = request.POST.get('categoria')
        nueva_categoria_nombre = request.POST.get('nueva_categoria')

        if nueva_categoria_nombre and nueva_categoria_nombre.strip():
            cat, _ = Categoria.objects.get_or_create(
                nombre=nueva_categoria_nombre.strip(),
                defaults={'descripcion': f'Categoría {nueva_categoria_nombre}'}
            )
            lugar.categoria = cat
        elif categoria_id:
            lugar.categoria_id = categoria_id

        lugar.save()
        return redirect('gestion_lugares')
    return render(request, 'core/editar_lugar.html', {'lugar': lugar, 'categorias': categorias})

@login_required
@permission_required('core.delete_lugarpatrimonial', raise_exception=True)
def eliminar_lugar(request, lugar_id):
    lugar = get_object_or_404(LugarPatrimonial, pk=lugar_id)
    if request.method == 'POST':
        lugar.delete()
        return redirect('gestion_lugares')
    return render(request, 'core/eliminar_lugar.html', {'lugar': lugar})

