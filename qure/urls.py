from django.urls import path
from .views import *

urlpatterns = [
    path('person/', PersonListCreateView.as_view(), name='person-list-create'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('person/all/', AllPersonListView.as_view(), name='all-person-list'),  
    path('person/delete/<int:pk>/', PersonDetailView.as_view(), name='person-delete'), 
    path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person-update'), 
    path('pratician/', PraticianListCreateView.as_view(), name='pratician-list-create'),
    path('pratician/<int:pk>/', PraticianDetailView.as_view(), name='pratician-detail'),
    path('pratician/all/', AllPraticianListView.as_view(), name='all-pratician-list'),  
    path('pratician/delete/<int:pk>/', PraticianDeleteView.as_view(), name='pratician-delete'), 
    path('pratician/update/<int:pk>/', PraticianUpdateView.as_view(), name='pratician-update'), 
    path('organization/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organization/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('organization/all/', AllOrganizationListView.as_view(), name='all-organization-list'),  
    path('organization/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='organization-delete'), 
    path('organization/update/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('subcription/', SubcriptionListCreateView.as_view(), name='subcription-list-create'),
    path('subcription/<int:pk>/', SubcriptionDetailView.as_view(), name='subcription-detail'),
    path('subcription/all/', AllSubcriptionListView.as_view(), name='all-subcription-list'),  
    path('subcription/delete/<int:pk>/', SubcriptionDeleteView.as_view(), name='subcription-delete'), 
    path('subcription/update/<int:pk>/', SubcriptionUpdateView.as_view(), name='subcription-update'),
    path('person/', AccountListCreateView.as_view(), name='account-list-create'),
    path('person/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('person/all/', AllAccountListView.as_view(), name='account-person-list'),  
    path('person/delete/<int:pk>/', AccountDetailView.as_view(), name='account-delete'), 
    path('person/update/<int:pk>/', AccountUpdateView.as_view(), name='account-update'),  

]