# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.models import User

from guardian.shortcuts import assign_perm, remove_perm

class AddManagerForm(forms.Form):
    username = forms.CharField(max_length=256)

    def user_exists(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
            return True
        except:
            return False

    def save(self, object, permission):
        user = User.objects.get(username=self.cleaned_data['username'])
        return assign_perm(permission, user, object)


class RemoveManagerForm(forms.Form):
    pass

    def save(self, object, user, permission):
        return remove_perm(permission, user, object)
