# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Sponsor.rank'
        db.delete_column('frontpage_sponsor', 'rank')


    def backwards(self, orm):
        
        # Adding field 'Sponsor.rank'
        db.add_column('frontpage_sponsor', 'rank', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    models = {
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'frontpage.notice': {
            'Meta': {'object_name': 'Notice'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'frontpage.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'frontpage.sponsorcate': {
            'Meta': {'object_name': 'SponsorCate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sponsors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['frontpage.Sponsor']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['frontpage']
