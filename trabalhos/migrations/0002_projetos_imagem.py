# Generated by Django 3.2.8 on 2021-10-21 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='imagem',
            field=models.ImageField(null=True, upload_to='static'),
        ),
    ]