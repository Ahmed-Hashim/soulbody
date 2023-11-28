from django.urls import path
from . import views

urlpatterns = [
    ###################################################################
    ########################### List URLS #############################
    ###################################################################
    path('customerlist', views.customerlist,name='customerlist'),
    path('list', views.Customerlistview,name='crm_list'),    
    path('listing', views.customerlist,name='listing'),
    ###################################################################
    ########################### CRUD URLS #############################
    ###################################################################
    path('add_client', views.AddClient,name='add_client'),
    path('delete_client/p=<int:id>', views.deleteClient,name='delete_client'),
    path('view_edit_customer/p=<int:id>', views.view_edit_customer,name='view_edit_customer'),
    path('veiw_client/p=<int:id>', views.veiw_client,name='veiw_client'),
    path('add_customer/', views.add_customer,name='add_customer'),    
    path('view_add_contact/p=<int:id>', views.view_add_contact,name='view_add_contact'),    
    path('delete_contact/p=<int:id>', views.delete_contact,name='delete_contact'),    
   
    ###################################################################
    ########################### Email URLS ############################
    ###################################################################
    path('emails/p=<int:id>', views.emails,name='emails'),
    path('show_email/p=<int:id>', views.show_email,name='show_email'),
    path('send_whatsapp/p=<int:id>', views.send_whatsapp,name='send_whatsapp'),
    path('whatsapp/p=<int:id>', views.whatsapp,name='whatsapp'),
    ###################################################################
    ########################### Random URLS ###########################
    ###################################################################
    path('json/', views.customerlist_json,name='customerlist_json'),
    path('toast/', views.toast,name='toast'),
    ###################################################################
    ###################### Client Profile URLS ########################
    ###################################################################
    path('client_profile/p=<int:id>', views.client_profile,name='client_profile'),
    path('client_emails/p=<int:id>', views.client_emails,name='client_emails'),
    path('client_notes/p=<int:id>', views.client_notes,name='client_notes'),
    path('profile_data/p=<int:id>', views.profile_data,name='profile_data'),
    path('client_products/p=<int:id>', views.client_products,name='client_products'),
    path('client_invoice/p=<int:id>', views.client_invoice,name='client_invoice'),
    path('show_note/p=<int:id>', views.show_note,name='show_note'),
    path('add_note/p=<int:id>', views.add_note,name='add_note'),
    ###################################################################
    ###################### Send Whatsapp Template URLS ################
    ###################################################################
    path('whatsapp_settings', views.whatsapp_settings,name='whatsapp_settings'),
    path('Whatsapp_Temp', views.Whatsapp_Temp,name='Whatsapp_Temp'),
    path('send_template', views.send_template,name='send_template'),
    path('add_wapp_temp_model', views.add_wapp_temp_model,name='add_wapp_temp_model'),
    path('show_temp/<int:id>', views.show_temp,name='show_temp'),
    path('edit_temp/<int:id>', views.edit_temp,name='edit_temp'),
    path('delete_temp/<int:id>', views.delete_temp,name='delete_temp'),
    path('temps_listing', views.temps_listing,name='temps_listing'),
    path('send_show_temp_whatsapp', views.send_show_temp_whatsapp,name='send_show_temp_whatsapp'),
    path('send_to_customer', views.send_to_customer,name='send_to_customer'),

]