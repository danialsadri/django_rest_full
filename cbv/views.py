from rest_framework import mixins, generics
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from .pagination import StandardResultsSetPagination, LargeResultsSetPagination


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = StandardResultsSetPagination


class CarRetrieveView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'my_name'


class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'my_name'


class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'my_name'


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'my_name'


# class CarGenericView(generics.GenericAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer_data = self.get_serializer(instance)
#         return Response(data=serializer_data.data)

class CarGenericView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.name == 'ferrari':
            return Response('Sorry..')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
