# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'QA'
        db.create_table('frontpage_qa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('frontpage', ['QA'])


    def backwards(self, orm):
        
        # Deleting model 'QA'
        db.delete_table('frontpage_qa')


    models = {
        'frontpage.feature': {
            'Meta': {'object_name': 'Feature'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'frontpage.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'frontpage.notice': {
            'Meta': {'object_name': 'Notice'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'frontpage.qa': {
            'Meta': {'object_name': 'QA'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'frontpage.screenshot': {
            'Meta': {'object_name': 'ScreenShot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
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
