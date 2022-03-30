from django.shortcuts import redirect, render
from fruits.forms import FruitsForm
from fruits.models import Fruits
# Create your views here.

def home(request):
    data = {}
    data['db'] = Fruits.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = FruitsForm()
    return render(request, 'form.html', data)

def create(request):
    form = FruitsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Fruits.objects.get(pk=pk)
    return render(request, 'view.html', data)