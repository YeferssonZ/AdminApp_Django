# Generated by Django 3.2 on 2023-05-25 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.roles'),
        ),
    ]