# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TradeDuration'
        db.create_table(u'trades_tradeduration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'trades', ['TradeDuration'])

        # Adding model 'TradeType'
        db.create_table(u'trades_tradetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'trades', ['TradeType'])

        # Deleting field 'Trade.length_of_offer'
        db.delete_column(u'trades_trade', 'length_of_offer')

        # Adding field 'Trade.trade_duration'
        db.add_column(u'trades_trade', 'trade_duration',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trades.TradeDuration'], null=True),
                      keep_default=False)


        # Renaming column for 'Trade.trade_type' to match new field type.
        db.rename_column(u'trades_trade', 'trade_type', 'trade_type_id')
        # Changing field 'Trade.trade_type'
        db.alter_column(u'trades_trade', 'trade_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trades.TradeType'], null=True))
        # Adding index on 'Trade', fields ['trade_type']
        db.create_index(u'trades_trade', ['trade_type_id'])


        # Renaming column for 'Trade.server' to match new field type.
        db.rename_column(u'trades_trade', 'server', 'server_id')
        # Changing field 'Trade.server'
        db.alter_column(u'trades_trade', 'server_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trades.Server'], null=True))
        # Adding index on 'Trade', fields ['server']
        db.create_index(u'trades_trade', ['server_id'])


    def backwards(self, orm):
        # Removing index on 'Trade', fields ['server']
        db.delete_index(u'trades_trade', ['server_id'])

        # Removing index on 'Trade', fields ['trade_type']
        db.delete_index(u'trades_trade', ['trade_type_id'])

        # Deleting model 'TradeDuration'
        db.delete_table(u'trades_tradeduration')

        # Deleting model 'TradeType'
        db.delete_table(u'trades_tradetype')

        # Adding field 'Trade.length_of_offer'
        db.add_column(u'trades_trade', 'length_of_offer',
                      self.gf('django.db.models.fields.CharField')(default=3, max_length=255),
                      keep_default=False)

        # Deleting field 'Trade.trade_duration'
        db.delete_column(u'trades_trade', 'trade_duration_id')


        # Renaming column for 'Trade.trade_type' to match new field type.
        db.rename_column(u'trades_trade', 'trade_type_id', 'trade_type')
        # Changing field 'Trade.trade_type'
        db.alter_column(u'trades_trade', 'trade_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Renaming column for 'Trade.server' to match new field type.
        db.rename_column(u'trades_trade', 'server_id', 'server')
        # Changing field 'Trade.server'
        db.alter_column(u'trades_trade', 'server', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'trades.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'trades.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'trades.server': {
            'Meta': {'object_name': 'Server'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'trades.trade': {
            'Meta': {'object_name': 'Trade'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'buyout_price': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trades.Category']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auth.User']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trades.Server']", 'null': 'True'}),
            'start_price': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'trade_duration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trades.TradeDuration']", 'null': 'True'}),
            'trade_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trades.TradeType']", 'null': 'True'})
        },
        u'trades.tradeduration': {
            'Meta': {'object_name': 'TradeDuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'trades.tradetype': {
            'Meta': {'object_name': 'TradeType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['trades']