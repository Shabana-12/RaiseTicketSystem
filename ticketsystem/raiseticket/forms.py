from django import forms
from django.contrib.auth.models import User

from .models import Ticket,Customer


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
    
        fields = ('service', 'details','file','customer')
class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
    
        fields = ('id',
                    'service',
                    'details',
                    'assigned_to',
                    'status'
                    
                    )       
    



class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('fname', 'lname', 'email', 'dob','address','city','pincode','gender')

