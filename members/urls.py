
from django.urls import path
from . views import PasswordsChangeView
from . import views


urlpatterns = [

    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('changeProfileImage', views.changeProfileImage, name='changeProfileImage'),
    path('change_password', PasswordsChangeView.as_view(
        template_name='registration/change_password.html')),
    ###########################################################################################
    ################################# User Lists and Chat #####################################
    ###########################################################################################
    path('users_list', views.users, name='users_list'),
    path('chat', views.chat, name='chat'),
    path('mainchat/<int:id>', views.mainchat, name='mainchat'),


]
