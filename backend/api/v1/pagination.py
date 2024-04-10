from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """Enables page size alternating by passing limit in URL params."""

    page_size_query_param = 'limit'
