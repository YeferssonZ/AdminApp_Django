# Generated by Django 3.2 on 2023-06-03 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_nota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='aulas',
        ),
        migrations.AddField(
            model_name='curso',
            name='aulas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.aula'),
        ),
    ]
