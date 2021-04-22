from django.conf.urls import url
from . import views
from django.urls import path
from .views import (QuizListView, quiz_view, quiz_data_view, save_quiz_view, show_quiz_result, result_view, user_id, leaderboard, leaderdata, GamesListView)

app_name = 'quiz'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list-view'),
    path('home/', GamesListView.as_view(), name='game-list-view'),
    # the pk value that we will be using further should be displayed in the url
    path('<int:pk>/', views.quiz_view, name='quiz-view'),
    path('<int:pk>/data/', views.quiz_data_view, name='quiz-data-view'),
    path('<int:pk>/save/', views.save_quiz_view, name='save-view'),
    path('<int:pk>/res/', views.result_view, name='result-view'),
    path('<int:pk>/res/result/', views.show_quiz_result, name='quiz-result'),
    path('user/', views.user_id, name='user-id'),
    path('leaderboard/user/', views.user_id, name='user-id'),
    path('home/user/', views.user_id, name='user-id'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('leaderboard/leaderdata/', views.leaderdata, name='leaderboard'),
]