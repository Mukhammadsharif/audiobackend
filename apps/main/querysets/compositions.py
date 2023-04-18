from core.querysets.base_queryset import BaseQuerySet


class CompositionQuerySet(BaseQuerySet):
    def list(self, search=None, reverse=None, catalog=None):
        query = self.filter(catalog=catalog) if catalog else self
        query = self.filter(title__icontains=search) if search else query
        if reverse:
            query = self.all().order_by('id') if reverse else query.order_by('-id')
        return query
