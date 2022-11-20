from rest_framework import serializers

from videos.models.video import Video, VideoThumbNail


class VideoSerializer(serializers.ModelSerializer):

    thumbnails = serializers.SerializerMethodField()

    def get_thumbnails(self, obj):
        return [
            VideoThumbNailSerializer(thumbnail).data
            for thumbnail in VideoThumbNail.objects.filter(video=obj)
        ]

    class Meta:
        model = Video
        fields = "__all__"


class VideoThumbNailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoThumbNail
        fields = "__all__"
