# Generated by Django 2.0.6 on 2019-05-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookClassify',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('null1', models.CharField(blank=True, max_length=20, null=True)),
                ('null2', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'book_classify',
            },
        ),
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pic_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('writer', models.CharField(blank=True, max_length=20, null=True)),
                ('press', models.CharField(blank=True, max_length=60, null=True)),
                ('p_time', models.DateField(blank=True, null=True)),
                ('edition', models.CharField(blank=True, max_length=20, null=True)),
                ('printing_time', models.DateField(blank=True, null=True)),
                ('p_number', models.CharField(blank=True, max_length=20, null=True)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=20, null=True)),
                ('words', models.CharField(blank=True, max_length=20, null=True)),
                ('pages', models.CharField(blank=True, max_length=20, null=True)),
                ('format', models.CharField(blank=True, max_length=20, null=True)),
                ('paperr', models.CharField(blank=True, max_length=20, null=True)),
                ('packaging', models.CharField(blank=True, max_length=20, null=True)),
                ('pricing', models.CharField(blank=True, max_length=20, null=True)),
                ('recommend', models.TextField(blank=True, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('directory', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('illustration', models.TextField(blank=True, null=True)),
                ('null1', models.CharField(blank=True, max_length=20, null=True)),
                ('null2', models.CharField(blank=True, max_length=20, null=True)),
                ('launch_time', models.DateField(blank=True, null=True)),
                ('purchase', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_book',
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('start_time', models.DateField(blank=True, null=True)),
                ('null1', models.CharField(blank=True, max_length=20, null=True)),
                ('null2', models.CharField(blank=True, max_length=20, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('state', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_order',
            },
        ),
        migrations.CreateModel(
            name='TOrderitem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_number', models.IntegerField(blank=True, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_orderitem',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email_addr', models.CharField(blank=True, max_length=60, null=True)),
                ('nickname', models.CharField(blank=True, max_length=60, null=True)),
                ('password', models.CharField(blank=True, max_length=60, null=True)),
                ('null_1', models.CharField(blank=True, max_length=60, null=True)),
                ('null_2', models.CharField(blank=True, max_length=60, null=True)),
                ('state', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_user',
            },
        ),
        migrations.CreateModel(
            name='TUserInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('addr', models.CharField(blank=True, max_length=40, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=20, null=True)),
                ('phone1', models.CharField(blank=True, max_length=20, null=True)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('null1', models.CharField(blank=True, max_length=20, null=True)),
                ('null2', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_user_info',
            },
        ),
    ]
