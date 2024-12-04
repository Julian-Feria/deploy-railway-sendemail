from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
from django.shortcuts import render, redirect

# from .models import EmailsData
from django.core.files.storage import default_storage


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Realiza una solicitud POST a /token/login/ para obtener el token JWT
        response = requests.post(
            f"{request.build_absolute_uri('/token/login/')}",
            data={'email': email, 'password': password},
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        
        if response.status_code == 200:
            # Autenticación exitosa, obtener tokens
            tokens = response.json()
            access_token = tokens.get('access')
            refresh_token = tokens.get('refresh')
            
            # Guardar tokens en la sesión
            request.session['access_token'] = access_token
            request.session['refresh_token'] = refresh_token
            
            # Redirige a la página de inicio u otra vista deseada
            return redirect('emails_list')  
            # return render(request, "users/login.html")
        else:
            # Si las credenciales son inválidas, muestra un mensaje de error
            messages.error(request, "Credenciales inválidas. Inténtalo de nuevo.")
    
    return render(request, "users/login.html")
