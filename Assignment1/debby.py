from flask import Flask, jsonify;

#initiating the Flask instance with only one argument
app = Flask(__name__)

#default route
@app.route("/",methods = ['GET'])
def articles():
    return "<p>Return all my articles</p>"

@app.route("/articles",methods = ['GET'])
def get_articles():
    books = [
        {
            "Id":1001,
            "title":"The Big Three",
            "body":"The adventures of Samak, a trickster-warrior hero of Persia's thousand-year-old oral storytelling tradition, are beloved in Iran",
            "author":"Tom Dickens"
        },
        {
           "Id":1002,
            "title":"Heidi",
            "body":"a fictional version of the real-life “no-no boys.” Yamada answered “no” twice in a compulsory government questionnaire as to whether he would serve in the armed forces and swear loyalty",
            "author":"Hayley Beiber" 
        },
        {
            "Id":1003,
            "title":"Birds Of Prey",
            "body":"They plot the most up-to-date distribution information for each species and include the location of cities for more accurate reference. Finally, the guides feature color habitat photographs next to the maps",
            "author":"Harley Queen"
        }
    ]

    return jsonify({
        "books":books
    })


if __name__ == "__name__":
    app.run(debug= True)



