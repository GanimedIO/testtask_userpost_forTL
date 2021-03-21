# Generated by Django 3.1.6 on 2021-03-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uposts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('suite', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catchPhrase', models.CharField(max_length=100)),
                ('bs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('website', models.CharField(max_length=100)),
                ('address', models.ManyToManyField(to='uposts.Address')),
                ('company', models.ManyToManyField(to='uposts.Company')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='geo',
            field=models.ManyToManyField(to='uposts.Geo'),
        ),
    ]
