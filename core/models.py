from django.db import models

class Gallery(models.Model):
    title = models.CharField('Título', max_length=100, blank=True)
    photo = models.ImageField('Galeria', upload_to='galeria', blank=True, null=True)

    class Meta:
    	verbose_name = 'Foto'
    	verbose_name_plural = 'Fotos'
    	
    def __str__(self):
        return self.title
   