from constance import config
from rest_framework.pagination import PageNumberPagination

class VideoPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page'
    max_page_size = 1000
    ordering="-publishedTime"