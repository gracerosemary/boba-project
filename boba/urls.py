from django.urls import path
from .views import BobaListView, BobaCreateView, BobaDeleteView, BobaDetailView, BobaUpdateView

urlpatterns = [
    path("", BobaListView.as_view(), name="boba_list"),
    path("<int:pk>/", BobaDetailView.as_view(), name="boba_detail"),
    path("new/", BobaCreateView.as_view(), name="boba_create"),
    path("<int:pk>/edit", BobaUpdateView.as_view(), name="boba_update"),
    path("<int:pk>/delete", BobaDeleteView.as_view(), name="boba_delete"),
]