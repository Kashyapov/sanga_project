# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from rest_framework import serializers
from models import Sadhu, SadhuAdditional
from sorl.thumbnail import get_thumbnail

class SubsSerializer(serializers.ModelSerializer):
    avatar_width = 45
    avatar_height = 45

    url_avatar = serializers.SerializerMethodField()
    url_avatar_width = serializers.SerializerMethodField()
    url_avatar_height = serializers.SerializerMethodField()

    def get_url_avatar_width(self, sadhu):
        return self.avatar_width

    def get_url_avatar_height(self, sadhu):
        return self.avatar_height

    def get_url_avatar(self, sadhu):
          url_avatar = ''
          sa = SadhuAdditional.objects.get(pk = 1)
          if sa and sa.image:
              try:
                im = get_thumbnail(sa.image.file, str(self.avatar_width) + 'x' + str(self.avatar_height), crop='center', quality=99)
                url_avatar = im.url
              except IOError:
                  pass
          return url_avatar


    class Meta:
        model = Sadhu
        fields = ('username', 'spiritual_name', 'last_name', 'first_name','middle_name', 'get_absolute_url', 'url_avatar', 'url_avatar_width', 'url_avatar_height')
