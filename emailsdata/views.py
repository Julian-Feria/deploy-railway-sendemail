import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EmailsData

def emails_list(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]
        try:
            df = pd.read_excel(excel_file)
            if 'email' not in df.columns:
                messages.error(request, "El archivo debe contener una columna 'email'.")
                return redirect("emails_list")
            for index, row in df.iterrows():
                email = row['email']
                EmailsData.objects.get_or_create(email=email)           
            messages.success(request, "Los datos han sido cargados exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al procesar el archivo: {e}")       
        return redirect("emails_list")
    emails = EmailsData.objects.all()
    return render(request, "emailsdata/emails_list.html", {"emails": emails})
