from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/question1")
def one():
    return render_template("question.html", number = 1, next = 2, question = "Do you like bananas?", 
    a = "Yes", b = "Yes", c = "Yes", d = "Yes")

@app.route("/question2")
def two():
    return render_template("question.html", number = 2, next = 3, question = "Which of these sports is your favorite?", 
    a = "Gorilla Wrestling", b = "Vine Swinging", c = "Baseball, but with feces instead of an actual baseball", d = "Competitive Banana Eating")

@app.route("/question3")
def three():
    return render_template("question.html", number = 3, next = 4, question = "Which activity would be perfect for a date?", 
    a = "Dinner and a Movie", b = "Making Monkey Noises for 24 Hours Straight", c = "Commiting Various Atrocities", d = "Persuading Humans to De-Evolve Back to Primates")

@app.route("/question4")
def four():
    return render_template("question.html", number = 4, next = 5, question = "What is your favorite drink?", 
    a = "Water (no salt)", b = "Water (with added salt)", c = "Glue", d = "Banana")

@app.route("/question5")
def five():
    return render_template("question.html", number = 5, next = 6, question = "Which of these fictional monkeys do you relate to the most?", 
    a = "Curious George", b = "Monkey (Kung Fu Panda)", c = "King Kong", d = "Goku")

@app.route("/question6")
def six():
    return render_template("question.html", number = 6, next = 7, question = "How do you respond to the phrase 'I love you'?", 
    a = "*various monkey noises*", b = '"Yes"', c = '"Ok, but why?"', d = '"If only someone loved you"')

@app.route("/question7")
def seven():
    return render_template("question.html", number = 7, next = 8, question = "Do you believe in God?", 
    a = "Yes (you are highly religious)", b = "Yes (you believe you are God)", c = "Why are you asking me this question?", d = "No")

@app.route("/question8")
def eight():
    return render_template("question.html", number = 8, next = 9, question = "A man with a gun approaches you. What do you do?", 
    a = "Have an intellectual debate with him in order to get him to not shoot you", b = "Punch him in the face before he gets the chance to shoot you", c = "Let him shoot you to find out if you're immortal or not", d = "Die.")

@app.route("/question9")
def nine():
    return render_template("question.html", number = 9, next = 10, question = "Which Donkey Kong character is the most attractive?", 
    a = "Donkey Kong", b = "Diddy Kong", c = "Funky Kong", d = "Chunky Kong")

@app.route("/question10")
def ten():
    return render_template("question.html", number = 10, next = 11, question = "What do you think is the most dire problem in monkey society?", 
    a = "Limited Water Supply", b = "The Lack of a System of Government", c = "Banana Theft", d = "The Impending Doom of the Earth's Eventual Destruction in the Distant Future")

@app.route("/question11")
def eleven():
    return render_template("question.html", number = 11, next = 12, question = "What aspect do you value most in a partner?", 
    a = "Murderous Intent", b = "Cute and Cuddly", c = "Sick Skateboarding Skills", d = "Having a PhD in Theoretical Physics")

@app.route("/question12")
def twelve():
    return render_template("question.html", number = 12, next = "last", question = "OOH OOH AAH AAH", 
    a = "OOHOOH OOH OOH", b = "AAAHA AAAHAAAH", c = "OOGA BOOGA UNGA BUNGA", d = "YABBADABBADOO")

@app.route("/questionlast")
def end():
    return render_template("end.html")

@app.route("/zachary")
def zachary():
    return render_template("zachary.html")

@app.route("/kathleen")
def kathleen():
    return render_template("kathleen.html")

@app.route("/dylan")
def dylan():
    return render_template("dylan.html")

@app.route("/daniel")
def daniel():
    return render_template("daniel.html")

if __name__ == "__main__":
    app.run(debug = True)