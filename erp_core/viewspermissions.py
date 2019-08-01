from rest_framework import  permissions, filters, status

class DefaultsMixin(object):

    """Default settings for view authentication, permissions,filtering and pagination."""
    
    #view authentication
    #authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    # view  permissions,
    permission_classes = (permissions.IsAuthenticated,)  # alow only authenticated user to access API End points
    # view  pagination.

    paginate_by = 25     # Pages of API end points/URLs
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    """
    #view  filtering
    #DefaultsMixin now defines the list of available filter_backends , which will enable these for all of the existing ViewSets.
    """
    filter_backends = (filters.SearchFilter,)
    '''
    We configure the SearchFilter by adding a search_fields attribute to each
    ViewSet . We configure the OrderingFilter by adding a list of fields, which can be used
    for ordering the ordering_fields .
    '''
