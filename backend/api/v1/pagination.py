from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """Включает изменение размера страницы """

    page_size_query_param = 'limit'
