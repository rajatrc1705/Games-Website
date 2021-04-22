from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from .models import Quiz
from .models import Home
from questions.models import Question
from questions.models import Answer
from results.models import Result
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class GamesListView(LoginRequiredMixin, ListView):

    login_url = '/login'
    model = Home
    template_name = 'quiz/home.html'

class QuizListView(LoginRequiredMixin, ListView):
    
    login_url = '/login'
    model = Quiz
    template_name = 'quiz/main.html'

# we will get pk value from the url

# @login_required(login_url='/login')
# def game_urls():
    


@login_required(login_url='/login')
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quiz.html', {'obj': quiz})

# quiz.html should be fed with proper questions and answers

@login_required(login_url='/login')
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = list()
    for q in quiz.get_questions():
        answers = list()
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
        
    return JsonResponse({
        'data': questions
    })

@login_required(login_url='/login')
def save_quiz_view(request, pk):
    
    if request.is_ajax():
        data = request.POST
        all_questions = list()
        data = dict(data)
        data.pop('csrfmiddlewaretoken')
        
        for k in data.keys():
            print(f"Key: {k} - Value: {data[k]}")
            try:    
                question = Question.objects.get(text=k)
            except:
                print("ERROR AT THIS KEY : ", k)
                question = k
            all_questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score=0
        multiplier = quiz.maximum_marks / quiz.num_of_questions
        results = []
        correct_answer = None

        for q in all_questions:
            answer_selected = request.POST.get(str(q))
            correct_answer = Answer.objects.filter(question=q).filter(correct=True)
            if str(answer_selected) == str(correct_answer[0]):
                score += multiplier
            else:
                print(f"{answer_selected} - {correct_answer[0]}")
        print(f"Your Score : {score}/{quiz.maximum_marks}")

        try:
            user = Result.objects.filter(user=user).user
            user_score = Result.objects.filter(user=user).score
            if user_score < score:
                Result.objects.filter(user=user).delete() 
                Result.objects.create(quiz=quiz, user=user, score=score)
        except:    
            Result.objects.create(quiz=quiz, user=user, score=score)
                
        return JsonResponse({
            'user': str(user), 'score': score
        })

@login_required(login_url='/login')
def result_view(request, pk):
    user = request.user
    result = Result.objects.filter(user=user)
    return render(request, 'quiz/result.html', {'obj': result})

@login_required(login_url='/login')
def show_quiz_result(request, pk):
    quiz=Quiz.objects.get(pk=pk)
    user = request.user
    results=Result.objects.filter(user=user)
    maximum = -1
    score = results[len(results)-1].score
    print("Result: ", results[len(results)-1].score)
    marks_each_question = quiz.maximum_marks/quiz.num_of_questions
    print("Marks each question ", marks_each_question)
    correct=score/marks_each_question
    data = dict()

    data['Username'] = str(user)
    data['Questions Correct'] = correct
    data['Score'] = score
    data['Maximum Marks'] = quiz.maximum_marks
    data['Date'] = str(str(results[len(results)-1].date).split('T')[0]).split(' ')[0]
    return JsonResponse({
        'data': data
    })

@login_required(login_url='/login')
def user_id(request):
    user = request.user
    data = str(user)
    
    return JsonResponse({
        'data': data
    })

@login_required(login_url = '/login')
def leaderboard(request):

    user = request.user
    # for user in all_users:
    #     print()
    return render(request, 'quiz/leaderboard.html', {'user': user})
    # return JsonResponse({'data': data})

def leaderdata(request):
    all_users = Result.objects.filter(user__username__startswith="").distinct()
    users = set()
    quizes = set()
    all_quizes = Quiz.objects.all()
    for q in all_quizes:
        quizes.add(q.quiz_name)
    for i in all_users:
        users.add(i.user)
        
    print(users)
    data = dict()
    for i in all_users:
        data[str(i.user)] = [str(i.user), -1] 
    for i in users:
        total_score = 0
        print(i)
        for q in quizes:
            user_result = Result.objects.filter(user__username__startswith=i).earliest('date')
            try:
                quiz_wise = Result.objects.filter(user__username__startswith=i).filter(quiz__quiz_name__startswith=q).earliest('date')
                print(quiz_wise.score, quiz_wise.quiz)
                total_score += quiz_wise.score
            except:
                print("Not Attempted")
            
            # print(f"QUIZ NAME: {Result.objects.filter(quiz__quiz_name__startswith=q).earliest('date')}")
            
            data[str(user_result.user)] = total_score
    data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    print(data)
    return JsonResponse({
        'data': data
    })
