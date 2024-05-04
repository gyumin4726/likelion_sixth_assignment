from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def user_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'user_profile.html', {'profile': profile})

@login_required
def user_update(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()

        profile.nickname = request.POST['nickname']
        profile.image = request.FILES.get('profile_image')
        profile.save()

        messages.success(request, '프로필이 성공적으로 수정되었습니다.')
        return redirect('home')
    else:
        return render(request, 'home.html', {'profile': profile})

# 회원가입

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],)
            
            profile = Profile(
                user=user,
                nickname=request.POST['nickname'],
                image=request.FILES.get('profile_image'),)
            
            profile.save()
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# 로그인

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html')
    return render(request, 'login.html')

# 로그아웃

def logout(request):
    auth.logout(request)
    return redirect('home')