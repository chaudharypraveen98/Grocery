from django.urls import path

from grocery_list import views

app_name = 'grocery'

urlpatterns = [
    path('', views.GroceryListView.as_view(), name="index"),
    path('<int:pk>/update', views.GroceryView.as_view(), name="update"),
    path('<int:pk>/delete', views.GroceryDeleteView.as_view(), name="delete"),
    path('create', views.GroceryCreateView.as_view(), name="create"),
]
