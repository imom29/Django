from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('<int:movie_id>', views.get_movie_by_id, name='get_movie_by_id'),
]
