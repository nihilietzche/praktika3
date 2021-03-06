# Generated by Django 3.2.6 on 2021-09-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210907_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_one',
            field=models.TextField(default='null', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='option_three',
            field=models.TextField(default='null', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option_three_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='option_two',
            field=models.TextField(default='null', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option_two_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
