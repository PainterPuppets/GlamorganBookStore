# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from django.db import models

class User(AbstractBaseUser):
    # required for registeration
    email = models.EmailField('注册邮箱', unique=True, db_index=True,
                              validators=[validate_email])
    # for admin
    is_staff = models.BooleanField(_('staff status'), default=False)