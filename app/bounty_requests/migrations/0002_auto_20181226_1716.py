# Generated by Django 2.1.4 on 2018-12-26 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        ('bounty_requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bountyrequestmeta',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='bountyrequest',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bounty_requests', to='dashboard.Profile'),
        ),
    ]
