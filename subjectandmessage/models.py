from django.db import models

class SubjectAndMessage(models.Model):
    subject = models.TextField(verbose_name='Asunto')
    message = models.TextField(verbose_name='Mensaje')

    def __str__(self):
            return self.subject
      
    class Meta:
            verbose_name = 'Asunto y Mensaje'  
            verbose_name_plural = 'Asunto y Mensaje' 
        
