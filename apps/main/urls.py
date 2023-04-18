from django.urls import path

from main.views.authors import AuthorListView, AuthorDetailView
from main.views.catalog import CatalogListView, CatalogDetailView
from main.views.compositions import CompositionListView, CompositionDetailView
from main.views.deferred import DeferredListView, DeferredDetailView
from main.views.liked import LikedListView, LikedDetailView

urlpatterns = [
    path('authors', AuthorListView.as_view(), name='authors-list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='authors-detail'),
    path('composition', CompositionListView.as_view(), name='composition-list'),
    path('composition/<int:pk>', CompositionDetailView.as_view(), name='composition-detail'),
    path('liked', LikedListView.as_view(), name='liked-list'),
    path('liked/<int:pk>', LikedDetailView.as_view(), name='liked-detail'),
    path('deferred', DeferredListView.as_view(), name='deferred-list'),
    path('deferred/<int:pk>', DeferredDetailView.as_view(), name='deferred-detail'),
    path('catalog', CatalogListView.as_view(), name='catalog-list'),
    path('catalog/<int:pk>', CatalogDetailView.as_view(), name='catalog-detail'),
]
