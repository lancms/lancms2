# -*- coding: utf-8 -*-

# used by 'display_user' from allauth
def username(user):
    if user.get_full_name():
        return user.get_full_name()
    else:
        return user.username
