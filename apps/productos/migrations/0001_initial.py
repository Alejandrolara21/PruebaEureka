# Generated by Django 2.2.24 on 2021-12-04 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subcategorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField(blank=True)),
                ('imagen', models.ImageField(upload_to='productos/imagenes')),
                ('registrado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcategorias.Subcategoria')),
            ],
        ),
    ]
