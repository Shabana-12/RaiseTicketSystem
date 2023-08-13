
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import Http404

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail

from .models import Ticket,Customer
from .forms import UserSettingsForm
from .forms import TicketCreateForm,CustomerForm,TicketUpdateForm

# Logging
import logging
logger = logging.getLogger(__name__)



def ticket_view(request, id):
    # dictionary for initial data with
    # field names as keys
    
    try:
        context ={}
        context["data"]= Ticket.objects.get(id =id)
        
    except Ticket.DoesNotExist:
        raise Http404('Data does not exist')
 
    return render(request, "my-tickets.html", context)


def usersettings_update_view(request):
    # dictionary for initial data with
    # field names as keys
    
    context ={}
 
    # add the dictionary during initialization
    form = UserSettingsForm(request.POST or None)
    
    
    
    if form.is_valid():
        
        form.save()
         
    context['form']= form
        
    return render(request, "settings.html", context)




def all_tickets_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Ticket.objects.all()
         
    return render(request, "all-tickets.html", context)


def create_ticket(request,customer_id):
    # dictionary for initial data with
    # field names as keys
   
    
    customer_id= Customer.objects.get(id=customer_id)
    
    context ={}
 
    # add the dictionary during initialization
    form = TicketCreateForm(request.POST)
    if form.is_valid():
        # obj.customer_id=customer_id
        obj = form.save()
        # set owner
        
        obj.status = "PENDING"
        obj.customer_id=customer_id
        obj.save()
        
         
    context['form']= form
        
    return render(request, "create_ticket.html", context)


def create_customer(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        
        form.save()
        
         
    context['form']= form
        
    return render(request, "create_customer.html", context)





def customer_view(request, id):
    # dictionary for initial data with
    # field names as keys
    
    try:
        context ={}
        context["data"]= Customer.objects.get(id =id)
        
    except Customer.DoesNotExist:
        raise Http404('Data does not exist')
 
    return render(request, "show_customer.html", context)

def update_ticket(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Ticket, id = id)
 
    # pass the object as instance in form
    form =TicketUpdateForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/ticket/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_ticket.html", context)