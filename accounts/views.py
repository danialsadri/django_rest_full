from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .serializers import UserRegisterSerializer, UserSerializer


class UserRegister(APIView):
    def post(self, request):
        serializer_data = UserRegisterSerializer(data=request.POST)
        if serializer_data.is_valid():
            serializer_data.create(serializer_data.validated_data)
            return Response(data=serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def list(self, request):
        serializer_data = UserSerializer(instance=self.queryset, many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer_data = UserSerializer(data=request.POST)
        if serializer_data.is_valid():
            serializer_data.create(serializer_data.validated_data)
            return Response(data=serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, reqeust, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer_data = UserSerializer(instance=user)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permission denied': 'you are not the owner'})
        serializer_data = UserSerializer(instance=user, data=request.POST)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(data=serializer_data.data, status=status.HTTP_200_OK)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permission denied': 'you are not the owner. '})
        serializer_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(data=serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permission denied': 'you are not the owner. '})
        user.is_active = False
        user.save()
        return Response(data={'message': 'user deactivated'})
