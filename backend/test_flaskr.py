import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        ######################################################################
        ############## Change username and password and whatever you need ##########################
        username = "postgres"
        password = "2021"
        self.database_path = "postgresql://{}:{}@{}/{}".format(username, password,'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_retrive_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_retrive_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total questions'])
        self.assertTrue(data['categories'])

    def test_delete_question(self):
        question = Question.query.first()
        response = self.client().delete('/questions/{}'.format(question.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'question deleted')

    def test_retrive_questions_wrong_page(self):
        response = self.client().get('/questions?page=200')
        data = json.loads(response.data)
        self.assertEqual(response.status_code,502)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'no question for that page')
    
    def test_create_question(self):
        response = self.client().post('/questions', json={
            'question': 'what is my name',
            'answer': 'Fox',
            'category': 4,
            'difficulty': 2
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'question was added')

    def test_quiz(self):
        response = self.client().post('/quizzes', json={
            'previous_questions': [], 
            'quiz_category': {
                'type': "Art", 
                'id': "4"
                }})
        
        data = json.loads(response.data)
        print(data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_search(self):
        response = self.client().post('/questions/search', json={'searchTerm': 'h'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total questions'])

    def test_questions_in_category(self):
        response = self.client().get('/categories/4/questions')
        data = json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total questions'])





# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()