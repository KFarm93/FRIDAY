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
        print ">>FRIDAY initializing..."
        os.system('say -v Vicki FRIDAY initializing')
        # print "======================================================================================"
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
        os.system('say -v Vicki How may I help you today, Kevin?')
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
                os.system('say -v Vicki Opening google.com')
            elif input2 == 'linkedin':
                print "======================================================================================"
                print ">>Opening linkedin.com."
                webbrowser.open_new('http://linkedin.com')
                os.system('say -v Vicki Opening linkedin.com')
            elif input2 == 'youtube':
                print "======================================================================================"
                print ">>Opening youtube.com."
                webbrowser.open_new('http://youtube.com')
                os.system('say -v Vicki Opening youtube.com')
            elif input2 == 'github':
                print "======================================================================================"
                print ">>Opening github.com."
                webbrowser.open_new('http://github.com')
                os.system('say -v Vicki Opening github.com')
            elif input2 == 'reddit':
                print "======================================================================================"
                print ">>Opening reddit.com."
                webbrowser.open_new('http://reddit.com')
                os.system('say -v Vicki Opening red it .com')
            elif input2 == 'gmail':
                print "======================================================================================"
                print ">>Opening gmail.com."
                webbrowser.open_new('http://gmail.com')
                os.system('say -v Vicki Opening g mail.com')
            elif input2 == 'aws':
                print "======================================================================================"
                print ">>Opening aws.amazon.com."
                webbrowser.open_new('https://aws.amazon.com/')
                os.system('say -v Vicki Opening a w s.amazon.com')
            elif input2 == 'slack':
                print "======================================================================================"
                print ">>Opening slack.com."
                webbrowser.open_new('https://slack.com')
                os.system('say -v Vicki Opening slack.com')
            elif input2 == 'netflix':
                print "======================================================================================"
                print ">>Opening netflix.com."
                webbrowser.open_new('https://netflix.com/')
                os.system('say -v Vicki Opening net flicks.com')
            elif input2 == 'fj':
                print "======================================================================================"
                print ">>Opening funnyjunk.com."
                webbrowser.open_new('https://funnyjunk.com')
                os.system('say -v Vicki Opening funny junk.com')
            elif input2 == 'portfolio':
                print "======================================================================================"
                print ">>Opening kevinfarmer.site."
                webbrowser.open_new('http://kevinfarmer.site')
                os.system('say -v Vicki Opening kevinfarmer.site')
            elif input2 == 'local':
                print "======================================================================================"
                print ">>Opening local server."
                webbrowser.open_new('http://localhost:8000')
                os.system('say -v Vicki Opening local server')


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
            elif input2 == 'atom':
                print "======================================================================================"
                print ">>Opening Atom."
                os.system("open /Applications/Atom.app")

            # exit
            elif input2 == 'exit':
                satisfied = 'true'
                print "======================================================================================"
                print ">>FRIDAY shutting down."
                print "======================================================================================"
                os.system('say -v Vicki FRIDAY shutting down.')
                sys.exit()


    # other
            elif input2 == 'what time is it?':
                now = time.asctime(time.localtime())

                # find which day of the week it is
                day_of_week = now[0:3]
                if day_of_week == "Sun":
                    day_of_week = "Sunday"
                elif day_of_week == "Mon":
                    day_of_week = "Monday"
                elif day_of_week == "Tue":
                    day_of_week = "Tuesday"
                elif day_of_week == "Wed":
                    day_of_week = "Wednesday"
                elif day_of_week == "Thu":
                    day_of_week = "Thursday"
                elif day_of_week == "Fri":
                    day_of_week = "Friday"
                elif day_of_week == "Sat":
                    day_of_week = "Saturday"


                # find out which month it is
                month = now[4:7]
                if month == "Jan":
                    month = "January"
                elif month == "Feb":
                    month = "February"
                elif month == "Mar":
                    month = "March"
                elif month == "Apr":
                    month = "April"
                # May does not need correcting
                elif month == "Jun":
                    month = "June"
                elif month == "Jul":
                    month = "July"
                elif month == "Aug":
                    month = "August"
                elif month == "Sep":
                    month = "September"
                elif month == "Oct":
                    month = "October"
                elif month == "Nov":
                    month = "November"
                elif month == "Dec":
                    month = "December"


                # find out what day of the month it is
                day_of_month = now[8:10]
                if day_of_month[1:2] == "1":
                    day_of_month += "st"
                elif day_of_month[1:2] == "2":
                    day_of_month += "nd"
                elif day_of_month[1:2] == "3":
                    day_of_month += "rd"
                else:
                    day_of_month += "th"

                # find out the time of day
                hour = int(now[11:13])
                if hour >= 12:
                    AM_PM = "PM"
                    if hour >= 13:
                        hour -= 12
                    else:
                        pass
                else:
                    AM_PM = "AM"

                # find out the minute
                minute = now[14:16]

                # find out the year
                year = int(now[20:24])

                # print
                print "======================================================================================"
                print ">>It is %i:%s %s on %s, %s %s, %i." % (hour, minute, AM_PM, day_of_week, month, day_of_month, year)
                os.system('say -v Kathy It is %(month)s %(day_of_month)s' % locals())




            else:
                print "======================================================================================"
                print ">>I'm sorry, I didn't understand '%s'." % (input2)
                os.system('say -v Vicki Eyem sorry, I dident understand %(input2)s' % locals())


    # Anything else?
            print "======================================================================================"
            print ">>What else can I do for you, %s?" % (thisUser.name)
            os.system('say -v Vicki What else can I do for you, Kevin?')
            print "======================================================================================"


FRIDAY = Sentient('FRIDAY', 'true', 'false')
Kevin = Sentient('Kevin', 'false', 'true')
thisUser = Kevin

FRIDAY.converse(thisUser)
