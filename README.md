# Full Stack API Final Project
## Trivia
Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
Delete questions.
Add questions and require that they include question and answer text.
Search for questions based on a text query string.
Play the quiz game, randomizing either all questions or within a specific category.
Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### NPM

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

Change the configration for Postgres in `/backend/models.py`

From within the `backend` directory

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Running Your Frontend

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## Testing
Change the configration for Postgres in `/backend/test_flaskr.py`

To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Reference

### Getting Started

Backend URL: `http://127.0.0.1:5000/`, Frontend URL: `http://127.0.0.1:3000/`

### Error Handling

The error codes:

* 404 – resource not found
* 422 – unprocessable entity
* 500 – not getting data
* 501 – not enough input
* 504 - issue while adding the question
* 503 - unable to delete
* 502 - no question for that page

Errors are in this format:

```json
      {
        "success": "False",
        "error": 404,
        "message": "resource not found",
      }
```

### Endpoints

#### GET /categories

- General: 
  - Returns all available categories.

- Sample:  `curl http://127.0.0.1:5000/categories`

```json
    {
        "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
        }, 
        "success": true
    }
```

#### GET /questions
- General:
  - return a list of questions, number of total questions, current category, categories

- Sample: `curl http://127.0.0.1:5000/questions`

```json
        {
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total questions": 10
}
```

#### DELETE /questions/<int:id\>


- General:
  - Deletes question by using a question ID.

- Sample: `curl http://127.0.0.1:5000/questions/10 -X DELETE`

```json
{
  "message": "question deleted",
  "success": true
}
```

#### POST /questions

- General:
  - Creates a new question.

- Sample: `curl --location --request POST 'http://127.0.0.1:5000/questions' \
--header 'Content-Type: application/json' \
--data-raw '{
    "question": "what'\''s my name?",
    "answer": "yasser",
    "difficulty": 1,
    "category": "1"
}'`

```json
{
    "message": "question was added",
    "success": true
}
```

#### POST /questions/search

- General:
  - return any questions for whom the search term is a substring of the question

- Sample: ` curl --location --request POST 'http://127.0.0.1:5000/questions/search' \
--header 'Content-Type: application/json' \
--data-raw '{
    "searchTerm": "what's my name?"
}' `

```json
{
    "questions": [
        {
            "answer": "yasser",
            "category": 1,
            "difficulty": 1,
            "id": 29,
            "question": "what's my name?"
        }
    ],
    "success": true,
    "total questions": 1
}
```

#### GET /categories/<int:id\>/questions

- General:
  - get questions based on category.
- Sample: `curl http://127.0.0.1:5000/categories/3/questions`

```json
{
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total questions": 3
}

```

#### POST /quizzes

- General
  - Takes the category and previous questions in the request.
  - Return random question not in previous questions.

- Sample: `curl --location --request POST 'http://127.0.0.1:5000/quizzes' \
--header 'Content-Type: application/json' \
--data-raw '{
    "previous_questions": [], 
    "quiz_category": {
        "type": "Art", 
        "id": "2"
    }
}'`

```json
{
    "question": {
        "answer": "Mona Lisa",
        "category": 2,
        "difficulty": 3,
        "id": 17,
        "question": "La Giaconda is better known as what?"
    },
    "success": true
}

```

## Authors
- Yasser Faleh Alharbi