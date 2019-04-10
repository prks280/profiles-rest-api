from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.Hello_Viewset, base_name='hello-viewset')
urlpatterns = [
    url(r'hello-view/',views.HelloAPIView.as_view()),
    url(r'',include(router.urls))

]