from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.browse_notes, name='browse_notes'),
    path('upload/', views.upload_note, name='upload_note'),
    path('download/<int:note_id>/', views.download_note, name='download_note'),
    path('view/<int:note_id>/', views.view_note, name='view_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]