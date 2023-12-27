from rest_framework import serializers
from .models import Question, Answer


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionsSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)

    # user = UserEmailRelationalField(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "user", "title", "slug", "body", "created", "updated", "answers"]

    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
