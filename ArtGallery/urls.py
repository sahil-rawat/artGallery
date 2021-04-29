from django.urls import path
from . import views

urlpatterns = [
  path('',views.Index.as_view()),
  path('create',views.CreateEntry.as_view()),
  path('read',views.ReadEntry.as_view()),
  path('edit/<int:id>',views.UpdateEntry.as_view()),
  path('delete/<int:id>',views.DeleteEntry.as_view()),
]
