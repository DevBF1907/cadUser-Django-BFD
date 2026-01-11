from django.shortcuts import render, redirect
from .forms import UsuarioForm

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})
