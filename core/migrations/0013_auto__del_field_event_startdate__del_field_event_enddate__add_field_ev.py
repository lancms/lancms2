# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.startdate'
        db.delete_column('core_event', 'startdate')

        # Deleting field 'Event.enddate'
        db.delete_column('core_event', 'enddate')

        # Adding field 'Event.startdatetime'
        db.add_column('core_event', 'startdatetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 18, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.enddatetime'
        db.add_column('core_event', 'enddatetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 18, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Event.startdate'
        raise RuntimeError("Cannot reverse this migration. 'Event.startdate' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.startdate'
        db.add_column('core_event', 'startdate',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Event.enddate'
        raise RuntimeError("Cannot reverse this migration. 'Event.enddate' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.enddate'
        db.add_column('core_event', 'enddate',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Deleting field 'Event.startdatetime'
        db.delete_column('core_event', 'startdatetime')

        # Deleting field 'Event.enddatetime'
        db.delete_column('core_event', 'enddatetime')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.event': {
            'Meta': {'object_name': 'Event'},
            'enddatetime': ('django.db.models.fields.DateTimeField', [], {}),
            'externalurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Organization']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']"}),
            'startdatetime': ('django.db.models.fields.DateTimeField', [], {}),
            'urlslug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        },
        'core.organization': {
            'Meta': {'object_name': 'Organization'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'externalurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['auth.Group']"}),
            'urlslug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        },
        'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'postalcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'streetaddress': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['core']