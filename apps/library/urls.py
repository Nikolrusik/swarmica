from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.library.views import DepartmentViewSet, BookViewSet, VisitorViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'books', BookViewSet)
router.register(r'visitors', VisitorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
