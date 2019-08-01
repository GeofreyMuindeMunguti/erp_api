from rest_framework import  permissions, filters, status

class DefaultsMixin(object):

    """Default filtering and pagination."""
  
    paginate_by = 25     # Pages of API end points/URLs
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (filters.SearchFilter,)

