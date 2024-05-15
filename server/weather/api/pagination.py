from rest_framework.pagination import PageNumberPagination

class WeatherPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 10000


class RecordsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 10000
