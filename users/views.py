from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginform, UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False) # dont save it yet
        password = form.cleaned_data.get('confirm_password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('login')
    context = {
        'form': form,
    }
    return render(request, "register.html", context)

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginform(request.POST or None)
    if form.is_valid():
        username =  form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, "login.html", context)

@login_required
def profile(request):
    img_height = 100
    img_width = 512
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
        'u_form': u_form,
        'img_height': img_height,
        'img_width': img_width,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
