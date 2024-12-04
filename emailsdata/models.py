from django.db import models

class EmailsData(models.Model):
      first_name = models.CharField(max_length=30, verbose_name='Primer nombre')
      last_name = models.CharField(max_length=30, verbose_name='Apellidos')
      email = models.EmailField(verbose_name='Correo')
      group = models.CharField(max_length=50, default='Group', verbose_name='Grupo')

      def __str__(self):
            return self.email
      
      class Meta:
            verbose_name = 'Email'  
            verbose_name_plural = 'Email' 
        