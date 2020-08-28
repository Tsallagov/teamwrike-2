import sys
from model_v1_test import Model_v1

answered = False
another_q = False

model = Model_v1()
model.fit_transform('how_to_data.csv')

def response(msg):
    global answered, another_q, end
    msg = msg.lower()
    if(msg == '/start'):
        answered = False
        another_q = False
        return 'Hello there! Try to put your question in one sentence. '\
        'Collect only the most necessary information in it, without words of greetings and thanks - '\
        'thus I better find the answer to the question. '\
        'An example of a good question for me: "How to create a task"'
    else:
        if(answered == False):
            title, answer = model.predict(msg)
            answered = True
            return title + '\n' + answer + '\n\nDid I answer your question?'
        if(answered == True and another_q == False):
            if(msg == 'no'):
                return "Sorry( It looks like I'm still stupid to work here. Adding a human to the chat."
            elif(msg == 'yes'):
                another_q = True
                return 'Nice! Do you have another question?'
            else:
                return 'Sorry, I don\'t get you. Please answer "Yes" or "No"'
        if(another_q == True):
            if (msg == 'no'):
                return "Good luck! Thank you for using Wrike!"
                answered = False
                another_q = False
            elif (msg == 'yes'):
                answered = False
                another_q = False
                return 'Okay, I am listening you'
            else:
                return 'Sorry, I don\'t get you. Please answer "Yes" or "No"'


print(response(sys.argv[1]))
print(response(sys.argv[2]))
print(response(sys.argv[3]))
print(response(sys.argv[4]))
print(response(sys.argv[5]))