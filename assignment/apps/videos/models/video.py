from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    publishedTime = models.DateTimeField(auto_now=False)
    videoId = models.CharField(max_length=100, primary_key=True)
    channelId = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True, editable=False)
    updatedOn = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "Videos"
        indexes = [
            models.Index(fields=["publishedTime"]),
            models.Index(fields=["title"]),
        ]

    def __str__(self):
        return self.title


class VideoThumbNail(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="thumbnail")
    screenType = models.CharField(max_length=20)
    url = models.URLField(max_length=1000)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    createdOn = models.DateTimeField(auto_now_add=True, editable=False)
    updatedOn = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "VideoThumbNails"

    def __str__(self):
        return self.video.title + self.screenSize
