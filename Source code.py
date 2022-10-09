import tkinter
from tkinter import *
from tkinter.messagebox import *
#Making the window
window=Tk()
window.geometry('1300x700')
window.resizable(0,0)
window.title('Beat the Score Quiz Game')
f=open("signup.txt")
L=eval(f.read())
f.close()
#Opening the files
easy_physics=open('easy.txt')
medium_physics=open('medium.txt')
hard_physics=open('hard.txt')
easy_computer=open('easyc.txt')
medium_computer=open('medc.txt')
hard_computer=open('hardc.txt')
easy_history=open('Easyh.txt')
medium_history=open('Mediumh.txt')
hard_history=open('Hardh.txt')

def store(f):
    '''This function stores the question and the information related to it in a sublist and all those sublists are then enlcosed in a major list.'''
    f.seek(0)
    easy=f.readlines()
    easy1=[]
    j=0
    k=6
    for i in range(0,(len(easy))//6):
        easy1.append(easy[j:k])
        j+=6
        k+=6
    return easy1

#Calling store function to store the questions of file in list
easyphysics=store(easy_physics)
mediumphysics=store(medium_physics)
hardphysics=store(hard_physics)
easycomputer=store(easy_computer)
mediumcomputer=store(medium_computer)
hardcomputer=store(hard_computer)
easyhistory=store(easy_history)
hardhistory=store(hard_history)
mediumhistory=store(medium_history)
#Closing the files
easy_physics.close()
medium_physics.close()
hard_physics.close()
easy_computer.close()
medium_computer.close()
hard_computer.close()
easy_history.close()
hard_history.close()
medium_history.close()
#Opening image files
world=PhotoImage(file="world.png")
coding=PhotoImage(file='programming-coding.png')
blackhole=PhotoImage(file='physics.png')
gandhara=PhotoImage(file='history.png')

def home():
    '''This function displays the first window to the user whether he wants to login as a user or administrator.'''
    def welcome():
        global world_img
        world_img = Label(window, image=world)
        world_img.place(relheight=1.0, relwidth=1.0)
    welcome()
    i = 1  # Global variable to work as a counter for proceeding questions
    x = IntVar()  # Variable to fetch the answer index selected by the user
    score = 0  # Initial score
    op5 = IntVar()  # Right option no.

    def show_questions(level):
        '''This function starts displaying the questions to the user one by one.It is executed when user selects easy, medium or hard.'''

        def select():
            '''This function is called when user selects any option. It stores the option in 'y' variable and compares it with the op5 variable which contain
            right option'''
            nonlocal i
            nonlocal score
            nonlocal op5
            nonlocal x
            y = x.get()
            question.config(text=level[i][0])
            op1['text'] = level[i][1]
            op2['text'] = level[i][2]
            op3['text'] = level[i][3]
            op4['text'] = level[i][4]
            op5 = int(level[i - 1][5])
            if op5 == y:
                score += 1
            i += 1
            if i >=len(level):
                question.destroy()
                op1.destroy()
                op2.destroy()
                op3.destroy()
                op4.destroy()

                def backToMain():
                    nonlocal i
                    nonlocal score
                    returnBack.destroy()
                    print_score.destroy()
                    i=1
                    score=0
                    menu()
                returnBack = Button(window, text="Return to Main Menu", command=backToMain, width=20, height=2, font=("Consolas bold",12), bg="yellow" )
                returnBack.place(x=200,y=550)
                if score <= 6:
                    print_score = Label(window, text=f"Your score is {score}\nWork Hard!", width=50, height=4, font=("Consolas Bold", 16), bg="red")
                    print_score.place(x=380, y=320)
                elif 6 < score <= 8:
                    print_score = Label(window, text=f"Your score is {score}\nNice work!", width=50, height=4, font=("Consolas Bold", 16), bg="yellow")
                    print_score.place(x=380, y=320)
                elif score > 8:
                    print_score = Label(window, text=f"Your score is{score}\nExceptional!", width=50, height=4, font=("Consolas Bold", 16), bg="green")
                    print_score.place(x=380, y=320)

        # Variables under showquestions function. These variables are used to design the display of each question to the user.
        question = Label(window, text=level[0][0], font=("Consolas Bold", 12), width=130, height=2, bg="#0930DB")
        question.place(x=100, y=320)
        op1 = Radiobutton(window, text=level[0][1], variable=x, value=1, command=select, font=("Consolas Bold", 10), width=50, bg="#A7F2A5")
        op2 = Radiobutton(window, text=level[0][2], value=2, variable=x, command=select, font=("Consolas Bold", 10), width=50, bg="#A7F2A5")
        op3 = Radiobutton(window, text=level[0][3], value=3, variable=x, command=select, font=("Consolas Bold", 10), width=50, bg="#A7F2A5")
        op4 = Radiobutton(window, text=level[0][4], value=4, variable=x, command=select, font=("Consolas Bold", 10), width=50, bg="#A7F2A5")
        op1.place(x=350, y=400)
        op2.place(x=350, y=450)
        op3.place(x=350, y=500)
        op4.place(x=350, y=550)

    def menu():
        '''This function is called when user chooses to login as a player.'''
        def physics_levels():
            'This function is called when user chooses physics as a domain. It displays the three levels to user.'
            def physics_destroy():
                physics_level1.destroy()
                physics_level2.destroy()
                physics_level3.destroy()
                difficulty_level.destroy()
                back1.destroy()
            global world_img
            world_img.destroy()
            blackhole_img=Label(window,image=blackhole)
            blackhole_img.place(relheight=1,relwidth=1)
            difficulty_level = Label(window, text="Choose difficulty level", width=50, height=2,font=("Consolas Bold", 12), anchor=CENTER, bg="violet")
            difficulty_level.place(x=470,y=300)
            def easyp_questions():
                show_questions(easyphysics)
                physics_destroy()
            def mediump_questions():
                show_questions(mediumphysics)
                physics_destroy()
            def hardp_questions():
                show_questions(hardphysics)
                physics_destroy()
            #These label and buttons will be destroyed if user chooses any domain and easy medium hard options will be displayed to him.
            domains.destroy()
            physics.destroy()
            computer.destroy()
            history.destroy()
            back.destroy()
            #Level 1 means easy level 2 means medium and level 3 means hard.
            physics_level1 = Button(window, text="Easy", width=20,height=2,font=("Consolas Bold",10), anchor=CENTER,command=easyp_questions,bg="blue")
            physics_level2 = Button(window, text="Medium", width=20,height=2, font=("Consolas Bold",10),anchor=CENTER,command=mediump_questions,bg="blue")
            physics_level3 = Button(window, text="Hard", width=20,height=2, font=("Consolas Bold",10),anchor=CENTER,command=hardp_questions,bg="blue")
            physics_level1.place(x=400,y=400)
            physics_level2.place(x=600,y=400)
            physics_level3.place(x=800,y=400)
            def back1():
                '''This function will take back the user from easy medium hard options back to menu window.'''
                physics_destroy()
                blackhole_img.destroy()
                welcome()
                menu()
            back1 = Button(window, text="Back", width=20, height=2, font=("Consolas Bold",10),bg="yellow", anchor=CENTER, command=back1)
            back1.place(x=200,y=550)

        def history_levels():
            '''This function is called when user chooses history as a domain .It displays three levels to user.'''
            def history_destroy():
                history_level1.destroy()
                history_level2.destroy()
                history_level3.destroy()
                difficulty_level.destroy()
                back1.destroy()
            global world_img
            world_img.destroy()
            gandhara_img=Label(window,image=gandhara)
            gandhara_img.place(relheight=1,relwidth=1)
            difficulty_level = Label(window, text="Choose difficulty level", width=50, height=2, font=("Consolas Bold", 12), anchor=CENTER, bg="violet")
            difficulty_level.place(x=470, y=300)
            def easyh_questions():
                show_questions(easyhistory)
                history_destroy()
            def mediumh_questions():
                show_questions(mediumhistory)
                history_destroy()
            def hardh_questions():
                show_questions(hardhistory)
                history_destroy()
            # These labels and buttons will be destroyed if user chooses any domain and easy, medium, hard options will be displayed to him
            domains.destroy()
            physics.destroy()
            computer.destroy()
            history.destroy()
            back.destroy()
            # Level1 means easy, Levle2 means medium, Levle3 means hard
            history_level1 = Button(window, text="Easy", width=20,font=("Consolas Bold",10), height=2,anchor=CENTER,bg="sky blue",command=easyh_questions)
            history_level2 = Button(window, text="Medium", width=20,font=("Consolas Bold",10), height=2,anchor=CENTER,bg="sky blue",command=mediumh_questions)
            history_level3 = Button(window, text="Hard", width=20, font=("Consolas Bold",10),height=2,anchor=CENTER,bg="sky blue",command=hardh_questions)
            history_level1.place(x=400,y=400)
            history_level2.place(x=600,y=400)
            history_level3.place(x=800,y=400)
            def back1():
                '''This function return back the user from easy, medium, hard options to menu window'''
                history_destroy()
                gandhara_img.destroy()
                welcome()
                menu()
            back1 = Button(window, text="Back", width=20, height=2, bg="yellow",font=("Consolas Bold",12), anchor=CENTER, command=back1)
            back1.place(x=200, y=550)

        def computer_levels():
            '''This functio is called when user chooses computer as a domain. It displays three levels to user'''
            def computer_destroy():
                computer_level1.destroy()
                computer_level2.destroy()
                computer_level3.destroy()
                back1.destroy()
                difficulty_level.destroy()
            global world_img
            world_img.destroy()
            coding_img=Label(window,image=coding)
            coding_img.place(relheight=1,relwidth=1)
            difficulty_level = Label(window, text="Choose difficulty level", width=50, height=2,font=("Consolas Bold", 12), anchor=CENTER, bg="violet")
            difficulty_level.place(x=470, y=300)
            def easyc_questions():
                show_questions(easycomputer)
                computer_destroy()
            def mediumc_questions():
                show_questions(mediumcomputer)
                computer_destroy()
            def hardc_questions():
                show_questions(hardcomputer)
                computer_destroy()
            # These labels and buttons will be destroyed if user chooses any domain and easy, medium, hard options will be displayed to him
            domains.destroy()
            physics.destroy()
            computer.destroy()
            history.destroy()
            back.destroy()
            # Levle1 means easy, Level2 means medium, Level3 means hard
            computer_level1 = Button(window, text="Easy", width=20, height=2,font=("Consolas Bold",10),anchor=CENTER,command=easyc_questions,bg="dark blue")
            computer_level2 = Button(window, text="Medium", width=20, height=2,font=("Consolas Bold",10),anchor=CENTER,command=mediumc_questions,bg="dark blue")
            computer_level3 = Button(window, text="Hard", width=20, height=2,font=("Consolas Bold",10),anchor=CENTER,command=hardc_questions,bg="dark blue")
            computer_level1.place(x=400, y=400)
            computer_level2.place(x=600, y=400)
            computer_level3.place(x=790, y=400)
            def back1():
                computer_destroy()
                coding_img.destroy()
                welcome()
                menu()
            back1 = Button(window, text="Back", width=20, height=2, font=("Consolas Bold",10),bg="yellow", anchor=CENTER, command=back1)
            back1.place(x=200, y=550)
        # These buttons are placed to choose domain by user
        domains=Label(window,text="Choose one of the following domains",width=50,height=2,font=("Consolas Bold",12),anchor=CENTER,bg="violet")
        domains.place(x=470,y=300)
        physics=Button(window,text="PHYSICS",width=20,height=2,anchor=CENTER,command=physics_levels,font=("Consolas Bold",10),bg="blue")
        physics.place(x=600, y=400)
        computer = Button(window, text="COMPUTER", width=20, height=2,anchor=CENTER,command=computer_levels,font=("Consolas Bold",10),bg="dark blue")
        computer.place(x=400, y=400)
        history = Button(window, text="HISTORY", width=20,height=2, anchor=CENTER,command=history_levels,font=("Consolas Bold",10),bg="sky blue")
        history.place(x=800, y=400)
        main.destroy()
        def back():
            domains.destroy()
            physics.destroy()
            computer.destroy()
            history.destroy()
            back.destroy()
            home()
        back = Button(window, text="Back", width=20, height=2,  anchor=CENTER, command=back,font=("Consolas Bold",10),bg="yellow")
        back.place(x=200, y=550)
        player.destroy()
        admin.destroy()

    def administrator():
                '''This function is called when user log in as an administrator.'''
                # These buttons will be destroyed when user login as an administrator and
                player.destroy()
                admin.destroy()
                def homeBack():
                    signup.destroy()
                    signin.destroy()
                    home_back.destroy()
                    home()
                home_back=Button(window,text="Back", width=20, height=2, anchor=CENTER, command=homeBack, font=("Consolas Bold",10), bg="yellow")
                home_back.place(x=200, y=550)
                def sign_in():
                    '''This function is called when user signing in his already created account'''
                    signUser = StringVar()
                    passUser = StringVar()
                    def signsubmit_btn():
                        global L
                        nonlocal signUser
                        nonlocal passUser
                        f=open('signup.txt','rt')
                        L=eval(f.read())
                        f.close()
                        getsignUser = signUser.get()
                        getsignPassword = passUser.get()
                        signList = [getsignUser, getsignPassword]
                        if signList in L:
                            signUsername.destroy()
                            signPassword.destroy()
                            signPass_entry.destroy()
                            signUser_entry.destroy()
                            signsubmit.destroy()
                            signinback.destroy()
                            def view_edit():
                                '''This function is called when want to edit question as an administtrator '''
                                def view():
                                    global Edit
                                    global admin_back
                                    Edit.destroy()
                                    View.destroy()
                                    admin_back.destroy()
                                    def physics_levels():
                                        '''This function is called when the administratior chooses physics domain. It then displays the three levels to administrator.'''
                                        def easyp_questions():
                                            '''This function is for hte easy sub-domain of physics.'''
                                            # Calling the function to show question of easy physics
                                            view_questions(easyphysics)
                                            # Destroying the previous buttons
                                            physics_level1.destroy()
                                            physics_level2.destroy()
                                            physics_level3.destroy()
                                            back1.destroy()
                                        def mediump_questions():
                                            '''This function is for the medium sub-domain of easy physics.'''
                                            # Calling the function to show question of medium physics
                                            view_questions(mediumphysics)
                                            # Destroying the previuos buttons
                                            physics_level1.destroy()
                                            physics_level2.destroy()
                                            physics_level3.destroy()
                                            back1.destroy()
                                        def hardp_questions():
                                            '''This function is for the hard sub-domain of physics'''
                                            # Calling the function to show question of hard physics
                                            view_questions(hardphysics)
                                            # Destroying the previous buttons
                                            physics_level1.destroy()
                                            physics_level2.destroy()
                                            physics_level3.destroy()
                                            back1.destroy()
                                        # Destroying the domains
                                        domains.destroy()
                                        physics.destroy()
                                        computer.destroy()
                                        history.destroy()
                                        back.destroy()
                                        # Buttons and their placing for hard, medium and easy leels
                                        physics_level1 = Button(window, text="Easy", width=25, anchor=CENTER, font=("Consolas",15), bg="blue", command=easyp_questions)
                                        physics_level2 = Button(window, text="Medium", width=25, anchor=CENTER, font=("Consolas",15), bg="blue", command=mediump_questions)
                                        physics_level3 = Button(window, text="Hard", width=25, anchor=CENTER, font=("Consolas",15),bg="blue", command=hardp_questions)
                                        physics_level1.place(x=400, y=400)
                                        physics_level2.place(x=600, y=400)
                                        physics_level3.place(x=800, y=400)
                                        def back1():
                                            '''This is function for the back button placed for administrator's facility'''
                                            # Destroying the previous buttons for next window
                                            physics_level1.destroy()
                                            physics_level2.destroy()
                                            physics_level3.destroy()
                                            back1.destroy()
                                            # When yiu select back option, it takes you to the previus state
                                            view()
                                        # Plaicing button of Back
                                        back1 = Button(window, text="Back", width=25, anchor=CENTER, font=("Consolas",15), bg="yellow", command=back1)
                                        back1.place(x=200, y=550)
                                    def history_levels():
                                        '''This function is called when user chooses history as a domain. It displays three levels of difficulty'''
                                        def easyh_questions():
                                            view_questions(easyhistory)
                                            history_level1.destroy()
                                            history_level2.destroy()
                                            history_level3.destroy()
                                            back1.destroy()
                                        def mediumh_questions():
                                            view_questions(mediumhistory)
                                            history_level1.destroy()
                                            history_level2.destroy()
                                            history_level3.destroy()
                                            back1.destroy()
                                        def hardh_questions():
                                            view_questions(hardhistory)
                                            history_level1.destroy()
                                            history_level2.destroy()
                                            history_level3.destroy()
                                            back1.destroy()
                                        domains.destroy()
                                        physics.destroy()
                                        computer.destroy()
                                        history.destroy()
                                        back.destroy()
                                        # These buttons are placed to choose difficulty level
                                        history_level1 = Button(window, text="Easy", width=25, anchor=CENTER,font=("Consolas",15), bg="sky blue", command=easyh_questions)
                                        history_level2 = Button(window, text="Medium", width=25, anchor=CENTER, font=("Consolas",15), bg="sky blue", command=mediumh_questions)
                                        history_level3 = Button(window, text="Hard", width=25, anchor=CENTER, font=("Consolas",15), bg="sky blue", command=hardh_questions)
                                        history_level1.place(x=400, y=400)
                                        history_level2.place(x=600, y=400)
                                        history_level3.place(x=800, y=400)
                                        def back1():
                                            history_level1.destroy()
                                            history_level2.destroy()
                                            history_level3.destroy()
                                            back1.destroy()
                                            view()
                                        back1=Button(window, text="Back", width=20, height=2, anchor=CENTER, font=("Consolas bold", 15), bg="yellow", command=back1)
                                        back1.place(x=200, y=550)
                                    def computer_levels():
                                        '''This function is called whhe user choses copmuter as a domain. It displays all three difficulty level'''
                                        def easyc_questions():
                                            view_questions(easycomputer)
                                            computer_level1.destroy()
                                            computer_level2.destroy()
                                            computer_level3.destroy()
                                            back1.destroy()
                                        def mediumc_questions():
                                            view_questions(mediumcomputer)
                                            computer_level1.destroy()
                                            computer_level2.destroy()
                                            computer_level3.destroy()
                                            back1.destroy()
                                        def hardc_questions():
                                            view_questions(hardcomputer)
                                            computer_level1.destroy()
                                            computer_level2.destroy()
                                            computer_level3.destroy()
                                            back1.destroy()
                                        domains.destroy()
                                        physics.destroy()
                                        computer.destroy()
                                        history.destroy()
                                        back.destroy()
                                        computer_level1 = Button(window, text="Easy", width=25, anchor=CENTER, font=("Consolas", 15), bg="dark blue", command=easyc_questions)
                                        computer_level2 = Button(window, text="Medium", width=25, anchor=CENTER, font=("Consolas", 15), bg="dark blue", command=mediumc_questions)
                                        computer_level3 = Button(window, text="Hard", width=25, anchor=CENTER, font=("Consolas",15), bg="dark blue", command=hardc_questions)
                                        computer_level1.place(x=400, y=400)
                                        computer_level2.place(x=600, y=400)
                                        computer_level3.place(x=800, y=400)
                                        def back_1():
                                            computer_level1.destroy()
                                            computer_level2.destroy()
                                            computer_level3.destroy()
                                            back1.destroy()
                                            view()
                                        back1 = Button(window, text="Back", width=20, height=2, anchor=CENTER, font=("Consolas bold",12), bg="yellow", command=back_1)
                                        back1.place(x=200, y=550)
                                    # These labels and buttons are placed to choose domains
                                    domains = Label(window, text="Choose one of the following domains", width=50, anchor=CENTER,font=("Consolas Bold",12),bg="violet")
                                    domains.place(x=470, y=300)
                                    physics = Button(window, text="PHYSICS", width=25, anchor=CENTER, command=physics_levels,font=("Consolas Bold",10),bg="blue")
                                    physics.place(x=600, y=400)
                                    computer = Button(window, text="COMPUTER", width=25, anchor=CENTER, command=computer_levels,font=("Consolas Bold",10),bg="dark blue")
                                    computer.place(x=400, y=400)
                                    history = Button(window, text="HISTORY", width=25, anchor=CENTER, command=history_levels,font=("Consolas Bold",10),bg="sky blue")
                                    history.place(x=800, y=400)
                                    def back():
                                        domains.destroy()
                                        physics.destroy()
                                        computer.destroy()
                                        history.destroy()
                                        back.destroy()
                                        view_edit()
                                        edit_edit()
                                    back = Button(window, text="Back", width=25, anchor=CENTER,font=("Consolas Bold",10),bg="yellow", command=back)
                                    back.place(x=200, y=550)
                                def view_questions(levels):
                                    '''This function is called when user want to view question bank'''
                                    i = 1
                                    def next():
                                        '''This function takes the user to next question'''
                                        nonlocal i
                                        question.config(text=levels[i][0])
                                        op1.config(text=levels[i][1])
                                        op2.config(text=levels[i][2])
                                        op3.config(text=levels[i][3])
                                        op4.config(text=levels[i][4])
                                        i += 1
                                        def backToMain():
                                            '''This function retirn back the user to view and edit function'''
                                            nonlocal i
                                            i=1
                                            returnBack.destroy()
                                            view_edit()
                                            edit_edit()
                                        if i >=len(levels):
                                            returnBack = Button(window, text="Return to Main Menu", width=25, height=2, bg="yellow", command=backToMain)
                                            returnBack.place(x=200, y=550)
                                            next.destroy()
                                            op1.destroy()
                                            op2.destroy()
                                            op3.destroy()
                                            op4.destroy()
                                            question.destroy()
                                    next = Button(window, text="Next", width=25, height=3, bg="dark green", anchor=CENTER, command=next)
                                    next.place(x=700, y=600)
                                    question = Label(window, text=levels[0][0], bg="green")
                                    question.place(x=400, y=150)
                                    op1 = Label(window, text=levels[0][1], bg="green")
                                    op1.place(x=400, y=250)
                                    op2 = Label(window, text=levels[0][2], bg="green")
                                    op2.place(x=400, y=300)
                                    op3 = Label(window, text=levels[0][3], bg="green")
                                    op3.place(x=400, y=350)
                                    op4 = Label(window, text=levels[0][4], bg="green")
                                    op4.place(x=400, y=400)
                                global View
                                View = Button(window, text="View Questions",  width=40, height=2, font=("Consolas", 15), bg='purple', anchor=CENTER,command=view)
                                View.place(x=330,y=300)
                            def edit_edit():
                                '''This function is called when user want to add new questions in quiz game'''
                                def edit():
                                    global Edit
                                    global View
                                    global admin_back
                                    admin_back.destroy()
                                    Edit.destroy()
                                    View.destroy()
                                    admin_back.destroy()
                                    def physics_levels():
                                            '''This function is called whe user want to enter new questions in physics domain. It display the three difficulty levels'''
                                            def easyp_questions():
                                                edit_questions('easy.txt',easyphysics)
                                                physics_level1.destroy()
                                                physics_level2.destroy()
                                                physics_level3.destroy()
                                                back1.destroy()
                                            def mediump_questions():
                                                edit_questions('easy.txt',mediumphysics)
                                                physics_level1.destroy()
                                                physics_level2.destroy()
                                                physics_level3.destroy()
                                                back1.destroy()
                                            def hardp_questions():
                                                edit_questions('easy.txt',hardphysics)
                                                physics_level1.destroy()
                                                physics_level2.destroy()
                                                physics_level3.destroy()
                                                back1.destroy()
                                            # Destroying labels and buttons
                                            domains.destroy()
                                            physics.destroy()
                                            computer.destroy()
                                            history.destroy()
                                            back.destroy()
                                            # These buttons are placed to choose in which sub domain user add new question
                                            physics_level1 = Button(window, text="Easy", width=25, anchor=CENTER, bg="blue", command=easyp_questions)
                                            physics_level2 = Button(window, text="Medium", width=25, anchor=CENTER, bg="blue", command=mediump_questions)
                                            physics_level3 = Button(window, text="Hard", width=25, anchor=CENTER, bg="blue", command=hardp_questions)
                                            physics_level1.place(x=400, y=400)
                                            physics_level2.place(x=600, y=400)
                                            physics_level3.place(x=800, y=400)
                                            def back1():
                                                physics_level1.destroy()
                                                physics_level2.destroy()
                                                physics_level3.destroy()
                                                back1.destroy()
                                                edit()
                                            back1 = Button(window, text="Back", width=25, anchor=CENTER,bg="yellow", command=back1)
                                            back1.place(x=200, y=550)
                                    def computer_levels():
                                            '''This function is called when user want to add new questions in computer domain. It displays the three difficulty level'''
                                            def easyc_questions():
                                                edit_questions('easyc.txt',easycomputer)
                                                computer_level1.destroy()
                                                computer_level2.destroy()
                                                computer_level3.destroy()
                                                back1.destroy()
                                            def mediumc_questions():
                                                edit_questions('medc.txt',mediumcomputer)
                                                computer_level1.destroy()
                                                computer_level2.destroy()
                                                computer_level3.destroy()
                                                back1.destroy()
                                            def hardc_questions():
                                                edit_questions('hardc.txt',hardcomputer)
                                                computer_level1.destroy()
                                                computer_level2.destroy()
                                                computer_level3.destroy()
                                                back1.destroy()
                                            # Destroying label and domains buttons
                                            domains.destroy()
                                            physics.destroy()
                                            computer.destroy()
                                            history.destroy()
                                            back.destroy()
                                            # These buttons are placed to in which subdomain user want to add new question
                                            computer_level1 = Button(window, text="Easy", width=25, anchor=CENTER, bg="dark blue", command=easyc_questions)
                                            computer_level2 = Button(window, text="Medium", width=25, anchor=CENTER, bg="dark blue", command=mediumc_questions)
                                            computer_level3 = Button(window, text="Hard", width=25, anchor=CENTER, bg="dark blue", command=hardc_questions)
                                            computer_level1.place(x=400, y=400)
                                            computer_level2.place(x=600, y=400)
                                            computer_level3.place(x=800, y=400)
                                            def back1():
                                                computer_level1.destroy()
                                                computer_level2.destroy()
                                                computer_level3.destroy()
                                                back1.destroy()
                                                edit()
                                            back1 = Button(window, text="Back", width=25, anchor=CENTER, bg="yellow", command=back1)
                                            back1.place(x=200, y=550)
                                    def history_levels():
                                            '''This function is called when user wnt to add new questions in history domain'''
                                            def easyh_questions():
                                                edit_questions('Easyh.txt',easyhistory)
                                                history_level1.destroy()
                                                history_level2.destroy()
                                                history_level3.destroy()
                                                back1.destroy()
                                            def mediumh_questions():
                                                edit_questions('Mediumh.txt',mediumhistory)
                                                history_level1.destroy()
                                                history_level2.destroy()
                                                history_level3.destroy()
                                                back1.destroy()
                                            def hardh_questions():
                                                edit_questions('Hardh.txt',hardhistory)
                                                history_level1.destroy()
                                                history_level2.destroy()
                                                history_level3.destroy()
                                                back1.destroy()
                                            # Destroying domains and button
                                            domains.destroy()
                                            physics.destroy()
                                            computer.destroy()
                                            history.destroy()
                                            back.destroy()
                                            # These buttons are placed to sub domain in which user want to add new question
                                            history_level1 = Button(window, text="Easy", width=25, anchor=CENTER, bg="sky blue", command=easyh_questions)
                                            history_level2 = Button(window, text="Medium", width=25, anchor=CENTER,bg="sky blue", command=mediumh_questions)
                                            history_level3 = Button(window, text="Hard", width=25, anchor=CENTER,bg="sky blue", command=hardh_questions)
                                            history_level1.place(x=400, y=400)
                                            history_level2.place(x=600, y=400)
                                            history_level3.place(x=800, y=400)
                                            def back1():
                                                history_level1.destroy()
                                                history_level2.destroy()
                                                history_level3.destroy()
                                                back1.destroy()
                                                edit()
                                            back1 = Button(window, text="Back", width=20, anchor=CENTER, bg="yellow", command=back1)
                                            back1.place(x=200, y=550)
                                    domains = Label(window, text="Choose one of the following domains", width=40, height=2, font=("Consolas Bold", 12), anchor=CENTER, bg="purple")
                                    domains.place(x=470, y=300)
                                    physics = Button(window, text="PHYSICS", width=20, height=2, anchor=CENTER, command=physics_levels, font=("Consolas Bold", 10), bg="blue")
                                    physics.place(x=600, y=400)
                                    computer = Button(window, text="COMPUTER", width=20, height=2, anchor=CENTER, command=computer_levels, font=("Consolas Bold", 10), bg="dark blue")
                                    computer.place(x=400, y=400)
                                    history = Button(window, text="HISTORY", width=20, height=2, anchor=CENTER, command=history_levels, font=("Consolas Bold", 10), bg="sky blue")
                                    history.place(x=800, y=400)
                                    def back():
                                        domains.destroy()
                                        physics.destroy()
                                        computer.destroy()
                                        history.destroy()
                                        back.destroy()
                                        edit_edit()
                                        view_edit()
                                    back = Button(window, text="Back", width=25, anchor=CENTER, font=("Consolas Bold", 10), bg="yellow", command=back)
                                    back.place(x=200, y=550)

                                def edit_questions(filename, levelList):
                                    '''This function is called when administrator want to add new questions'''
                                    def choose():
                                        '''This function is called when the administrator enter on edit question'''
                                        def save_newques():
                                            '''This function is called when administrator want to save new questions and this get value from entry boxes'''
                                            new_list = []
                                            que = new_que.get()+'\n'
                                            op1 = new_op1.get()+'\n'
                                            op2 = new_op2.get()+'\n'
                                            op3 = new_op3.get()+'\n'
                                            op4 = new_op4.get()+'\n'
                                            correctop = new_correctop.get()
                                            # que_label.destroy()
                                            que_entry.delete(0, 'end')
                                            op1_entry.delete(0, 'end')
                                            op2_entry.delete(0, 'end')
                                            op3_entry.delete(0, 'end')
                                            op4_entry.delete(0, 'end')
                                            correctop_entry.delete(0, 'end')
                                            showinfo("Success", "You have successfully entered a question")
                                            # This  extend and then append new added question in list and thus it type cast it into string
                                            new_list.extend((que, op1, op2, op3, op4, str(correctop)+'\n'))
                                            levelList.insert(-1,new_list)
                                            Astring = ''
                                            for i in range(len(levelList)):
                                                for j in levelList[i]:
                                                    Astring = Astring + j
                                            with open(filename,'w+') as level_d:
                                                level_d.write(Astring)
                                        add_question.destroy()
                                        back_edit.destroy()
                                        # These labels are created to give command to an administrator to enter new questions and its option along its correct option
                                        que_label = Label(window, text="Enter new question", bg="green")
                                        que_label.place(x=300, y=100)
                                        op1_label = Label(window, text="Enter option 1", bg="green")
                                        op1_label.place(x=300, y=180)
                                        op2_label = Label(window, text="Enter option 2", bg="green")
                                        op2_label.place(x=300, y=260)
                                        op3_label = Label(window, text="Enter option 3", bg="green")
                                        op3_label.place(x=300, y=340)
                                        op4_label = Label(window, text="Enter option 4", bg="green")
                                        op4_label.place(x=300, y=420)
                                        correctop_label = Label(window, text="Enter correct option number", bg="green")
                                        correctop_label.place(x=300, y=500)
                                        # This is used to take variable data in form of string for StringVar() and integer for IntVarI()
                                        new_que = StringVar()
                                        new_op1 = StringVar()
                                        new_op2 = StringVar()
                                        new_op3 = StringVar()
                                        new_op4 = StringVar()
                                        new_correctop = IntVar()
                                        # These entry boxes are used to enter variable text which is new question and its option
                                        que_entry = Entry(window, textvariable=new_que,fg="green", width=100)
                                        que_entry.place(x=300, y=130)
                                        op1_entry = Entry(window, textvariable=new_op1,fg="green", width=100)
                                        op1_entry.place(x=300, y=210)
                                        op2_entry = Entry(window, textvariable=new_op2, fg="green", width=100)
                                        op2_entry.place(x=300, y=290)
                                        op3_entry = Entry(window, textvariable=new_op3, fg="green", width=100)
                                        op3_entry.place(x=300, y=370)
                                        op4_entry = Entry(window, textvariable=new_op4, fg="green", width=100)
                                        op4_entry.place(x=300, y=450)
                                        correctop_entry = Entry(window, textvariable=new_correctop, fg="green", width=10)
                                        correctop_entry.place(x=300, y=530)
                                        # Save button is used to execute command of save function
                                        Save_button = Button(window, text="Save",width=30, height=3, bg="dark green", command=save_newques)
                                        Save_button.place(x=900, y=600)
                                        def back():
                                            '''This back fuction will take the administrator from enter new questions to edit question. '''
                                            # Destroying buttons, labels and entry boxes of this window
                                            back_button.destroy()
                                            que_label.destroy()
                                            op1_entry.destroy()
                                            op2_entry.destroy()
                                            op3_entry.destroy()
                                            op4_entry.destroy()
                                            correctop_entry.destroy()
                                            Save_button.destroy()
                                            op1_label.destroy()
                                            op2_label.destroy()
                                            op3_label.destroy()
                                            op4_label.destroy()
                                            que_label.destroy()
                                            correctop_label.destroy()
                                            que_entry.destroy()
                                            # This will take the administrator to edit question
                                            edit_questions(filename, levelList)
                                        # Back button to execute command of back function
                                        back_button = Button(window,width=20, height=2, text="Back",bg="yellow", command=back)
                                        back_button.place(x=200, y=600)
                                        # Destroying button of Edit Questions from window
                                        Edit.destroy()
                                    def backEdit():
                                        '''Returns back to the window where choice between edit and viewing questions is offered'''
                                        add_question.destroy()
                                        back_edit.destroy()
                                        edit_edit()
                                        view_edit()
                                    back_edit = Button(window, text="Back", anchor=CENTER,width=20, bg="yellow", command=backEdit)
                                    back_edit.place(x=200, y=550)
                                    # Edit Question button to execute command of choose function
                                    add_question=Button(window,text="Edit Question",width=40,  bg="violet", command=choose)
                                    add_question.place(x=500,y=500)
                                global Edit
                                Edit = Button(window, text="Edit Questions", width=40, height=2,  font=("Consolas", 15), bg="purple", anchor=CENTER,command=edit)
                                Edit.place(x=330,y=400)
                                def adminBack():
                                    '''This function returns back the user from view and edit questions choice to sign in window'''
                                    global Edit
                                    global View
                                    global admin_back
                                    admin_back.destroy()
                                    Edit.destroy()
                                    View.destroy()
                                    sign_in()
                                global admin_back
                                admin_back=Button(window,text="Back",width=25, bg="yellow", command=adminBack)
                                admin_back.place(x=200, y=550)
                            edit_edit()
                            view_edit()
                        else:
                            warning = showinfo("Invalid Username or Password","Please enter valid username or password")

                    def signinback_btn():
                        '''This function is called when user presses back button to return from sign in window to home signup or sign in window'''
                        signUsername.destroy()
                        signUser_entry.destroy()
                        signPassword.destroy()
                        signPass_entry.destroy()
                        signsubmit.destroy()
                        signinback.destroy()
                        administrator()
                    home_back.destroy()
                    signup.destroy()
                    signin.destroy()
                    signUsername = Label(window, text="Username", width=30, height=1, font=20, bg="light green", anchor=CENTER)
                    signUsername.place(x=400, y=150)
                    signUser_entry = Entry(window, textvariable=signUser, width=40)
                    signUser_entry.place(x=400, y=200)
                    signPassword = Label(window, text="Password", width=30, height=1, font=20, bg="light green", anchor=CENTER)
                    signPassword.place(x=400, y=300)
                    signPass_entry = Entry(window, textvariable=passUser, width=40,show='*')
                    signPass_entry.place(x=400, y=350)
                    signsubmit = Button(window, text="Submit", width=10, height=2, font=("Consolas", 20), bg="green", anchor=CENTER, command=signsubmit_btn)
                    signsubmit.place(x=700, y=500)
                    signinback = Button(window, text="Back", width=10, height=1, font=("Consolas", 20), bg="yellow", anchor=CENTER, command=signinback_btn)
                    signinback.place(x=300, y=500)

                def sign_up():
                    '''This function is called when user opts to sign up'''
                    def submit_btn():
                        '''This function takes all the values of user who wants to signup'''
                        global L
                        nonlocal uservar
                        nonlocal passvar
                        getUser = uservar.get()
                        getPassword = passvar.get()
                        signupList = [getUser, getPassword]
                        L.append(signupList)
                        with open('signup.txt','wt') as f:
                            f.write(str(L))
                        administrator()
                        Username.destroy()
                        Password.destroy()
                        submit.destroy()
                        User_entry.destroy()
                        Pass_entry.destroy()
                        signupback.destroy()
                    def signupback_btn():
                        '''This function is called when user returns from sign up window where the choice between signup and signin is offered'''
                        Username.destroy()
                        User_entry.destroy()
                        Password.destroy()
                        Pass_entry.destroy()
                        submit.destroy()
                        signupback.destroy()
                        administrator()
                    home_back.destroy()
                    signup.destroy()
                    signin.destroy()
                    uservar = StringVar()
                    passvar = StringVar()
                    Username = Label(window, text="Username", width=30, height=1, font=20, bg="light green", anchor=CENTER)
                    Username.place(x=400, y=150)
                    User_entry = Entry(window, textvariable=uservar, width=40)
                    User_entry.place(x=400, y=200)
                    Password = Label(window, text="Password", width=30, height=1, font=20, bg="light green", anchor=CENTER)
                    Password.place(x=400, y=300)
                    Pass_entry = Entry(window, textvariable=passvar, width=40,show='*')
                    Pass_entry.place(x=400, y=350)
                    submit = Button(window, text="Submit", width=6,height=1,font=("Consolas", 15), bg="green", anchor=CENTER, command=submit_btn)
                    submit.place(x=700, y=500)
                    signupback = Button(window, text="Back", width=10, height=1, font=("Consolas", 20), bg="yellow", anchor=CENTER, command=signupback_btn)
                    signupback.place(x=300, y=500)
                signup = Button(window, text="Sign Up", command=sign_up, width=50, height=2, font=("Consolas", 15), bg='green', anchor=CENTER)
                signin = Button(window, text="Sign in", command=sign_in, width=50, height=2, font=("Consolas", 15), bg='green', anchor=CENTER)
                signup.place(x=400, y=300)
                signin.place(x=400, y=400)
                main.destroy()
    # These labels and buttons are place to choose as mode of game, whether  as a player or as an administrator
    main=Label(window, text="Welcome to\nBeat The Score\nQUIZ GAME", width=30, height=4, font=("Consolas bold",40), bg="black", fg="#FFFFFF")
    main.place(x=175, y=100)
    player=Button(window,text="Login as player",width=30,height=2,font=("Consolas bold",20),bg="light blue",anchor=CENTER,command=menu)
    player.place(x=350, y=400)
    admin=Button(window,text="Login as administrator",width=30,height=2,font=("Consolas bold",20),bg="light blue",anchor=CENTER,command=administrator)
    admin.place(x=350,y=500)
home()
window.mainloop()
