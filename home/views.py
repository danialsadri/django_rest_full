from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionsSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from permissions import IsOwnerOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework import serializers


# class Home(APIView):
#     def get(self, request):
#         # name = request.GET.get('name')
#         name = request.query_params.get('name')
#         return Response({'name': name})
#
#     def post(self, request):
#         name = request.data.get('name')
#         return Response({'name': name})

class Home(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    """this is home page"""

    def get(self, request):
        persons = Person.objects.all()
        serializer_data = PersonSerializer(instance=persons, many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)


class QuestionListView(APIView):
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # throttle_scope = 'contacts'
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all()
        page_number = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('limit', 2)
        paginator = Paginator(object_list=questions, per_page=page_size)
        serializer_data = QuestionsSerializer(instance=paginator.page(page_number), many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
    create a new questions.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionsSerializer

    def post(self, request):
        serializer_data = QuestionsSerializer(data=request.POST)
        if serializer_data.is_valid():
            serializer_data.save(user=request.user)
            return Response(data=serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, question_id):
        questions = Question.objects.get(pk=question_id)
        self.check_object_permissions(request, questions)
        serializer_data = QuestionsSerializer(instance=questions, data=request.POST, partial=True)
        if serializer_data.is_valid():
            serializer_data.save(user=request.user)
            return Response(data=serializer_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'message': 'question deleted. '})
