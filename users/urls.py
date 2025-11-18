from django.urls import path , include
from  .views import create_accounts , login_view, change_password ,logout_view

urlpatterns = [
    path('create/account/', create_accounts, name='create_account'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('change/password/' ,change_password, name='change_password'),

]