from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def registerUser(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Kayıt işleminiz başarıyla gerçekleştildi, ana sayfaya yönlendirildiniz..")


        return redirect("index")

    context = dict(
        form=form
    )

    return render(request, "register.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Çıkış işleminiz başarıyla gerçekleştirildi, Ana Sayfa'ya yönlendirildiniz..")
    return redirect("index")


def loginUser(request):

    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)
        if user is None:
            messages.warning(request, "Kullanıcı adı veya parola hatalı. Lütfen bilgilerinizi kontrol edip tekrar deneyiniz yada üye ol butonuna tıklayarak üye olunuz...")    

            return render(request, 'login.html', context)
        messages.success(request, "Giriş işleminiz başarıyla gerçekleşti. Ana sayfaya yönlendirildiniz..")
        login(request, user)
        return redirect("index")
    return render(request, 'login.html', context)
