# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookClassify(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    c = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    null1 = models.CharField(max_length=20, blank=True, null=True)
    null2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_classify'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TBook(models.Model):
    pic_addr = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    writer = models.CharField(max_length=20, blank=True, null=True)
    press = models.CharField(max_length=60, blank=True, null=True)
    p_time = models.DateField(blank=True, null=True)
    edition = models.CharField(max_length=20, blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    p_number = models.CharField(max_length=20, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    words = models.CharField(max_length=20, blank=True, null=True)
    pages = models.CharField(max_length=20, blank=True, null=True)
    format = models.CharField(max_length=20, blank=True, null=True)
    paperr = models.CharField(max_length=20, blank=True, null=True)
    packaging = models.CharField(max_length=20, blank=True, null=True)
    pricing = models.CharField(max_length=20, blank=True, null=True)
    recommend = models.TextField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    directory = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    illustration = models.TextField(blank=True, null=True)
    null1 = models.CharField(max_length=20, blank=True, null=True)
    null2 = models.CharField(max_length=20, blank=True, null=True)
    launch_time = models.DateField(blank=True, null=True)
    purchase = models.IntegerField(blank=True, null=True)
    book = models.ForeignKey(BookClassify, models.DO_NOTHING, blank=True, null=True)
    dang_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    info = models.ForeignKey('TUserInfo', models.DO_NOTHING, blank=True, null=True)
    null1 = models.CharField(max_length=20, blank=True, null=True)
    null2 = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderitem(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    item_number = models.IntegerField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_orderitem'


class TUser(models.Model):
    id = models.IntegerField(primary_key=True)
    email_addr = models.CharField(max_length=60, blank=True, null=True)
    nickname = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    null_1 = models.CharField(max_length=60, blank=True, null=True)
    null_2 = models.CharField(max_length=60, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TUserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    addr = models.CharField(max_length=40, blank=True, null=True)
    postalcode = models.CharField(max_length=20, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    null1 = models.CharField(max_length=20, blank=True, null=True)
    null2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_info'


class Confirm_string(models.Model):
    code = models.CharField(max_length=256, verbose_name='用户注册码')
    user = models.ForeignKey('TUser', on_delete=models.CASCADE, verbose_name='关联的用户')
    code_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 't_confirm_string'
