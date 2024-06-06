from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload_document, name='document-upload'),
    path("", views.CardListView, name="card-list"),
    path("new", views.CardCreateView, name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>", views.BoxView, name="box-view"),
    path("delete-box/<int:box_num>", views.delete_box, name="delete-box"),
    path("train", views.SelectBoxView, name="select-box"),
    path("train/<int:box_num>", views.TrainView, name="card-train"),
]
