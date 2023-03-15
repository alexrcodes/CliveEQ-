# This code is a voice-activated emotional support assistant that uses the OpenAI API to generate intelligent responses, all in under 100 lines of code.
# It can perform various tasks such as  1. Identifying and assessing emotions in yourself and others; 2. Regulating your own emotions; 
# and 3. Utilizing emotional information to guide decisions and thinking.
# It uses the speech_recognition and pyttsx3 libraries to recognize user voice input and provide audio responses.

# I created him because I believe it's important to take care of ourselves and make sure we prioritize our mental health especially as students, 
# because times will get hard and you need to know what your triggers and relievers are. Maybe you're the type of person that likes to take a nap or listen to music to relax like me. 
# Whatever it is EQ can help you get through it.


# Import required libraries
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import webbrowser
import requests

# Set OpenAI API key 
# MAKE SURE YOU LOG INTO OPENAI AND USE YOUR OWN API KEY 
# YOU CAN FIND YOUR API KEY UNDER 'User settings'
# (this code will not work if you dont have your own api key)
openai.api_key = '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'


# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition object and microphone
r = sr.Recognizer()
mic = sr.Microphone()

# Set conversation and bot name
conversation = ""
user_name = "Sir"
bot_name = "EQ" "Emotional Intelligence"

# Set text-to-speech engine rate
engine.setProperty('rate', 140)

# Define talk function to speak responses
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Define welcome function to greet user and tell current time
def welcome(): 
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime('%I:%M %p')
    # Greet user based on current time
    if hour>=0 and hour<=12:
        talk("good morning sir, it is" +time)
    elif hour>12 and hour<18:
        talk("good afternoon sir, it is" +time)
    else:
        talk("good evening sir, it is" +time)
    # Introduce bot
    talk("E Q here ready to help you")

# Call welcome function
welcome()

# Continuously listen for user input and generate responses
while True:
    with mic as source:
        print('\nlistening')
        #r.adjust_for_ambient_noise(source, duration=0.15)
        audio = r.listen(source)
    print("no longer listening...\n")

    try:
        # Use Google's speech recognition API to convert user speech to text
        user_input = r.recognize_google(audio)
        print("user input :" + user_input)
    except Exception as e:
        print(e)
        continue


    # Append user input to conversation history
    prompt = user_name + ": " + user_input + "\n" + bot_name+":"
    conversation += prompt

    # Use OpenAI API to generate a response
    response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=1000)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("EQ: " + ": ", 1)[0]
    
    # Append bot response to conversation history
    conversation += response_str + "\n"
    print(response_str)
    
    # Speak bot response
    engine.say(response_str)
    engine.runAndWait()


# Some questions you can ask to get the conversation going

# First: Who are you and what can you do?
# Second: Why do you think mental health and emotional well-being is important?
# Third: How can I use you to accomplish my goal of improving my mental health?

# Scenario 1 
# Prompt: How are you feeling today?
# Me: hello EQ
# Me: Im feeling anxious
# EQ: response...
# Me: I have exams coming up soon, maybe if you walk me through some deep breathing exercises it may help
# EQ: response... 
# Me: Thank you, I feel a lot better
# EQ: response...

# Scenario 2
# Prompt: A really good day
# Me: Its been a really good day
# EQ: response...
# Me: I had a lot of fun today 
# EQ: response...
# Me: I hung out with friends, ate some great food, and joked around all day
# EQ: response...
# Me: Yeah, we went to the zoo
# EQ: response
# Me: Why are friends an important part of mental health? 
# EQ: response... 
# Me: I agree. thank you for listening!