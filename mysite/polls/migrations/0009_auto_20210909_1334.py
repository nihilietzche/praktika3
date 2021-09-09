# Generated by Django 3.2.6 on 2021-09-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210909_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='option_four_count',
            new_name='option_four_points',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='option_one_count',
            new_name='option_one_points',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='option_three_count',
            new_name='option_three_points',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='option_two_count',
            new_name='option_two_points',
        ),
        migrations.AddField(
            model_name='question',
            name='option_four_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_one_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_three_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_two_visible',
            field=models.BooleanField(default=True),
        ),
    ]