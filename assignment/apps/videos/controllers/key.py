from django_filters import FilterSet, filters
from rest_framework import mixins, viewsets

from videos.models.key import APIKey
from videos.serializers.key import APIKeySerializer


class APIKeyFilter(FilterSet):
    active = filters.BooleanFilter(
        field_name="active", lookup_expr="exact", label="active"
    )

    class Meta:
        model = APIKey
        fields = {"active"}


class APIKeyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = APIKey.objects.all().order_by("-active")
    serializer_class = APIKeySerializer
    filter_class = APIKeyFilter
    filter_fields = {"active"}
