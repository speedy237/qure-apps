# Generated by Django 5.0.6 on 2024-07-07 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('reason', models.CharField(default='general consultation', max_length=500)),
                ('systolic', models.IntegerField()),
                ('diastolic', models.IntegerField()),
                ('weight', models.FloatField()),
                ('heart_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type_organization', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('abo', models.CharField(max_length=10)),
                ('rh', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('result', models.TextField()),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='ExamFileResult',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='exam_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.examination')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.patient'),
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person_contact', models.CharField(max_length=100)),
                ('operation10', models.CharField(max_length=100)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qure2.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Antecedent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('patient_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.patientrecord')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qure2.person'),
        ),
        migrations.CreateModel(
            name='Practician',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qure2.person')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='practician',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='qure2.practician'),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.organization')),
                ('practician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.practician')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('posology', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=100)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dos', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Transfert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_done', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.organization')),
                ('patientRecord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qure2.patientrecord')),
            ],
        ),
    ]
