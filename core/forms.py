from django import forms
from .models import Gallery
from django.core.validators import ValidationError


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'photo']

    def clean_image(self):
        image = self.cleaned_data.get('photo', False)
        if image:
            if image.__sizeof__ > 4*1024*1024:
                raise ValidationError('Imagem muito grande (maioro que 5mb)')
            return image
        else:
            raise ValidationError("Não pode abrir o arquivo de imagem")
            

