# Generated by Django 4.0.1 on 2022-01-11 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferModel',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que fue creado el objeto.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha en la que fue alterado el objeto.')),
                ('offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('salary', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_id', to=settings.AUTH_USER_MODEL)),
                ('updater_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
