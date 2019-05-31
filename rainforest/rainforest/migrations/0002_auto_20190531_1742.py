# Generated by Django 2.2.1 on 2019-05-31 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rainforest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_in_cents',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='rainforest.Product')),
            ],
        ),
    ]
