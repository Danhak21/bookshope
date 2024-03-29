# Generated by Django 4.1.3 on 2022-11-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=250)),
                ('condition', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('book_publisher', models.CharField(max_length=250)),
                ('publish_year', models.DateField()),
                ('created_date', models.DateTimeField()),
                ('book_thumbnai', models.ImageField(blank=True, null=True, upload_to=None)),
                ('description', models.TextField()),
            ],
        ),
    ]
