from rest_framework.pagination import LimitOffsetPagination

class SmallPagination(LimitOffsetPagination):
    default_limit = 12
    max_limit = 20
