from django.urls import path
from .views import StoriesListApiView


urlpatterns = [
    path('', StoriesListApiView.as_view()),
]
