# Generated by Django 5.0.6 on 2024-05-25 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one_image', '0002_field_honor_person_delete_image_honor_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
                ('build_date', models.DateTimeField()),
                ('work_goal', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='honor',
            name='name',
            field=models.CharField(default='Honor', max_length=30, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='honor',
            name='who_give',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='one_image.institute', verbose_name='از طرف'),
        ),
        migrations.AddField(
            model_name='person',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='one_image.institute', verbose_name='سازمان'),
        ),
    ]