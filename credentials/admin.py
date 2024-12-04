from datetime import timedelta
from django.utils.timezone import now
from django.contrib import admin
from .models import Credentials

class CredentialsAdmin(admin.ModelAdmin):
    list_display = ('name_account', 'email_account', 'is_active', 'emails_sent_today', 'time_until_reset')
    
    readonly_fields = ('emails_sent_today', 'last_reset')

    def get_readonly_fields(self, request, obj=None):
        """Evita que los campos de solo lectura se modifiquen también durante la creación."""
        if obj:  
            return self.readonly_fields
        return self.readonly_fields + ('emails_sent_today', 'last_reset')  

    def time_until_reset(self, obj):
        """Calcula y muestra el tiempo restante para el próximo reinicio en el panel admin."""
        next_reset = obj.last_reset + timedelta(days=1)
        remaining_time = next_reset - now()
        if remaining_time.total_seconds() > 0:
            return str(remaining_time).split(".")[0]  
        return "Reinicio en proceso"

    time_until_reset.short_description = "Tiempo hasta reinicio"

    def save_model(self, request, obj, form, change):
        """Asegura que los campos por defecto se asignen automáticamente durante la creación."""
        if not change:  
            obj.emails_sent_today = 0
            obj.last_reset = now()
        super().save_model(request, obj, form, change)

admin.site.register(Credentials, CredentialsAdmin)