from django.urls import path

from . import views

urlpatterns = [
    path('data', views.CaptureView.get_text_from_url, name='get_text_from_url'),
    path('visitors', views.ListVisitors.as_view())
]