from rest_framework import viewsets,mixins,status
from .serializers import ContactSerializer
from .models import contacts
from rest_framework import generics
from rest_framework import filters
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CreateContactView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """View for creating new contacts (post)"""
    queryset = contacts.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetAllContactsView(mixins.ListModelMixin,generics.GenericAPIView):
    """View for listing all contacts"""
    queryset = contacts.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
    @method_decorator(cache_page(60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ContactView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """View for updating, deleting existing contacts"""
    queryset = contacts.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,
    @method_decorator(cache_page(60))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @method_decorator(cache_page(60))
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
