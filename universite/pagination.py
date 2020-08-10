from rest_framework.pagination import PageNumberPagination



class PostPageNUmberPagination(PageNumberPagination):
    page_size = 5