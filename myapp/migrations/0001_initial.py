# Generated by Django 4.2.7 on 2023-11-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Citizens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('fdob', models.CharField(max_length=20)),
                ('pob', models.CharField(max_length=20)),
                ('fpob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('cob', models.CharField(max_length=20)),
                ('nrc', models.CharField(max_length=20)),
                ('postal', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('village', models.CharField(max_length=20)),
                ('chief', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
