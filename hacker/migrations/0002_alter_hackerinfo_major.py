# Generated by Django 4.0 on 2022-01-04 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackerinfo',
            name='major',
            field=models.CharField(choices=[('High School/Secondary School', 'High School/Secondary School'), ('University (Undergrad)', 'University (Undergrad)'), ("University (Master's/Doctoral)", "University (Master's/Doctoral)")], default='other', max_length=60),
        ),
    ]