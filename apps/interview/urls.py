from django.urls import path

from apps.interview.views import QuizView, CreateQuestionView, RetrieveQuizListView, SubmitQuizView, \
    GetSubmittedUserQuizView, ManageQuestionView, QuizUpdateView, QuizRemoveView

app_name = 'interview'

urlpatterns = [
    path('', QuizView.as_view(), name='create-quiz'),
    path('update/<int:pk>/', QuizUpdateView.as_view(), name='update-quiz'),
    path('remove/<int:pk>/', QuizRemoveView.as_view(), name='remove-quiz'),
    path('question/create/', CreateQuestionView.as_view(), name='create-question'),
    path('question/<int:pk>/manage/', ManageQuestionView.as_view(), name='manage-question'),
    path('active_quizes/', RetrieveQuizListView.as_view(), name='quiz-list'),
    path('submit_quiz/', SubmitQuizView.as_view(), name='submit-quiz'),
    path('user/quiz/<int:user_ident>/', GetSubmittedUserQuizView.as_view(), name='user-submitted-quiz'),
]
