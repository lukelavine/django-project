# Generated by Django 3.2.4 on 2022-12-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioEntry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
