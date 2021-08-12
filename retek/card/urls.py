from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('card/', views.TestList, name='test_list'),
    path('card/reader', views.TestReader, name='test_reader'),
    path('card/reader/ajax/', views.TestReaderAjax, name='test_reader_ajax'),    
    path('card/add/', login_required(views.TestAdd.as_view()), name='test_add'),
    path('card/<int:pk>/',login_required(views.TestEdit.as_view()), name='test_edit'),
    path('card/<int:pk>/delete',login_required(views.TestDelete.as_view()), name='test_delete'),
]