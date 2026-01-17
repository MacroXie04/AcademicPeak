from rest_framework import viewsets, generics
from rest_framework.response import Response
from ..models import Menu, Page
from ..serializers import MenuSerializer, PageListSerializer, PageDetailSerializer


class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns the menu tree structure.
    Only returns root menus (parent=None), children are nested.
    """
    queryset = Menu.objects.filter(parent__isnull=True, is_active=True).order_by('order')
    serializer_class = MenuSerializer
    pagination_class = None


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all().order_by('-created_at')
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PageDetailSerializer
        return PageListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        menu_id = self.request.query_params.get('menu_id')
        if menu_id:
            # Optionally filter by menu including children if needed,
            # for now just direct match or basic filter
            queryset = queryset.filter(menu_id=menu_id)
        return queryset

