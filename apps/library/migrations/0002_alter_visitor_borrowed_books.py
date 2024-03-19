# Generated by Django 5.0.3 on 2024-03-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='borrowed_books',
            field=models.ManyToManyField(blank=True, related_name='borrowers', to='library.book'),
        ),
    ]