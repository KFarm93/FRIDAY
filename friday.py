import random
import sys
import webbrowser
import time
import os


class Sentient(object):
    def __init__(self, name, program, user):
        self.name = name
        self.program = program
        self.user = user

    def converse(self, thisUser):
        print "======================================================================================"
        print ">>Friday initializing..."
        # print "======================================================================================"
        time.sleep(1)
        # print ">>Hello, %s! You are %s, aren't you?" % (thisUser.name, thisUser.name)
        # print ">>(y/n/exit)"
        # print "======================================================================================"
        # input1 = str(raw_input())
        # sufficientInfo = 'false'
        # while sufficientInfo == 'false':
        #     if input1 == 'y':
        #         break
        #         sufficientInfo = 'true'
        #     if input1 == 'n':
        #         print "======================================================================================"
        #         print ">>My apologies. What should I call you, then?"
        #         print ">>(enter your name/exit)"
        #         print "======================================================================================"
        #         newUserName = str(raw_input())
        #         thisUser = Sentient(newUserName, 'false', 'true')
        #         print "======================================================================================"
        #         print ">>It's very nice to meet you, %s! My name is %s." % (thisUser.name, self.name)
        #         sufficientInfo = 'true'
        #         break
        #     if input1 == 'exit':
        #         print "======================================================================================"
        #         print ">>Goodbye!"
        #         print "======================================================================================"
        #         sys.exit()
        #     else:
        #         print "======================================================================================"
        #         print ">>I'm sorry. I didn't understand that, %s. You are %s, aren't you?" % (thisUser.name, thisUser.name)
        #         print ">>(y/n/exit)"
        #         print "======================================================================================"
        #         input1 = str(raw_input())

    # User has been established

        # if thisUser.program == 'false':
        print "======================================================================================"
        print ">>How may I help you today, %s?" % (thisUser.name)
        # print ">>(examples: google, linkedin, github, youtube, exit)"
        print "======================================================================================"
        satisfied = 'false'
        while satisfied == 'false':
            input2 = str(raw_input())


    # standard websites
            if input2 == 'google':
                print "======================================================================================"
                print ">>Opening google.com."
                webbrowser.open_new('http://google.com')
            elif input2 == 'linkedin':
                print "======================================================================================"
                print ">>Opening linkedin.com."
                webbrowser.open_new('http://linkedin.com')
            elif input2 == 'youtube':
                print "======================================================================================"
                print ">>Opening youtube.com."
                webbrowser.open_new('http://youtube.com')
            elif input2 == 'github':
                print "======================================================================================"
                print ">>Opening github.com."
                webbrowser.open_new('http://github.com')
            elif input2 == 'reddit':
                print "======================================================================================"
                print ">>Opening reddit.com."
                webbrowser.open_new('http://reddit.com')
            elif input2 == 'gmail':
                print "======================================================================================"
                print ">>Opening gmail.com."
                webbrowser.open_new('http://gmail.com')
            elif input2 == 'aws':
                print "======================================================================================"
                print ">>Opening aws.amazon.com."
                webbrowser.open_new('https://aws.amazon.com/')
            elif input2 == 'netflix':
                print "======================================================================================"
                print ">>Opening netflix.com."
                webbrowser.open_new('https://netflix.com/')
            elif input2 == 'fj':
                print "======================================================================================"
                print ">>Opening funnyjunk.com."
                webbrowser.open_new('https://funnyjunk.com')
            elif input2 == 'portfolio':
                print "======================================================================================"
                print ">>Opening kevinfarmer.site."
                webbrowser.open_new('http://kevinfarmer.site')


    # grouped websites
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


    # applications
            elif input2 == 'notes':
                print "======================================================================================"
                print ">>Opening Notes."
                os.system("open /Applications/Notes.app")
            elif input2 == 'steam':
                print "======================================================================================"
                print ">>Opening Steam."
                os.system("open /Applications/Steam.app")
            elif input2 == 'pages':
                print "======================================================================================"
                print ">>Opening Pages."
                os.system("open /Applications/Pages.app")
            elif input2 == 'curse':
                print "======================================================================================"
                print ">>Opening Curse."
                os.system("open /Applications/Curse.app")
            elif input2 == 'postgres':
                print "======================================================================================"
                print ">>Opening Postgres."
                os.system("open /Applications/Postgres.app")
            elif input2 == 'exit':
                satisfied = 'true'
                print "======================================================================================"
                print ">>Friday shutting down."
                print "======================================================================================"
                sys.exit()
            else:
                print "======================================================================================"
                print ">>I'm sorry, I didn't understand '%s'." % (input2)


    # Anything else?
            print "======================================================================================"
            print ">>What else can I do for you, %s?" % (thisUser.name)
            print "======================================================================================"


Friday = Sentient('Friday', 'true', 'false')
Kevin = Sentient('Kevin', 'false', 'true')
thisUser = Kevin

Friday.converse(thisUser)
