#
import random, time, socket

host = "a78d302f21bc1951.247ctf.com"
port = 50011

def ask_server():
    data_received = s.recv(1024)
    return data_received.decode('utf-8')

def answer_server(my_answer):
    client_answer = my_answer.encode('utf-8')
    s.send(client_answer)
    pass

# useless and not used
def generateWinNum():
        secret = random.Random()
        t = int(time.time()+1)
        secret.seed(t)
        winning_choice = str(secret.random())
        # self.request.sendall("Can you guess the number to win the flag lottery?\n")
        #your_choice = self.request.recv(1024).strip()
        #if winning_choice == your_choice:
        #    self.request.sendall("Congratulations you won the lottery! Have a flag!\n")
        #    self.request.sendall("%s\n" % open('flag.txt').readline().rstrip())
        #else:
        #    self.request.sendall("Nope! The winning number was %s, better luck next time!\n" % winning_choice)
        return winning_choice

while True:
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect((host, port))
    server_response = ask_server()
    print(server_response)
    # can be removed
    # my_num= generateWinNum()
    #print("My number: %s" % my_num)
    answer_server("1")
    the_correct_answer = ask_server()
    the_correct_number = the_correct_answer.split(' ')
    # get server's number from response
    my_cheat_number = the_correct_number[5].rstrip(',')
    print("Closing connection with the server and pushing the correct answer %s again... " % my_cheat_number)
    s.close()
    # reconnect 
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect((host, port))
    server_response = ask_server()
    print(server_response)
    # feed the cheat number for the server
    answer_server(my_cheat_number)
    server_response2 = ask_server()
    if (server_response2.split(' ')[0] == "Congratulations"):
        print(ask_server())
        print(ask_server())
        break;
    s.close()
s.close()
