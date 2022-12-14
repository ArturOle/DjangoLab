# Generated by Django 3.2.8 on 2021-11-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(verbose_name='create time')),
                ('last_edit_time', models.DateTimeField(verbose_name='last edit time')),
            ],
        ),
    ]
