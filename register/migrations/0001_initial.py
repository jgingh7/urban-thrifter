from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import places.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpseekerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borough', models.CharField(choices=[('MAN', 'Manhattan'), ('BRK', 'Brooklyn'), ('QUN', 'Queens'), ('BRX', 'The Bronx'), ('STN', 'Staten Island')], max_length=3)),
                ('complaint_count', models.IntegerField(default=0)),
                ('rc_1', models.CharField(blank=True, choices=[('FOOD', 'Food'), ('MDCL', 'Medical/ PPE'), ('CLTH', 'Clothing/ Covers'), ('ELEC', 'Electronics'), ('OTHR', 'Others')], default=None, max_length=4, null=True)),
                ('rc_2', models.CharField(blank=True, choices=[('FOOD', 'Food'), ('MDCL', 'Medical/ PPE'), ('CLTH', 'Clothing/ Covers'), ('ELEC', 'Electronics'), ('OTHR', 'Others')], default=None, max_length=4, null=True)),
                ('rc_3', models.CharField(blank=True, choices=[('FOOD', 'Food'), ('MDCL', 'Medical/ PPE'), ('CLTH', 'Clothing/ Covers'), ('ELEC', 'Electronics'), ('OTHR', 'Others')], default=None, max_length=4, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DonorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropoff_location', places.fields.PlacesField(blank=True, max_length=255, null=True)),
                ('donation_count', models.IntegerField(default=0)),
                ('complaint_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]