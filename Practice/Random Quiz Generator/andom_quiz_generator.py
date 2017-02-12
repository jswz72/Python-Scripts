#! /usr/bin/python3


import random

capitals_dic = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


#Generate 35 quiz files

for quiz_num in range(35):
    
    quiz_file = open('capitalsquiz%s' % (quiz_num + 1), 'w')
    quiz_key = open('captialsquiz_answers%s' % (quiz_num + 1), 'w')

    quiz_file.write('Name:\n\nDate:\n\n')   #header for each quiz
    quiz_file.write('\n' + (''*20) + 'State Capitals Quiz Form %s' % (quiz_num) + '\n\n')

    #shuffle states
    states = list(capitals_dic.keys())
    random.shuffle(states)

    for i in range(50):

        correct = capitals_dic[states[i]]   #capital match for random state
        wrong_answers = list(capitals_dic.values())
        del wrong_answers[wrong_answers.index(correct)]  #leaves list of only wrong answers

        #make randomized list of 3 wrong answers and the correct answer
        wrong_answers = random.sample(wrong_answers,3)
        options = wrong_answers + [correct]
        random.shuffle(options)
            
            
        quiz_file.write('What is the capital of ' + states[i] + ' ?\n')
        #create options a,b,c,d
        for k in range(4):
             quiz_file.write(' %s: %s\n' % ('ABCD'[k], options[k]))                
        quiz_file.write('\n')
        #add correct ans to answer key
        quiz_key.write('%s: %s\n' % (i, correct))   #add question number and correct answer to answer 

    quiz_file.close()
    quiz_key.close()
                    
        
    
