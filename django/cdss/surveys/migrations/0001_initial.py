# Generated by Django 3.2 on 2021-04-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(default='wcp', max_length=10)),
                ('block', models.IntegerField(max_length=4)),
            ],
        ),
    ]