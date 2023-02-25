# Generated by Django 4.1.4 on 2023-01-03 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=30)),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('mob', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('address', models.TextField()),
                ('qualification', models.CharField(max_length=10)),
                ('sem', models.CharField(max_length=10)),
                ('passout', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.student')),
                ('total_fee', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('submitamount', models.CharField(max_length=100)),
                ('submitdate', models.CharField(max_length=100)),
                ('nextpaydate', models.DateField()),
            ],
        ),
    ]