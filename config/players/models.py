import os
import uuid

from django.db import models

from django.conf import settings

from config import settings


class Player(models.Model):
    # player Model

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(blank=False)
    playername = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=False)
    nationality = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    playerimage = models.ImageField(upload_to='images/', blank=True)

    # To discrimination on admin page

    def __str__(self):
        return f"{self.playername} {self.nationality}"

    def get_image_path(self, filename):
        prefix = 'images/'
        name = str(uuid.uuid4()).replace('-', '')
        extension = os.path.splitext(filename)[-1]
        return prefix + name + extension

    def delete_previous_file(function):
        def wrapper(*args, **kwargs):
            self = args[0]

            # 保存前のファイル名を取得
            result = Player.objects.filter(pk=self.pk)
            previous = result[0] if len(result) else None
            super(Player, self).save()

            # 関数実行
            result = function(*args, **kwargs)

            # 保存前のファイルがあったら削除
            if previous:
                os.remove(settings.MEDIA_ROOT + '/' + previous.image.name)
            return result
        return wrapper
