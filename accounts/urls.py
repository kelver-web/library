from django.urls import path
from . views import RegisterView, IndexView, UpdateUserView, PasswordUpdatView

app_name = 'accounts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('alterar-dados/', UpdateUserView.as_view(), name='update_user'),
    path('alterar-senha/', PasswordUpdatView.as_view(), name='update_password'),
]