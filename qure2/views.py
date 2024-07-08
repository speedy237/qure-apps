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


#Gestion des Dossiers Médicaux    

class PatientRecordListCreateView(generics.ListCreateAPIView):
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer

class PatientRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer

#Gestion des transfert

class TransfertListCreateView(generics.ListCreateAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer

class TransfertDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer

class AllAccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AllTransfertListView(generics.ListAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer

class TransfertUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer
    partial = True

#Gestion des comptes utilisateurs des medecins

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

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

class AccountsByOrganizationView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return Account.objects.filter(organization_id=organization_id)
    
#gestion du patient
#     
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDeleteView(generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Patient deleted successfully"})
class PatientUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    partial = True

class PersonSearchByNameView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            return Person.objects.filter(name__icontains=name)
        return Person.objects.none()
    
# consultation 

class ConsultationListCreateView(generics.ListCreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ConsultationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

#prescription

class PrescriptionListCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

#Antecedent

class AntecedentListCreateView(generics.ListCreateAPIView):
    queryset = Antecedent.objects.all()
    serializer_class = AntecedentSerializer

class AntecedentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Antecedent.objects.all()
    serializer_class = AntecedentSerializer

class ExamFileResultListCreateView(generics.ListCreateAPIView):
    queryset = ExamFileResult.objects.all()
    serializer_class = ExamFileResultSerializer

class ExamFileResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamFileResult.objects.all()
    serializer_class = ExamFileResultSerializer

#Exam

class ExaminationListCreateView(generics.ListCreateAPIView):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer

class ExaminationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer

class ConsultationByPracticianView(generics.ListAPIView):
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        practician_id = self.kwargs['practician_id']
        return Consultation.objects.filter(practician_id=practician_id)

class ConsultationByPatientView(generics.ListAPIView):
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Consultation.objects.filter(patient_id=patient_id)
    
class ConsultationsByPatientPracticianView(generics.ListAPIView):
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        practician_id = self.kwargs['practician_id']
        return Consultation.objects.filter(patient_id=patient_id, practician_id=practician_id)
    
class ConsultationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer