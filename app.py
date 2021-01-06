
from flask import Flask, render_template, request
from chatbot_model import chatbot_response
from textblob import TextBlob

check_wikipedia1 = ['what', 'is']
check_wikipedia2 = ['who', 'is']
check_wikihow = ['how', 'to']

app = Flask(__name__)
@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/get",methods=['GET','POST'])
def get_bot_response():
    user_request = request.args.get('msg')  # Fetching input from the user
    user_request = user_request.lower()
    
    print("Input: ",user_request,type(user_request))
    #print(type(user_request))
    #response = chatbot_response(user_request)
    #return response
    
    user_request = str(user_request)
    #print(type(user_request))
    blob = TextBlob(user_request)
    usr_lang = blob.detect_language()
    print(usr_lang)
    if usr_lang == "en":
        response = chatbot_response(user_request)
        return response
    elif usr_lang == "mr":
        to_english = blob.translate(to='en')
        print(to_english)
        to_english = str(to_english)
        response = chatbot_response(to_english)
        print(response)
        response = TextBlob(response)
        response = response.translate(to='mr')
        print(response)
        response = str(response)
        return response
    elif usr_lang == "hi":
        to_english = blob.translate(to='en')
        print(to_english)
        to_english = str(to_english)
        response = chatbot_response(to_english)
        print(response)
        response = TextBlob(response)
        response = response.translate(to='hi')
        print(response)
        response = str(response)
        return response
    elif usr_lang == "gu":
        to_english = blob.translate(to='en')
        print(to_english)
        to_english = str(to_english)
        response = chatbot_response(to_english)
        print(response)
        response = TextBlob(response)
        response = response.translate(to='gu')
        print(response)
        response = str(response)
        return response
    elif usr_lang == "kn":
        to_english = blob.translate(to='en')
        print(to_english)
        to_english = str(to_english)
        response = chatbot_response(to_english)
        print(response)
        response = TextBlob(response)
        response = response.translate(to='kn')
        print(response)
        response = str(response)
        return response
    elif usr_lang == "ta":
        to_english = blob.translate(to='en')
        print(to_english)
        to_english = str(to_english)
        response = chatbot_response(to_english)
        print(response)
        response = TextBlob(response)
        response = response.translate(to='ta')
        print(response)
        response = str(response)
        return response
    
    
    

if __name__ == "__main__":
    app.run(threaded=False)