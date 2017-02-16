import random
import sys
import webbrowser
import time


class Sentient(object):
    def __init__(self, name, program, user):
        self.name = name
        self.program = program
        self.user = user

    def converse(self, thisUser):
        print "======================================================================================"
        print ">>Friday initializing..."
        print "======================================================================================"
        time.sleep(1)
        print ">>Hello, %s! You are %s, aren't you?" % (thisUser.name, thisUser.name)
        print ">>(y/n/exit)"
        print "======================================================================================"
        input1 = str(raw_input())
        sufficientInfo = 'false'
        while sufficientInfo == 'false':
            if input1 == 'y':
                break
                sufficientInfo = 'true'
            if input1 == 'n':
                print "======================================================================================"
                print ">>My apologies. What should I call you, then?"
                print ">>(enter your name/exit)"
                print "======================================================================================"
                newUserName = str(raw_input())
                thisUser = Sentient(newUserName, 'false', 'true')
                print "======================================================================================"
                print ">>It's very nice to meet you, %s! My name is %s." % (thisUser.name, self.name)
                sufficientInfo = 'true'
                break
            if input1 == 'exit':
                print "======================================================================================"
                print ">>Goodbye!"
                print "======================================================================================"
                sys.exit()
            else:
                print "======================================================================================"
                print ">>I'm sorry. I didn't understand that, %s. You are %s, aren't you?" % (thisUser.name, thisUser.name)
                print input1
                print ">>(y/n/exit)"
                print "======================================================================================"
                input1 = str(raw_input())

    # User has been established

        if thisUser.program == 'false':
            print "======================================================================================"
            print ">>How may I help you today, %s?" % (thisUser.name)
            print ">>(examples: google, linkedin, github, youtube, exit)"
            print "======================================================================================"
            satisfied = 'false'
            while satisfied == 'false':
                input2 = str(raw_input())
                if input2 == 'google':
                    print "======================================================================================"
                    print ">>Next stop, google.com."
                    webbrowser.open_new('http://google.com')
                elif input2 == 'linkedin':
                    print "======================================================================================"
                    print ">>Next stop, linkedin.com."
                    webbrowser.open_new('http://linkedin.com')
                elif input2 == 'youtube':
                    print "======================================================================================"
                    print ">>Next stop, youtube.com."
                    webbrowser.open_new('http://youtube.com')
                elif input2 == 'github':
                    print "======================================================================================"
                    print ">>Next stop, github.com."
                    webbrowser.open_new('http://github.com')
                elif input2 == 'reddit':
                    print "======================================================================================"
                    print ">>Next stop, reddit.com."
                    webbrowser.open_new('http://reddit.com')
                elif input2 == 'gmail':
                    print "======================================================================================"
                    print ">>Next stop, gmail.com."
                    webbrowser.open_new('http://gmail.com')
                elif input2 == "let's get to work":
                    print "======================================================================================"
                    print ">>Right away, sir."
                    webbrowser.open_new('http://gmail.com')
                    webbrowser.open_new('http://google.com')
                    webbrowser.open_new('http://linkedin.com')
                    webbrowser.open_new('http://github.com')
                elif input2 == "break time":
                    print "======================================================================================"
                    print ">>Right away, sir."
                    webbrowser.open_new('http://funnyjunk.com')
                    webbrowser.open_new('http://reddit.com')
                    webbrowser.open_new('http://netflix.com')
                    webbrowser.open_new('http://youtube.com')
                elif input2 == 'exit':
                    satisfied = 'true'
                    print "======================================================================================"
                    print ">>Goodbye!"
                    print "======================================================================================"
                    sys.exit()
                else:
                    print "======================================================================================"
                    print ">>I'm sorry, I didn't understand %s." % (input2)

                print "======================================================================================"
                print ">>What else can I do for you, %s?" % (thisUser.name)
                print "======================================================================================"


Friday = Sentient('Friday', 'true', 'false')
Kevin = Sentient('Kevin', 'false', 'true')
thisUser = Kevin

Friday.converse(thisUser)
