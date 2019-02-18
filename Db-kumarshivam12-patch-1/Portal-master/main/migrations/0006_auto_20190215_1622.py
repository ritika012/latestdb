# Generated by Django 2.1.7 on 2019-02-15 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190215_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='role_per',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=250)),
                ('perr', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='cabprosessing',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.AlterField(
            model_name='consumer_db',
            name='Empid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.role_per'),
        ),
    ]
