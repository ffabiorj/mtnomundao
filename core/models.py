from django.db import models

class Photo(models.Model):
    title = models.CharField('Title', max_length=100, blank=True)
    galery_photos = models.ImageField('Galeria', upload_to='galeria', blank=True, null=True)

    def __str__(self):
        return self.title
    