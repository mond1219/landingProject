# Generated by Django 4.0.3 on 2022-04-07 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('med_uid', models.AutoField(primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=20)),
                ('med_type', models.CharField(max_length=8)),
                ('med_buyprice', models.PositiveIntegerField()),
                ('med_sellprice', models.PositiveIntegerField()),
                ('med_cgst', models.PositiveSmallIntegerField()),
                ('med_sgst', models.PositiveSmallIntegerField()),
                ('med_expire', models.DateField()),
                ('med_mfg', models.DateField()),
                ('med_desc', models.TextField()),
                ('med_instock', models.PositiveIntegerField()),
                ('med_qty', models.PositiveSmallIntegerField()),
                ('med_company', models.CharField(max_length=30)),
                ('user_uid', models.ForeignKey(db_column='user_uid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
        ),
    ]