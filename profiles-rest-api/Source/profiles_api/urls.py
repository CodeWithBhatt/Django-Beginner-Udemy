from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-view-set', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-api-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls)),
]