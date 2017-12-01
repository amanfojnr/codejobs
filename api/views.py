from django.shortcuts import render
from rest_framework import generics
from .models import Company, Listing, Company
from .serializers import CompanySerializer, ListingSerializer
from rest_framework import permissions

# Create your views here.


class CompanyList(generics.ListCreateAPIView):
    """ list all companies """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListingList(generics.ListCreateAPIView):
    """ list all jobs """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class CompanyDetail(generics.RetrieveUpdateAPIView):
    """ retrieve or update existing job """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ListingDetail(generics.RetrieveUpdateAPIView):
    """ retrieve or update existing job """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
