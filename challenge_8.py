# A number of challenges will require you to create solutions which are more efficiently solved by making use of a programming language to automate and perform the computations. 
# For this purpose, we recommend to make use of PYTHON as well as complementary libraries such as REQUESTS and PWNTOOLS.
# If you are not sure where to start with Python, we recommend the introductory PYTHON 101 FOR HACKERS course.
# Click the ‘START CHALLENGE’ button to the right of this text description to start a socket challenge. 
# Utilise a programming language to interface with the socket and automate solving 500 simple addition problems to receive the flag. 
# Take care when interfacing with unknown remote services - '\n' is not the only way to end

import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = "66ce6cf75a126dda.247ctf.com"
port = 50234
url = "tcp://66ce6cf75a126dda.247ctf.com:50234"
number_of_questions = 500

def answerQuestion(msg):
    print("Server message:")
    # server says
    print(msg)
    # split a question into sentences
    strings = msg.split('\r\n')
    if len(strings) > 1:
        # last sentence with numbers
        aQuestion = strings[len(strings)-2]
        print(aQuestion)
        # split question in words
        words = aQuestion.split(' ')
        # get number 1 into int a, get number 2 into b
        a = int(words[5])
        b = int(words[7].rstrip('?'))
        # return arithmetical sum of numbers
        return a + b
    else:
        return strings[len(strings)-1]

s.connect((host, port))

def ask_server():
    data_received = s.recv(1024)
    return data_received


def answer_server(my_answer):
    client_answer = my_answer.encode('utf-8')
    s.send(client_answer)
    pass


for i in range(number_of_questions):
    # receive server response
    print("Question " + str(i+1))
    server_response = ask_server()
    # srv msg is not empty
    # send srv msg to the function and get the answer
    srv_msg = server_response.decode('utf-8')
    myanswer = str(answerQuestion(srv_msg))
    print("My answer: " + myanswer)
    myanswer += "\r\n"
    # send answer to server
    answer_server(myanswer)

print("Your flag:")
print(ask_server().decode('utf-8'))
