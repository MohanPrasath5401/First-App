# Generated by Django 4.1.2 on 2022-11-10 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_masterdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('time1', models.IntegerField()),
                ('ip_address', models.EmailField(max_length=100)),
                ('date1', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=200)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uid', to='firstApp.masterdata')),
            ],
            options={
                'unique_together': {('date1', 'ip_address'), ('uid', 'date1')},
            },
        ),
    ]