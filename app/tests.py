from django.http import HttpRequest
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase

from app.models import Question, User

# Create your tests here.

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create( 
            question = 'What is your name?', 
            answer = 'My name is John',
            resA = 'A',
            resB = 'B',
            resC = 'C',
            resD = 'D',
            highlight = 'A',
            image = 'image.jpg',
            timeLimit = 123,
            definitions = 'A: John, B: Doe, C: Smith, D: Doe')

    def test_get_question_list(self):
        response = self.client.get('/questions', **{'HTTP_Access-Code': 'test'})
        self.assertEqual(response.status_code, 200) 
    
    def test_get_question_list_fail(self):
        response = self.client.get('/questions', **{'HTTP_Access-Code': 'fail'})
        self.assertEqual(response.status_code, 404)

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create( 
        id = 1, 
        username = 'A', 
        email = 'a@a.com', 
        score = 0, 
        accessCode = 'test')

    def test_get_user_id(self):
        response = self.client.post('/getuser', {'username': 'A'})
        print(response.request)
        self.assertEqual(response.status_code, 200)