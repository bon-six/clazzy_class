# Generated by Django 3.2.9 on 2021-11-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('comment_title', models.CharField(max_length=200)),
                ('comment_content', models.TextField()),
                ('comment_date', models.DateTimeField(verbose_name='when comment')),
            ],
        ),
    ]
