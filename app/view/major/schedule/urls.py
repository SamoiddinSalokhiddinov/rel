from django.urls import path , include

from .views import *

app_name = 'schedule'

#from . import views
urlpatterns = [
    path("", ScheduleListView.as_view(), name="list"),
    path("add/", ScheduleCreateView.as_view(), name="add"),
    path("<int:pk>/", ScheduleDetailView.as_view(), name="single"),
    path("delete/<int:pk>/", ScheduleDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", ScheduleUpdateView.as_view(), name="update"),
]
