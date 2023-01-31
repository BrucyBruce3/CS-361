# Author: Bruce Curtis
# Date: 01/30/2023
# Description: Thieves Thebes
#              Trivia Game that allows a player to player, a teacher to manage questions, and an admin to manage the game.

class Game:

    def __init__(self):
        self._topics = [["Mathematics",[["What is the hypotenuse of a right angle that has one leg of 100 ft and another of 240 ft?","260"],["Perimeter of 100 square feet square","40"],["Volume of a 300 ft tall pyramid with a 100 square foot base","10000"]]],
                        ["Egyptian History",[["Egyptian Queen who loved Marc Antony","Cleopatra"],["Colloquial name of Famous Pharoah whose remains were discovered in 1922","King Tut"],["City of the Famous Library built by Alexander the Great","Alexandria"]]],
                        ["Egyptian Mythology",[["God of the Sun","Ra"],["God of the Underworld","Osiris"],["God of fertility","Min"]]]]
        self._questions_to_prize = 3
        self._user_types = ["Player","Teacher","Administrator"]
        self._passwords = ["teach","manage"]
        self._game_name = ["Thebes Thieves"]

    def get_questions_to_prize(self):
        "Method to return the required correct answers to get a prize"
        return self._questions_to_prize

    def get_topics(self):
        "Method to get the topics in the game"
        for topic in self._topics:
            print(topic[0])

    def remove_topic(self,number):
        "Method to remove the topics in a game"
        self._topics.pop(number)

    def update_topic(self,topic_number,new_topic):
        "Method to update a topic. Not currently used in the code"
        self._topics[topic_number][0] = new_topic

    def update_question(self, topic_number,question_num,question,answer):
        "Method to update a question. Not currently used in the code"
        self._topics[topic_number-1][1][question_num-1][0] = question
        self._topics[topic_number-1][1][question_num-1][1] = answer

    def remove_question(self, topic_number,question_number):
        "Method to update a question. Not currently used in the code"
        self._topics[topic_number][1][question_number].remove()

    def print_topics(self):
        "Method to print the available topics."
        for int in range(len(self._topics)):
            print(f"{int+1}. {self._topics[int][0]}")

    def get_question(self,topic_number,question_number):
        "Method to get a question. Not currently used in the code"
        return self._topics[topic_number][1][question_number][0]

    def get_questions(self,topic_number):
        "Method to get all the questions for a topic. Not currently used in the code"
        question_list = []
        for question in self._topics[topic_number][1]:
            question_list.append(question[0])
        return question_list

    def print_questions(self,topic_number):
        "Method to print the questions for a given topic."
        question_list = self.get_questions(topic_number)
        for int in range(len(question_list)):
            print(str(int + 1) + ". " + question_list[int])

    def get_answer(self,topic_number,question_number):
        "Method to get an answer for a given question. Not used in the code."
        return self._topics[topic_number][1][question_number][1]

    def print_user_types(self):
        "Method to get print the user types."
        for int in range(0,len(self._user_types)):
            print(str(int + 1) + ". " + self._user_types[int])

game = Game()

def user_type_intro(game,name):
    "Introduction method that assigns the user to a user type."

    game.print_user_types()
    print("4. Main Menu")
    print("5. Exit")
    user_type = input()
    if user_type == str(1):
        questions_answered = 0
        answered_list = [[0,0,0],[0,0,0],[0,0,0]]
        print(f"Answer {game.get_questions_to_prize()} questions to find the treasure!!")
        answer = input("Continue? Y/N\n")
        if answer == "N" or answer == "n":
            main()
        elif answer == "Y" or answer == "y":
            player_intro(game, name, questions_answered,answered_list)
    elif user_type == str(2):
        teacher_intro(game,name)
    elif user_type == str(3):
        print("Welcome Admin!")
        administrator_intro(game,name)
    elif user_type == str(4):
        main()
    elif user_type == str(5):
        return
    else:
        print("Please enter one of the available numbers.")
        user_type_intro(game, name)

def player_intro(game,name,questions_answered,answered_list):
        "Introduces a player type by first showing available topics."

        print(f"Hi {name}, here are the available question topics")
        game.print_topics()
        print("4. Back")
        print("5. Main Menu")
        print("6. Exit")
        topic = input()
        if topic == str(1) or topic == str(2) or topic == str(3):
            player_questions(game, name,int(topic),questions_answered,answered_list)
        elif topic == str(4):
            player_intro(game, name,questions_answered,answered_list)
        elif topic == str(5):
            main()
        elif topic == str(6):
            return

