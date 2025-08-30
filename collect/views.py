from rest_framework import viewsets, permissions
from .models import Collect
from .serializers import CollectSerializer

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Collect

class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

@cache_page(60 * 15)  # Кешируем на 15 минут (900 секунд)
def collect_list(request):
    collects = Collect.objects.all()
    return render(request, 'collect/collect_list.html', {'collects': collects})
