# Generated by Django 3.2.9 on 2022-06-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twit', models.URLField(verbose_name='twitter')),
                ('linkedin', models.URLField(verbose_name='linkedin')),
                ('ins', models.URLField(verbose_name='instagram')),
            ],
            options={
                'verbose_name': 'мои ссылки',
                'verbose_name_plural': 'ссылку',
            },
        ),
    ]
