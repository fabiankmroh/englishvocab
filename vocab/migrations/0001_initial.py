# Generated by Django 2.0.4 on 2018-09-02 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defTxt', models.TextField()),
                ('wrongC', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocabTxt', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='definition',
            name='vocab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocab.Vocab'),
        ),
    ]
