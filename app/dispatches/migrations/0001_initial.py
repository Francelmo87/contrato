# Generated by Django 5.2.1 on 2025-06-15 02:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requisitions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_at', models.DateTimeField(auto_now_add=True, verbose_name='Movido em')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('moved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='requisitions.requisition')),
            ],
        ),
        migrations.CreateModel(
            name='RequisitionApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_at', models.DateTimeField(auto_now_add=True, verbose_name='Aprovado em')),
                ('status', models.CharField(choices=[('approved', 'Aprovado'), ('rejected', 'Rejeitado')], default='approved', max_length=20)),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comentários')),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('requisition', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='approvals', to='requisitions.requisition')),
            ],
        ),
    ]
