from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PersonUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    partial = True
    
    
class PersonDeleteView(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Person"))

class PraticianListCreateView(generics.ListCreateAPIView):
    queryset = Practician.objects.all()
    serializer_class = PraticianSerializer
    
class PraticianUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Practician.objects.all()
    serializer_class = PraticianSerializer
    partial = True
    
    
class PraticianDeleteView(generics.DestroyAPIView):
    queryset = Practician.objects.all()
    serializer_class = PraticianSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Pratician"))

class SubcriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer
    
class SubcriptionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer
    partial = True
    
    
class SubcriptionDeleteView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Subcription"))

class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
class OrganizationUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    partial = True
    
    
class OrganizationDeleteView(generics.DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Organization"))
    
class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    
class PraticianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Practician.objects.all()
    serializer_class = PraticianSerializer

class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
    
class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class SubcriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer
    
    
class SubcriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer

class AllPersonListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class AllPraticianListView(generics.ListAPIView):
    queryset = Practician.objects.all()
    serializer_class = PatientSerializer

class AllOrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class AllSubcriptionListView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PraticianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Practician.objects.all()
    serializer_class = PraticianSerializer

class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
class SubcriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer
class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransfertListCreateView(generics.ListCreateAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer
class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
class TransfertDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer
class AllAccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AllTransfertListView(generics.ListAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer

class AccountDeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Account"))
class AccountUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    partial = True
class TransfertUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer
    partial = True
        