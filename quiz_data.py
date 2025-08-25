import random

def get_questions():
    data = {
        "Python": [
            {"q": "What is the output of print(2**3)?", "options": ["6", "8", "9", "5"], "answer": "8"},
            {"q": "Which keyword is used for function?", "options": ["def", "func", "define", "function"], "answer": "def"},
            {"q": "Which is NOT a Python data type?", "options": ["List", "Tuple", "Set", "Array"], "answer": "Array"},
            {"q": "What does len() function do?", "options": ["Adds numbers", "Returns length", "Converts to string", "Prints output"], "answer": "Returns length"},
            {"q": "Which symbol is used for comments in Python?", "options": ["//", "<!-- -->", "#", "/* */"], "answer": "#"},
            {"q": "What is the output of print(type(10))?", "options": ["<class 'float'>", "<class 'str'>", "<class 'int'>", "<class 'bool'>"], "answer": "<class 'int'>"},
            {"q": "Which of these is a valid variable name?", "options": ["2value", "value_2", "value-2", "value 2"], "answer": "value_2"},
            {"q": "Which data type stores True/False values?", "options": ["int", "str", "bool", "float"], "answer": "bool"},
        ],
        "General Knowledge": [
            {"q": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome"], "answer": "Paris"},
            {"q": "Who wrote Hamlet?", "options": ["Dickens", "Shakespeare", "Twain", "Hemingway"], "answer": "Shakespeare"},
            {"q": "H2O is the chemical formula for?", "options": ["Oxygen", "Hydrogen", "Water", "Salt"], "answer": "Water"},
            {"q": "Which continent is the largest by area?", "options": ["Africa", "Asia", "Europe", "Antarctica"], "answer": "Asia"},
            {"q": "Which organ pumps blood in the human body?", "options": ["Brain", "Liver", "Heart", "Kidney"], "answer": "Heart"},
            {"q": "Which gas do plants absorb from the air?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"q": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "India", "Thailand"], "answer": "Japan"},
            {"q": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
        ],
        "Sports": [
            {"q": "How many players in a soccer team?", "options": ["9", "10", "11", "12"], "answer": "11"},
            {"q": "Where are the Olympics held every 4 years?", "options": ["Same city", "Different cities", "London", "Rome"], "answer": "Different cities"},
            {"q": "What sport is Serena Williams famous for?", "options": ["Basketball", "Tennis", "Golf", "Football"], "answer": "Tennis"},
            {"q": "How many rings are there in the Olympic symbol?", "options": ["4", "5", "6", "7"], "answer": "5"},
            {"q": "Which sport uses a bat and ball?", "options": ["Football", "Tennis", "Cricket", "Swimming"], "answer": "Cricket"},
            {"q": "Which country invented football (soccer)?", "options": ["Brazil", "England", "Germany", "Spain"], "answer": "England"},
            {"q": "How many points is a touchdown worth in American football?", "options": ["3", "6", "7", "10"], "answer": "6"},
            {"q": "Which sport is played at Wimbledon?", "options": ["Golf", "Tennis", "Rugby", "Baseball"], "answer": "Tennis"},
        ],
        "Interesting Topic": [
            {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
            {"q": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Rhino"], "answer": "Blue Whale"},
            {"q": "Which is the fastest land animal?", "options": ["Lion", "Cheetah", "Leopard", "Tiger"], "answer": "Cheetah"},
            {"q": "Which animal is known for changing its color?", "options": ["Chameleon", "Tiger", "Elephant", "Kangaroo"], "answer": "Chameleon"},
            {"q": "Which planet has the most moons?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Jupiter"},
            {"q": "What is the tallest mountain in the world?", "options": ["K2", "Everest", "Kilimanjaro", "Alps"], "answer": "Everest"},
            {"q": "Which bird is known for its beautiful tail feathers?", "options": ["Crow", "Parrot", "Peacock", "Eagle"], "answer": "Peacock"},
            {"q": "Which element is most abundant in the Earth's crust?", "options": ["Iron", "Oxygen", "Silicon", "Carbon"], "answer": "Oxygen"},
        ]
    }

    # Shuffle questions and options for each topic
    for topic in data:
        random.shuffle(data[topic])  # Shuffle question order
        for question in data[topic]:
            random.shuffle(question["options"])  # Shuffle options

    return data

def calculate_score(selected_answers, questions):
    score = 0
    for idx, ans in enumerate(selected_answers):
        if ans == questions[idx]["answer"]:
            score += 1
    return score

def get_feedback(score, total):
    if score == total:
        return "Excellent!"
    elif score >= total // 2:
        return "Good Try!"
    else:
        return "Keep Practicing!"
