# motorcycle/urls.py
from django.urls import path
from .views import motorcycle_list, motorcycle_detail, create_motorcycle, update_motorcycle, delete_motorcycle

app_name = 'motorcycle'

urlpatterns = [
    path('', motorcycle_list, name='motorcycle_list'),
    path('<int:motorcycle_id>/', motorcycle_detail, name='motorcycle_detail'),
    path('create/', create_motorcycle, name='create_motorcycle'),
    path('<int:motorcycle_id>/update/', update_motorcycle, name='update_motorcycle'),
    path('<int:motorcycle_id>/delete/', delete_motorcycle, name='delete_motorcycle'),  # Add this line
]
