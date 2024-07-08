from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    abo = models.CharField(max_length=10)  # GS might refer to blood group or similar
    rh = models.CharField(max_length=10)  # RH might refer to Rhesus factor
    def __str__(self):
        return self.abo

class Practician(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    order = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Organization(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type_organization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Consultation(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    practician = models.ForeignKey(Practician,on_delete=models.CASCADE,default=1)
    reason=models.CharField(max_length=500,default="general consultation")
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    weight = models.FloatField()
    heart_rate = models.IntegerField()
    def __str__(self):
        return self.reason

class Examination(models.Model):
    id = models.BigAutoField(primary_key=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    result = models.TextField()
    def __str__(self):
        return self.name


class Prescription(models.Model):
    id = models.BigAutoField(primary_key=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    posology = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    dos = models.DateField()  # Date of Subscription
    status = models.CharField(max_length=50)

class PatientRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    person_contact = models.CharField(max_length=100)
    operation10 = models.CharField(max_length=100)  # This seems to be a placeholder, adjust as necessary

class Antecedent(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_record = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

class ExamFileResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    file = models.FileField(upload_to='exam_files/')
    created_at = models.DateTimeField(auto_now_add=True)

class Account(models.Model):
    id=models.BigAutoField(primary_key=True)
    practician=models.ForeignKey(Practician,on_delete=models.CASCADE)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
class Transfert(models.Model):
    patientRecord=models.ForeignKey(PatientRecord,on_delete=models.CASCADE)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    is_done=models.BooleanField(default=False)