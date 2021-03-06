import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  CORS(app, resources={"/": {'origins': '*'}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  @app.route('/categories')
  def retrive_categories():
    try:
      categories = {}
      for category in Category.query.all():
        categories[category.id] = category.type

      return jsonify({
        'success': True,
        'categories': categories
      }), 200
    except:
      abort(500)

  @app.route('/questions')
  def retrive_questions():
    try:
      categories = {}
      for category in Category.query.all():
        categories[category.id] = category.type
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE
      questions = [question.format() for question in Question.query.all()]
      questions = questions[start:end]
      if (len(questions) < 1):
          abort(502)
      return jsonify({
        'success': True,
        'questions': questions,
        'total questions': len(questions),
        'categories': categories
      }), 200
    except:
      abort(502)

  @app.route('/questions/<int:id>', methods=['DELETE'])
  def question_delete(id):
    try:
      question = Question.query.get(id)
      question.delete()
      return jsonify({
        'success': True,
        'message': 'question deleted',
        'question': id
      }), 200
    except:
      abort(503)

  @app.route('/questions', methods=['POST'])
  def question_create():
    data = request.get_json()
    try:
      question = data.get('question')
      answer = data.get('answer')
      category = data.get('category')
      difficulty = data.get('difficulty')
      if question is None or answer is None:
        abort(501)
      question = Question(question = question, answer = answer, difficulty = difficulty, category=category)
      question.insert()
      return jsonify({
        'success': True,
        'message': 'question was added'
      }), 200
    except:
      abort(504)

  @app.route('/questions/search', methods=['POST'])
  def search():
    data = request.get_json()
    try:
      searchTerm = data.get('searchTerm')
      if searchTerm is None:
        abort(501)
      filter_questions = Question.query.filter(Question.question.ilike('%'+ searchTerm + '%')).all()
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE
      questions = [question.format() for question in filter_questions]
      questions = questions[start:end]
      if questions == []:
        abort(500)
      else:
        return jsonify({
          'success': True,
          'questions': questions,
          'total questions': len(questions)
        }), 200
    except:
      abort(500)

  @app.route('/categories/<int:id>/questions')
  def questions_in_category(id):
    try:
      questions = Question.query.filter_by(category=id).all()
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE
      questions = [question.format() for question in questions]
      questions = questions[start:end]
      if len(questions) == 0:
        abort(500)
      return jsonify({
        'success': True,
        'questions': questions,
        'total questions': len(questions)
      }), 200
    except:
      abort(500)

  @app.route('/quizzes', methods=['POST'])
  def play():
    data = request.get_json()
    previous = data.get('previous_questions')
    category = data.get('quiz_category')
    try:
      questions = None
      if category['id'] == 0:
        questions = Question.query.all()
      else:
        questions = Question.query.filter_by(category=category['id']).all()
      while True:
        question = questions[random.randint(0, len(questions) - 1)]
        if len(questions) == len(previous):
          return jsonify({
            'success': True,
            'question': None
          }), 200
        elif question.id in previous:
          continue
        elif len(questions) != len(previous):
          return jsonify({
            'success': True,
            'question': question.format()
          }), 200
        else:
          abort(500)
    except:
      abort(500)

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'resource not found'
    }), 404

  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'unprocessable entity'
    }), 422

  @app.errorhandler(500)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 500,
      'message': 'not getting data'
    }), 500
  @app.errorhandler(501)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 501,
      'message': 'not enough input'
    }), 501
  @app.errorhandler(504)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 504,
      'message': 'issue while adding the question'
    }), 504
  @app.errorhandler(503)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 503,
      'message': 'unable to delete'
    }), 503
  @app.errorhandler(502)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 502,
      'message': 'no question for that page'
    }), 502

  return app

    