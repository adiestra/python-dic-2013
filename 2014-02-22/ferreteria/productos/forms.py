from django import forms
from django.utils.translation import ugettext as _
from productos.models import Producto

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(
        label=_(u'Nombre'),
        widget=forms.Textarea(attrs={'rows':5, 'cols':30})
    )
    
    class Meta:
        model = Producto
        exclude = ['id', 'fecha_creacion', 'fecha_modificacion']
        
        
    def save(self, *args, **kwargs):
        # Personalizar algo que necesiten
        return super(ProductoForm, self).save(*args, **kwargs)
