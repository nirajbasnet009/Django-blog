from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method =='POST':
       form = UserRegisterForm(request.POST)
       print('posted')
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request,f'Account Successfully Created for {username} Login Now!'.format(username=username))
           return redirect('Login')
    else:         
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Profile is Updated!')
            redirect("profile")

    else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            context = {
                'u_form': u_form,
                'p_form': p_form,
            }
            return render(request, 'users/profile_update.html',context)

    return render(request, 'users/profile_update.html')