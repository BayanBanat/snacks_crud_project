from django.urls import path
from .views import SnacksListView,SnacksDetailView,SnacksCreateView,SnacksDeleteView,SnacksUpdateView

urlpatterns = [
    path('', SnacksListView.as_view(), name="snakslist"),
    path('<int:pk>', SnacksDetailView.as_view(), name="snaksdetail"),
    path('create/', SnacksCreateView.as_view(), name="createsnaks"),
    path('delete/<int:pk>/', SnacksDeleteView.as_view(), name="deletesnaks"),
    path('update/<int:pk>/', SnacksUpdateView.as_view(), name="updatesnaks"),
]