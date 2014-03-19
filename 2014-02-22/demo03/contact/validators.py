from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

def non_free_email(value):
    DOMAIN_BLACKLIST = (
        'gmail.com',
        'hotmail.com',
        'outlook.com'
    )
    user, domain = value.split('@')
    if domain in DOMAIN_BLACKLIST:
        message = _(u'No aceptamos correos de %s' % domain)
        raise ValidationError(message)
