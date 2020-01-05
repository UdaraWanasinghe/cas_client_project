from django.shortcuts import render


def render_home(request):
    user_type = type(request.user)
    return render(request, 'home.html', {'user': request.user, 'user_type': user_type})
