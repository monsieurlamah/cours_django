# Generated by Django 5.0.7 on 2024-08-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact_civility_alter_contact_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/%d/%m/%Y'),
        ),
    ]
