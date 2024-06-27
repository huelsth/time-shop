from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import TimeModel, Booking, CustomerProfile
from .forms import BookingForm

def home(request):
    time_models = TimeModel.objects.all()
    return render(request, 'shop/home.html', {'time_models': time_models})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def book_time(request, time_model_id):
    time_model = TimeModel.objects.get(id=time_model_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.time_model = time_model
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'shop/book_time.html', {'form': form, 'time_model': time_model})
