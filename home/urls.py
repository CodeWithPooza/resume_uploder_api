from django.urls import include, path
from home import views
from rest_framework import routers
from home.views import resumeViewSet  

router = routers.DefaultRouter()
router.register(r'resume', resumeViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]
