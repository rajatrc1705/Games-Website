from django.db import models
from quiz.models import Quiz

# Create your models here.

class Question(models.Model):

    text = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    image = models.URLField(default='https://www.denofgeek.com/wp-content/uploads/2015/02/potter.jpeg?fit=300%2C225')

    def __str__(self):
        # return f"{str(self.text)}|{self.image}"
        return str(self.text)

    def get_image_link(self):
        return self.image
        
    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):

    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)
    
    
