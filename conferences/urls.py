import from django.urls import path
import from django.urls import views
urlpatterns = [
    path('', views.create_conference),
    path('read conference', views.read_conference),
    path('update conferences', views.update_conference),
    path('delete conference', views.delete_conference)
]