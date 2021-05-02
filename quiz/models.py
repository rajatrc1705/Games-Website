from django.db import models
import random
# Create your models here.

difficulty = (
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard"),
)

class Quiz(models.Model):
    
    quiz_name = models.CharField(max_length=100)
    num_of_questions = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=10, choices=difficulty,default="Medium")
    time_limit = models.IntegerField(default=10)
    maximum_marks = models.IntegerField(default=10)

    class Meta:
        verbose_name_plural = "Quizes"

    def __str__(self):
        return self.quiz_name 

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.num_of_questions]

class Home(models.Model):

    game_name = models.CharField(max_length=100)
    url = models.URLField(max_length=210, default='https://adoring-hawking-6d5afd.netlify.app/')
    def __str__(self):
        return self.game_name


