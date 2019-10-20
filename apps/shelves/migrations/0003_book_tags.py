# Generated by Django 2.2.6 on 2019-10-20 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='books', to='shelves.Tag'),
        ),
    ]