from django.urls import path
from .views import BookListView, CategoryListView
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('livros/<slug:slug>/', views.book, name='book'),
]