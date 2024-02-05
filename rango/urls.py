from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('about/', views.about, name = 'about'),
    path('', views.index, name = 'index'),
    #path('greetings/', views.greet, name = 'greet')
    path('category/<slug:category_name_slug>/', 
        views.show_category, name='show_category'),
]
