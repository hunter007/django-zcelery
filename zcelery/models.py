from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    '''
    celery task
    '''
    name = models.CharField('Task Name', max_length=32)
    desc = models.CharField('Description', max_length=128)

    class Meta:
        db_table = 'task'


class TaskMeta(models.Model):
    '''

    '''
    task_id = models.CharField('Task ID', max_length=64)
    # group = models.CharField
    chord = models.CharField('Task ID', max_length=64)
    args = models.TextField('Args', default=(,))
    kwargs = models.TextField('Keyword Args', default={})
    retries = models.IntegerField('Retries')
    is_eager = models.NullBooleanField('is eager?')
    eta = models.DateTimeField('ETA')
    expires = models.DateTimeField('expires', null=True, blank=True)
    log_file = models.CharField('Log File Path', max_length=128, null=True, blank=True)
    log_level = models.CharField('Log Level', max_length=16, null=True, blank=True)
    hostname = models.CharField('Hostname', max_length=32, null=True, blank=True)
    delivery_info = models.TextField('delivery_info', max_length=2048)
    called_directly = models.BooleanField('called directly')
    callbacks = models.TextField('delivery_info', max_length=2048)
    utc = models.BooleanField('UTC')
    headers = models.TextField('headers', max_length=1024)
    reply_to = models.CharField('reply_to', max_length=32)
    correlation_id = models.CharField('correlation_id', null=True, blank=True)

    class Meta:
        db_table = 'task_meta'


class TaskOption
