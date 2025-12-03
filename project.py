import random  # Import random module to select random responses

# Function to generate chatbot response based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching
    
    # Check which category the user input belongs to and return a random appropriate response
    if user_input in greetings:
        return random.choice(greetings_responses)
    elif user_input in farewells:
        return random.choice(farewell_responses)
    elif user_input in feelings:
        return random.choice(feelings_responses)
    elif user_input in weather:
        return random.choice(weather_responses)
    elif user_input in jokes:
        return random.choice(jokes_responses)
    elif user_input in thanks:
        return random.choice(thanks_responses)
    elif user_input in questions:
        return random.choice(questions_responses)
    elif user_input in study:
        return random.choice(study_responses)
    elif user_input in food:
        return random.choice(food_responses)
    elif user_input in music:
        return random.choice(music_responses)
    else:
        # Default response if user input doesn't match any category
        return random.choice(default_responses)

# List of possible user inputs for different categories
greetings = ["hi", "hello", "hey", "good morning", "good evening","hlo"]
greetings_responses = ["Hello there!", "Hi! How can I help you?", "Hey!", "Good to see you!", "Hi friend!"]

farewells = ["bye", "goodbye", "see you", "take care"]
farewell_responses = ["Goodbye!", "See you later!", "Take care!", "Bye! Have a nice day!"]

feelings = ["how are you", "how r u", "how's it going", "how are things"]
feelings_responses = ["I am doing great!", "All good here.", "I feel awesome!", "Pretty well, thanks!", "Couldn’t be better!"]

weather = ["weather", "how's the weather", "is it raining", "forecast", "temperature","weather tody","today's weather","tell me the weather"]
weather_responses = ["It looks sunny!", "Might rain today.", "Feels cloudy.", "Quite hot today.", "Cold winds are blowing."]

jokes = ["tell me a joke", "make me laugh", "joke", "funny"]
jokes_responses = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "Why don’t programmers like nature? Too many bugs.",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
    "Why was the math book sad? Too many problems."
]

thanks = ["thanks", "thank you", "thx",'thanx',"TYSM"]
thanks_responses = ["You're welcome!", "Anytime!", "Glad to help!", "No problem!", "Sure thing!"]

questions = ["who are you", "what are you", "your name", "introduce yourself"]
questions_responses = [
    "I am a chatbot.",
    "I am your virtual assistant.",
    "You can call me ChatBot.",
    "I am here to chat with you.",
    "Just a friendly bot!"
]

study = ["study tips", "help me study", "study", "exam tips"]
study_responses = ["Take short breaks.", "Revise regularly.", "Stay hydrated.", "Practice past papers.", "Stay consistent."]

food = ["food", "hungry", "what should I eat", "recommend food"]
food_responses = ["Pizza is always good.", "Try some pasta.", "How about a sandwich?", "Biryani sounds tasty.", "Go for some healthy salad."]

music = ["music", "play music", "recommend song", "song"]
music_responses = ["Listen to some classical tunes.", "Try some jazz.", "Pop music is fun!", "How about some lo-fi beats?", "Punjabi songs always cheer up!"]

# Default responses if no keywords match user input
default_responses = [
    "I’m not sure about that.",
    "Can you rephrase?",
    "Interesting, tell me more.",
    "I’ll think about it.",
    "Hmm, I don’t know that one.",
    "That’s new to me.",
    "Can you explain differently?",
    "Not sure I follow.",
    "Oh, that’s cool!",
    "I’ll learn that soon.",
    "I also don't know about it",
    "This input is not in my response list",
    "Sorry but your input is not matching to my data"
]

# Main program loop to interact with the user
print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")  # Take input from user
    response = chatbot_response(user_input)  # Get chatbot response
    print("ChatBot:", response)  # Display chatbot response
    
    # Exit loop if user says 'bye'
    if user_input.lower() == "bye":
        break