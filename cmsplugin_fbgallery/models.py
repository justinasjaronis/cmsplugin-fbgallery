from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

import re

class FacebookGallery(CMSPlugin):
    album_url = models.CharField(_('Album URL'), max_length=1000)
    album_id = models.CharField(_('Album Id'), max_length=500, default='(detect automatically)')
    album_name = models.CharField(_('Album Name'), max_length=100)
    
    def save(self, *args, **kwargs):
        p = re.compile('\d+')
        ids = p.findall(self.album_url)
        if len(ids) > 3:
            self.album_id = '%s_%s' % (ids[2], ids[1])
        res = super(FacebookGallery, self).save(*args, **kwargs)
        return res