def player_questions(game,name,topic,questions_answered,answered_list):
    "Shows questions for a user."

    print(f"{game._topics[topic-1][0]}\n")

    game.print_questions(topic-1)
    print("4. Back")
    print("5. Main Menu")
    print("6. Exit")
    question = input()
    if question == str(1) or question == str(2) or question == str(3):
        player_show_question(game, name,int(topic),int(question),questions_answered,answered_list)
    elif question == str(4):
        player_intro(game, name,questions_answered,answered_list)
    elif question == str(5):
        main()
    elif question == str(6):
        return

def player_show_question(game,name,topic,question,questions_answered,answered_list):
    "Gives options for the user for a specific question."

    print(f"{game._topics[topic-1][0]}\n")

    print(game._topics[topic-1][1][question-1][0]+"\n")
    print("1. Answer Question")
    print("2. Back")
    print("3. Main Menu")
    print("4. Exit")

    decision = input()

    if decision == str(1) and answered_list[topic-1][int(question-1)] == 0:
        player_answer_question(game, name,topic,int(question),questions_answered,answered_list)
    if decision == str(1) and answered_list[topic-1][int(question-1)] == 1:
        print("Please select another question\n")
        player_questions(game, name,topic,questions_answered,answered_list)
    elif decision == str(2):
        player_questions(game, name,topic,questions_answered,answered_list)
    elif decision == str(3):
        main()
    elif decision == str(4):
        return

def player_answer_question(game, name,topic,question_num,questions_answered,answered_list):
    "Method for the user to answer a question"

    print(f"{game._topics[topic-1][0]}\n")

    print(game._topics[topic-1][1][question_num-1][0]+"\n")

    print("Please do not include units")

    answer = input()

    if str(answer) == str(game._topics[topic-1][1][question_num-1][1]):
        questions_answered += 1
        if questions_answered == game._questions_to_prize:
            answered_list[topic - 1][int(question_num-1)] = 1
            print("Congratulations, you've found the Ancient Treasure!!\n")
            main()
        if questions_answered < game._questions_to_prize:
            answered_list[topic - 1][int(question_num-1)] = 1
            print("Congratulations, you're one step closer to the treasure!!\n")
            player_questions(game,name,topic,questions_answered,answered_list)
    else:
        print("Sorry that is incorrect.\n")
        print("1. Try Again")
        print("2. Back")
        print("3. Main Menu")
        print("4. Exit")
        decision = input()

        if decision == str(1):
            player_answer_question(game, name,topic,question_num,questions_answered)
        elif decision == str(2):
            player_show_question(game,name,topic,question_num,questions_answered)
        elif decision == str(3):
            main()
        elif decision == str(4):
            return


def teacher_intro(game,name):
        "Introduction for the teacher user type."

        password = input("Please enter teacher password: ")
        if password != game._passwords[0]:
            print("1. Enter Teacher Password Again")
            print("2. Main Menu")
            print("3. Exit")
            decision = input()
            if decision == str(1):
                teacher_intro(game,name)
            elif decision == str(2):
                main()
            elif decision == str(3):
                return
        else:
            print("Please select one of the options below")
            print("1. Update Teacher Password")
            print("2. Question Topics")
            print("3. Back")
            print("3. Main Menu")
            print("4. Exit")

            decision = input()
            if decision == str(1):
                teacher_update_password(game,name)
            elif decision == str(2):
                teacher_topics(game,name)
            elif decision == str(3):
                teacher_intro(game,name)
            elif decision == str(4):
                main()
            elif decision == str(5):
                return
            else:
                print("Please try again")
                teacher_intro(game,name)

def teacher_update_password(game,name):
    "Method for a teacher to update the teacher password."

    print("Please enter the new teacher password below: ")
    old_password = game._passwords[0]
    new_password = input()
    game._passwords[0] = new_password
    print("Success, the password has been updated\n")

    print("1. Undo New Password")
    print("2. Back")
    print("3. Main Menu")
    print("4. Exit")

    decision = input()
    if decision == str(1):
        game._passwords[0] = old_password
        teacher_update_password(game,name)
    elif decision == str(2):
        teacher_intro(game, name)
    elif decision == str(4):
        main()
    elif decision == str(5):
        return
    else:
        print("Please try again")
        teacher_update_password(game, name)

def teacher_topics(game,name):
            "Method to show a teacher the available question topics."

            print(f"Hi {name}, here are the available question topics")
            game.print_topics()
            print("4. Back")
            print("5. Main Menu")
            print("6. Exit")
            topic = input()
            if topic == str(1) or topic == str(2) or topic == str(3):
                teacher_questions(game, name,int(topic))
            elif topic == str(4):
                teacher_intro(game, name)
            elif topic == str(5):
                main()
            elif topic == str(6):
                return

