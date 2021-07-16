from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.interview.models import Quiz, Question, UserQuiz
from apps.interview.serializers import QuizSerializer, QuestionSerializer, SubmitQuizSerializer, UserQuizSerializer, \
    QuizUpdateSerializer, QuestionCreateSerializer


class QuizView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizUpdateView(generics.UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizUpdateSerializer
    http_method_names = ['put']


class QuizRemoveView(generics.DestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class CreateQuestionView(generics.CreateAPIView):
    serializer_class = QuestionCreateSerializer
    queryset = Question.objects.all()


class ManageQuestionView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    http_method_names = ['put', 'delete']


class RetrieveQuizListView(generics.ListAPIView):
    queryset = Quiz.objects.filter(is_active=True)
    serializer_class = QuizSerializer
    permission_classes = (AllowAny,)


class SubmitQuizView(generics.CreateAPIView):
    serializer_class = SubmitQuizSerializer
    queryset = UserQuiz.objects.all()
    permission_classes = (AllowAny, IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response({'user_quiz': instance.pk}, status=status.HTTP_201_CREATED)


class GetSubmittedUserQuizView(generics.RetrieveAPIView):
    serializer_class = UserQuizSerializer
    queryset = UserQuiz.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'user_ident'
