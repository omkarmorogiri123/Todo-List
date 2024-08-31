from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

# Use the router's URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