def teacher_questions(game,name,topic):
    "Method to show a teacher the available questions for a given topic."

    print(f"{game._topics[topic-1][0]}\n")

    game.print_questions(topic-1)
    print("4. Back")
    print("5. Main Menu")
    print("6. Exit")
    question = input()
    if question == str(1) or question == str(2) or question == str(3):
        teacher_show_question(game, name,int(topic),int(question))
    elif question == str(4):
        teacher_intro(game, name)
    elif question == str(5):
        main()
    elif question == str(6):
        return
    else:
        print("Please try again")

def teacher_show_question(game,name,topic,question):
    "Method to show a teacher the available options for a given question."

    print(f"{game._topics[topic-1][0]}\n")

    print(game._topics[topic-1][1][question-1][0]+"\n")
    print("1. Edit Question / Answer")
    print("2. Delete Question")
    print("3. Back")
    print("4. Main Menu")
    print("5. Exit")

    decision = input()

    if decision == str(1):
        teacher_edit_question(game, name,topic,int(question))
    if decision == str(2):
        teacher_delete_question(game, name,topic,int(question))
    elif decision == str(3):
        teacher_questions(game, name,topic)
    elif decision == str(4):
        main()
    elif decision == str(5):
        return

def teacher_edit_question(game, name,topic,question):
    "Method to allow a teacher to edit a question."

    print(f"{game._topics[topic-1][0]}\n")

    print(game._topics[topic-1][1][question-1][0]+"\n")

    old_question = game._topics[topic-1][1][question-1][0]
    old_answer = game._topics[topic-1][1][question-1][1]
    print("Please enter the updated question below. If null, question won't be updated.\n")

    new_question = input()

    print("Please enter the updated answer below. If null, question won't be updated.\n")

    new_answer = input()

    if new_question != "":
        game._topics[topic - 1][1][question - 1][0] = new_question
    if new_answer != "":
        game._topics[topic - 1][1][question - 1][1] = new_answer

    print(f"{game._topics[topic-1][0]}\n")

    print(game._topics[topic-1][1][question-1][0]+"\n")

    if new_question != "" or new_answer != "":
        print("1. Undo Changes")
        print("2. Back")
        print("3. Main Menu")
        print("4. Exit")

        decision = input()

        if decision == str(1):
            game._topics[topic - 1][1][question - 1][0] = old_question
            game._topics[topic - 1][1][question - 1][1] = old_answer
            teacher_show_question(game, name, topic, question)
        elif decision == str(2):
            teacher_show_question(game,name,topic,question)
        elif decision == str(3):
            main()
        elif decision == str(4):
            return


def teacher_delete_question(game, name, topic, question):
    "Method to allow a teacher to delete a question."

    print(f"{game._topics[topic - 1][0]}\n")

    print(game._topics[topic - 1][1][question - 1][0] + "\n")

    old_question = game._topics[topic - 1][1][question - 1][0]
    old_answer = game._topics[topic - 1][1][question - 1][1]
    print("Please confirm if you'd like to delete the question.\n")

    print("1. Delete Question")
    print("2. Back")
    print("3. Main Menu")
    print("4. Exit")

    decision = input()

    if decision == str(1):
            game._topics[topic - 1][1][question - 1][0] = "Empty"
            game._topics[topic - 1][1][question - 1][1] = ""
            print("1. Undo Question Deletion")
            print("2. Back")
            print("3. Main Menu")
            print("4. Exit")

            decision = input()
            if decision == str(1):
                game._topics[topic - 1][1][question - 1][0] = old_question
                game._topics[topic - 1][1][question - 1][1] = old_answer
                teacher_show_question(game, name, topic, question)
            elif decision == str(2):
                teacher_show_question(game, name, topic, question)
            elif decision == str(3):
                main()
            elif decision == str(4):
                return
    elif decision == str(2):
        teacher_show_question(game, name, topic, question)
    elif decision == str(3):
        main()
    elif decision == str(4):
        return


def administrator_intro(game, name):
    "Method to introduce an administrator."

    password = input("Please enter Admin password: ")
    if password != game._passwords[1]:
        print("1. Enter Admin Password Again")
        print("2. Main Menu")
        print("3. Exit")
        decision = input()
        if decision == str(1):
            administrator_intro(game, name)
        elif decision == str(2):
            main()
        elif decision == str(3):
            return
        else:
            administrator_intro(game, name)
    else:
        print("Please select one of the options below")
        print("1. Game Management")
        print("2. Update Administrator Password")
        print("3. Back")
        print("4. Main Menu")
        print("5. Exit")

        decision = input()
        if decision == str(1):
            administrator_game_manage(game, name)
        elif decision == str(2):
            administrator_update_password(game, name)
        elif decision == str(3):
            administrator_intro(game, name)
        elif decision == str(4):
            main()
        elif decision == str(5):
            return
        else:
            print("Please try again")
            administrator_intro(game, name)

