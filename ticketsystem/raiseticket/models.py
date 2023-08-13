from django.db import models
from django.contrib.auth.models import User

try:
    from django.utils import timezone
except ImportError:
    from datetime import datetime as timezone


def user_unicode(self):
    """
    return 'last_name, first_name' for User by default
    """
    return u'%s, %s' % (self.last_name, self.first_name)


User.__unicode__ = user_unicode


def attachment_path(instance, filename):
    """
    Provide a file path that will help prevent files being overwritten, by
    putting attachments in a folder off attachments for ticket/followup_id/.
    """
    import os
    from django.conf import settings
    os.umask(0)
    path = 'tickets/%s' 
    print(path)
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files. \
                                         storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)
    return os.path.join(path, filename)

class Customer (models.Model):
    
    
    fname = models.CharField('FirstName', max_length=200)
    lname = models.CharField('LastName', max_length=200)
    email = models.EmailField('Email', max_length=200,unique=True)
    dob=models.DateField()
    address=models.CharField('Address', max_length=200)
    city=models.CharField('City', max_length=200)
    pincode=models.IntegerField('Pincode')
    GENDER_CHOICES=(('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        
        ('OTHER','OTHER'))
    gender = models.CharField('Gender', choices=GENDER_CHOICES,
                              max_length=255,
                              blank=True,
                              null=True)
    class Meta:
        # ordering = ['filename', ]
        verbose_name = 'Customer'


class Ticket(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    #service types
    customer_id=Customer.pk
    SERVICE_CHOICES=(('START', 'START'),
        ('MOVE', 'MOVE'),
        ('STOP', 'STOP'),
        ('GAS LEAK', 'GAS LEAK'),
        ('OTHER','OTHER'))

    service = models.CharField('Service', choices=SERVICE_CHOICES,
                              max_length=255,
                              blank=True,
                              null=True)

    
#details
    details = models.TextField('Details', blank=True, null=True)
#service status
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('IN PROGRESS', 'IN PROGRESS'),
        
        ('DONE', 'DONE'),
    )
    status = models.CharField('Status',
                              choices=STATUS_CHOICES,
                              max_length=255,
                              blank=True,
                              null=True)

    waiting_for = models.ForeignKey(User,
                                    related_name='waiting_for',
                                    blank=True,
                                    null=True,
                                    verbose_name='Waiting For',on_delete=models.CASCADE)

    file = models.FileField('File',blank=True,
                                    null=True,
                            upload_to=attachment_path,
                            max_length=1000)

    filename = models.CharField('Filename',blank=True,
                                    null=True, max_length=1000)

    

   

    def get_upload_to(self, field_attname):
        """ Get upload_to path specific to this item """
        if not self.id:
            return u''
        return u'../media/tickets/%s' % (
            self.id,
        )
    # set in view when status changed to "DONE"
    closed_date = models.DateTimeField(blank=True, null=True)

    assigned_to = models.ForeignKey(User,related_name='assigned_to',
                                    blank=True,
                                    null=True,
                                    verbose_name='Assigned to',on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.id)
    

    



