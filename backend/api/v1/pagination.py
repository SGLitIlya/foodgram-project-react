from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """Включает изменение размера страницы 
       путем передачи ограничения в параметрах URL-адреса.
    """

    page_size_query_param = 'limit'
