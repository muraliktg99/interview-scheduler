from rest_framework.routers import DefaultRouter
from django.urls import path
from .viewsets import PersonViewset, SearchViewset

router = DefaultRouter()

router.register(r'schedule', PersonViewset, basename='schedule')

urlpatterns = [
    path('search/', SearchViewset.as_view(), name="search")
]
urlpatterns += router.urls