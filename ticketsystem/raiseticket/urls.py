from django.urls import path

from raiseticket import views

urlpatterns = [
    path("", views.create_customer, name="create_customer"),
    path('all-tickets', views.all_tickets_view, name='all-tickets'),
    path('settings', views.usersettings_update_view, name='settings'),
    path('ticket/<id>', views.ticket_view, name='ticket'),
    path('create-ticket/<customer_id>', views.create_ticket, name='create-ticket'),
    path('customer/<id>', views.customer_view, name='customer'),
    path('update-ticket/<id>', views.update_ticket, name='update-ticket'),
]