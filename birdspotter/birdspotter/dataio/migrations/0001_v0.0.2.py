# Generated by Django 3.1.3 on 2021-03-12 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import private_storage.storage.files
import uuid


class Migration(migrations.Migration):

    replaces = [('dataio', '0001_initial')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comments', models.CharField(blank=True, max_length=500)),
                ('dataset_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_public', models.BooleanField(default=False)),
                ('date_collected', models.DateField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'permissions': [('export_dataset', 'Can export dataset')],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.ImageField(storage=private_storage.storage.files.PrivateFileSystemStorage, upload_to='')),
                ('image_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataio.dataset')),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(storage=private_storage.storage.files.PrivateFileSystemStorage, upload_to='raw_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Shapefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('island_name', models.CharField(max_length=50)),
                ('cireg', models.CharField(max_length=20)),
                ('photo_date', models.DateField()),
                ('observer', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=100)),
                ('behavior', models.IntegerField()),
                ('certain_p1', models.CharField(max_length=20)),
                ('comments', models.CharField(blank=True, max_length=500)),
                ('point_x', models.FloatField()),
                ('point_y', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('data_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataio.dataset')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataio.image')),
            ],
        ),
        migrations.CreateModel(
            name='RawShapefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataio.dataset')),
                ('rawshp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataio.rawdata')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='geotiff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataio.rawdata'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
