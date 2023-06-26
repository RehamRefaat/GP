from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', loginpage, name="login"),
    path('logout/', logoutpage, name="logout"),
    path('register/', register,name="register"),
    path('home/', home_page,name='home'),
    path('about/', about_page, name='about'),

    path('services/', services_page, name='services'),
    path('OCT-service/options/using-model/', OCT_subservices_page, name='subser'),
    path('OCT-service/options/using-model/New/', OCT_subservicesnew_page, name='subsernew'),

    path('OCT-service/options/using-model/message', Message_OCT_page, name='message'),
    path('OCT-service/options/', OCT_options_page, name='opt'),
    path('OCT-service/options/steps/', OCT_steps_page, name='steps'),

    path('Macula-service/options/', Macula_options_page, name='opt2'),
    path('Macula-service/options/using-model/', Macula_subservices_page, name='subser2'),
    path('Macula-service/options/using-model/message', Message_Macula_page, name='message2'),
    path('Macula-service/options/steps/', Macula_steps_page, name='steps2'),

    path('contact/', contact_page, name='contact'),
    path('account/', account_page, name='acc'),
    path('account/editprofile', edit_page, name='edit'),
    path('account/changepassword', change_page, name='change'),
    path('account/more-details/<int:pk>', details_page, name='det'),


]