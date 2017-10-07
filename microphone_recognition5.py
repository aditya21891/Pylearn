from pygame import mixer;from subprocess import call;import time
import pywapi; import speech_recognition as sr
mixer.init() #you must initialize the mixer
x=0;y=0;extra=""
recognised=""
recengine="google"
mode=0
r = sr.Recognizer()

call(["espeak","Adjusting for background noise"])
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

while True:
    call(["espeak","Please say something and I will try to understand."])    
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            recognised=r.recognize_google(audio)
            print recognised
        except:
            recognised=r.recognize_sphinx(audio)
            print "sphinx:"+recognised
                  
    if mode==1:
        if "stop" in recognised:
            if "dictation" or "dictating" in recognised:
                mode=0
                call(["espeak","stopping dictation"])
            else:
                print recognised

    if mode==0:
        try:
            if computername in recognised:
                call(["espeak","yes I believe "+computername+" is my name."])
        except:
            print ""

        if "time" in recognised:
            if "what" in recognised or "tell" in recognised:
                timenow = time.localtime()
                timeh= timenow.tm_hour;timem = timenow.tm_min
                if timeh<13: ampm="A.M"
                else: ampm="P.M"
                if timem>9: extra=" "
                else: extra="oh"
                call(["espeak","the time is"+str(timeh)+extra+str(timem)+ampm])


        if "your name" in recognised:
                try:
                    computername
                    call(["espeak","my name is "+computername])
                    print "my name is "+ computername
                    if "change" in recognised:
                        call(["espeak","I can change my name now"])
                        print "I can change my name now"    
                        raise ValueError('make program change name')
                except:
                    call(["espeak","what name would you like to call me"])
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        try:
                            computername=r.recognize_google(audio)
                            print computername
                        except:
                            computername=r.recognize_sphinx(audio)
                            print "sphinx:"+computername
                    call(["espeak","OK, my name is "+computername+" what else can I do for you"])

        elif "use" in recognised or "change" in recognised:
            if "google" in recognised: recengine="google"
            if "sphinx" or "Sphinx" in recognised: recengine="sphinx"

        elif "exit" in recognised or "close" in recognised:
            call(["espeak","OK. I am ending the program"])

        elif "alarm" in recognised:
            if "set" in recognised or "make" in recognised:
                if "minutes" in recognised:
                    numbers = [int(s) for s in recognised.split() if s.isdigit()]
                    if numbers:
                        call(["espeak","OK I can set an alarm in "+str(numbers[-1])+"minutes"])
                if ":" in recognised:
                    location=recognised.find(":")
                    if "p.m" in recognised or "evening" in recognised or "evening" in recognised:
                        call(["espeak","OK I can set an alarm at "+recognised[location-2:location+3]+"in the evening"])
                    else:
                        call(["espeak","OK I can set an alarm at "+recognised[location-2:location+3]+"in the morning"])

        elif "hello" in recognised or "good morning" in recognised or "hi" in recognised:
            call(["espeak","greetings to you too. I'm ready tou do your bidding."])

        elif "open" in recognised:
            if "browser" in recognised or "internet" in recognised or "firefox" in recognisedd:
                call(["espeak","OK I'll open a browser"])
                call(["firefox","www.google.com"])                

        elif "weather" in recognised:
            loc="Bolton"
            lookup = pywapi.get_location_ids(loc)
            for i in lookup:
                location_id = i
            weather=pywapi.get_weather_from_weather_com(location_id)
            call (["espeak", "the weather in "+loc+" is "+weather['current_conditions']['text']+". Current temp "+weather['current_conditions']['temperature']+" degrees centigrade"])


        elif "thank" in recognised:
            call(["espeak","You're welcome."])

        elif "dictation" in recognised:
            if "start" in recognised or "mode" in recognised:
                mode=1
                call(["espeak","entering dictation mode"])
                
        elif "what" in recognised:
            if "do" in recognised or "say" in recognised:
                call(["espeak", "I can do dictation, tell the time, set alarms, say hello and goodbye and open a browser, respond to thankyous and tell you what i can understand"])

        else:
            call(["espeak", "I didnt understand" + recognised + ". But what else can I do for you"])
        
