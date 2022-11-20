from django.db.models import Q
from django_filters import FilterSet, filters
from rest_framework import mixins, viewsets

from django.contrib.postgres.search import SearchVector, SearchQuery
from videos.models.video import Video
from videos.paginations import VideoPagination
from videos.serializers.video import VideoSerializer


class VideoFilter(FilterSet):
    title = filters.CharFilter(method="search_keyword", label="Title")

    class Meta:
        model = Video
        fields = {"title"}

    def search_keyword(self, queryset, name, value):
        return queryset.annotate(search=SearchVector("title", "description")).filter(
            search=SearchQuery(value)
        )


class VideoViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Video.objects.all().order_by("-publishedTime")
    serializer_class = VideoSerializer
    filter_class = VideoFilter
    pagination_class = VideoPagination
