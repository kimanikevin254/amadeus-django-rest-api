from .import views
from django.urls import path

urlpatterns = [
    # City search endpoint
    path('cities/search/', views.CitySearchAPIView.as_view(), name='city-search'),
]