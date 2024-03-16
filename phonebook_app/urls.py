from django.urls import path, include
from .views import PersonViewSet, AddressViewSet
from rest_framework import routers


address_router = routers.DefaultRouter()
address_router.register('', AddressViewSet)

person_router = routers.DefaultRouter()
person_router.register('', PersonViewSet)


urlpatterns = [
    path('address/', include(address_router.urls,)),
    path('person/', include(person_router.urls,)),
]
