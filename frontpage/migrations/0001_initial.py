# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Feature'
        db.create_table('frontpage_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('new', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('frontpage', ['Feature'])

        # Adding model 'Notice'
        db.create_table('frontpage_notice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('important', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('frontpage', ['Notice'])

        # Adding model 'Sponsor'
        db.create_table('frontpage_sponsor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('frontpage', ['Sponsor'])

        # Adding model 'SponsorCate'
        db.create_table('frontpage_sponsorcate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('frontpage', ['SponsorCate'])

        # Adding M2M table for field sponsors on 'SponsorCate'
        db.create_table('frontpage_sponsorcate_sponsors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sponsorcate', models.ForeignKey(orm['frontpage.sponsorcate'], null=False)),
            ('sponsor', models.ForeignKey(orm['frontpage.sponsor'], null=False))
        ))
        db.create_unique('frontpage_sponsorcate_sponsors', ['sponsorcate_id', 'sponsor_id'])


    def backwards(self, orm):
        
        # Deleting model 'Feature'
        db.delete_table('frontpage_feature')

        # Deleting model 'Notice'
        db.delete_table('frontpage_notice')

        # Deleting model 'Sponsor'
        db.delete_table('frontpage_sponsor')

        # Deleting model 'SponsorCate'
        db.delete_table('frontpage_sponsorcate')

        # Removing M2M table for field sponsors on 'SponsorCate'
        db.delete_table('frontpage_sponsorcate_sponsors')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
