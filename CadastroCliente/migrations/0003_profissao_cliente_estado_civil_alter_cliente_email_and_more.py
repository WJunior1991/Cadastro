# Generated by Django 4.2 on 2023-04-24 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0002_cliente_bairro_cliente_cep_cliente_cidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado_civil',
            field=models.CharField(choices=[('SOL', 'Solteiro'), ('CAS', 'Casado'), ('DIV', 'Divorciado'), ('VIU', 'Viúvo')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
