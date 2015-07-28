from django.contrib import admin

import simple_history
from django.contrib.auth.models import User, Group

simple_history.register(User)
simple_history.register(Group)
