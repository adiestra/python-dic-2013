# -*- coding: utf8 -*-

from django import forms
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
from django.conf import settings
from contact.validators import non_free_email

class ContactForm(forms.Form):
    subject = forms.CharField(
        label=_(u'Asunto'),
        max_length=100
    )
    
    message = forms.CharField(
        label=_(u'Mensaje'),
        widget=forms.Textarea(attrs={'rows':5, 'cols':30})
    )
    
    sender = forms.EmailField(
        label=_(u'Remitente'),
        error_messages={'required': 'El remitente es un campo obligatorio.'},
        validators=[non_free_email]
    )
    
    cc_myself = forms.BooleanField(
        label=_(u'Enviar copia al remitente'),
        required=False
    )
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_lines = len(message.split('\n'))
        if num_lines < 3:
            message = _(u'El mensaje debe tener 3 o más líneas')
            raise forms.ValidationError(message)
        return message
        
    def send_email(self):
        recipients = [settings.DEFAULT_TO_EMAIL]
        if self.cleaned_data['cc_myself']:
            recipients.append(self.cleaned_data['sender'])
        send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            settings.DEFAULT_FROM_EMAIL, 
            recipients, 
            fail_silently=False
        )
        return True
