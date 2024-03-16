from django.shortcuts import render, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from .serializers import AddressSerializer, PersonSerializer
from .models import Person, Address


class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Address.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Person.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