def administrator_game_manage(game,name):
    "Method to show the admin game management options"

    print("What would you like to manage?")

    print("1. Update Admin Password")
    print("2. Update Game Name")
    print("3. Delete Questions")
    print("4. Back")
    print("5. Main Menu")
    print("6. Exit")

    decision = input()

    if decision == str(1):
        administrator_update_password(game, name)
    if decision == str(2):
        administrator_update_game_name(game, name)
    if decision == str(3):
        administrator_delete_questions(game, name)
    elif decision == str(4):
        administrator_intro(game, name)
    elif decision == str(5):
        main()
    elif decision == str(6):
        return

def administrator_update_password(game,name):
    "Method to allow an administrator to update the admin password."

    print("Please enter the new Admin password below: ")
    old_password = game._passwords[1]
    new_password = input()
    game._passwords[1] = new_password
    print("Success, the password has been updated\n")

    print("1. Undo New Password")
    print("2. Back")
    print("3. Main Menu")
    print("4. Exit")

    decision = input()
    if decision == str(1):
        game._passwords[1] = old_password
        administrator_game_manage(game,name)
    elif decision == str(2):
        administrator_intro(game, name)
    elif decision == str(3):
        main()
    elif decision == str(4):
        return
    else:
        print("Please try again")
        administrator_update_password(game, name)

def administrator_update_game_name(game,name):
    "Method to allow an administrator to update the game name."

    print("Please enter the new Game name below: ")
    old_game_name = game._game_name

    new_game_name = input()

    game._game_name[0] = new_game_name
    print("Success, the password has been updated\n")

    print("1. Undo New Game Name")
    print("2. Back")
    print("3. Main Menu")
    print("4. Exit")

    decision = input()
    if decision == str(1):
        game._game_name = old_game_name
        administrator_game_manage(game,name)
    elif decision == str(2):
        administrator_game_manage(game,name)
    elif decision == str(3):
        main()
    elif decision == str(4):
        return
    else:
        print("Please try again")
        administrator_game_manage(game,name)

def administrator_delete_questions(game, name):
    "Method to allow an administrator to delete multiple questions."

    game.print_topics()
    print("4. Delete All Questions")
    print("5. Back")
    print("6. Main Menu")
    print("7. Exit")
    decision = input()
    if decision == str(1) or decision == str(2) or decision == str(3):
        old_topic = game._topics[int(decision)-1][1]

        game._topics[int(decision) - 1][1] = [["Empty",""],["Empty",""],["Empty",""]]

        print("1. Undo Question Deletion")
        print("2. Back")
        print("3. Main Menu")
        print("4. Exit")
        decision = input()
        if decision == str(1):
            game._topics[int(decision) - 1][1] = old_topic
            administrator_game_manage(game,name)
        elif decision == str(2):
            administrator_game_manage(game,name)
        elif decision == str(3):
            main()
        elif decision == str(4):
            return
    elif decision == str(4):
        old_questions = game._topics

        game._topics = [["Mathematics",[["Empty",""],["Empty",""],["Empty",""]]],
                        ["Egyptian History",[["Empty",""],["Empty",""],["Empty",""]]],
                        ["Egyptian Mythology",[["Empty",""],["Empty",""],["Empty",""]]]]

        print("1. Undo All Questions Deleted")
        print("2. Back")
        print("3. Main Menu")
        print("4. Exit")
        decision = input()
        if decision == str(1):
            game._topics = old_questions
            administrator_game_manage(game,name)
        elif decision == str(2):
            administrator_game_manage(game,name)
        elif decision == str(3):
            main()
        elif decision == str(4):
            return
        elif decision == str(5):
            administrator_game_manage(game,name)
        elif decision == str(6):
            main()
        elif decision == str(7):
            return

    elif decision == str(4):
        administrator_delete_all_questions(game, name)
    elif decision == str(5):
        administrator_intro(game, name)
    elif decision == str(6):
        main()
    elif decision == str(7):
        return

def main():
        print(f"{game._game_name[0]}\n")

        answer = input("Continue? Y/N\n")

        if answer == "N" or answer == "n":
            main()
        elif answer == "Y" or answer == "y":
            name = input("What is your name?\n")
            print(f"Hi {name}, what is your user type?\n")
            user_type_intro(game,name)
        else:
            main()

main()
