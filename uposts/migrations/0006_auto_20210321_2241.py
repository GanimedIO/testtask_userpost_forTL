# Generated by Django 3.1.6 on 2021-03-21 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uposts', '0005_auto_20210320_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='uposts.users'),
        ),
    ]