# Generated by Django 2.2 on 2019-04-30 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctavka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='sport_name',
            field=models.CharField(max_length=30, verbose_name='Вид спорта'),
        ),
        migrations.CreateModel(
            name='Ctavka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('coefficient', models.FloatField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ctavka.Sport', verbose_name='спорт')),
            ],
            options={
                'verbose_name': 'Ставка',
                'verbose_name_plural': 'Ставки',
                'ordering': ['-published'],
            },
        ),
    ]
