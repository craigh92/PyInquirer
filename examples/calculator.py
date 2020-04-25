from PyInquirer import prompt
import math

questions = [
    {
        'type' : 'list',
        'name' : 'operation',
        'message' : 'Choose operation',
        'choices' : [
            {
                'name' : 'Add',
                'callback' : lambda answers: print("The answer is: " + str(float(answers['first_value']) + float(answers['second_value']))) # callbacks are not called untill every prompt has been asked
            },
            {
                'name' : 'Subtract',
                'callback' : lambda answers: print("The answer is: " + str(float(answers['first_value']) - float(answers['second_value']))) # callbacks are not called untill every prompt has been asked
            },
            {
                'name' : 'Sin',
                'callback' : lambda answers: print("The answer is: " + str(math.sin(float(answers['first_value'])))) # callbacks are not called untill every prompt has been asked
            },
            {
                'name' : 'Exit',
                'callback' : lambda x: print("Goodbye!")
            }
        ]
    },
    {
        'type' : 'input',
        'name' : 'first_value',
        'message' : 'Enter First Value',
        'when' : lambda answers : answers['operation'] in ['Add', 'Subtract', 'Sin']
    },
    {
        'type' : 'input',
        'name' : 'second_value',
        'message' : 'Enter second Value',
        'when' : lambda answers : answers['operation'] in ['Add', 'Subtract'],
    }
]

answers = prompt(questions)