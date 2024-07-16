from flask import Flask, render_template, jsonify
from model import NGram_Words, prepare_data

#mcdonalds_data = pd.read_csv(open("datasets/McDonald_s_Reviews.csv", errors='ignore'))["review"].to_numpy().astype(str)
mcdonalds_model = NGram_Words("mcdonalds_model", None, 3)

#airline_data = pd.read_csv(open("datasets/AirlineReviews.csv", errors='ignore'))["Review"].to_numpy().astype(str)
airline_model = NGram_Words("airline_model", None, 3)

#elon_tweet_data = pd.read_csv(open("datasets/Emusk_2021_tweets.csv", errors='ignore'))["Text"].to_numpy().astype(str)
elon_tweet_model = NGram_Words("elon_tweet_model", None, 3)

app = Flask(__name__)

@app.route('/gen_elon_tweet', methods=['GET'])
def generate_elon_tweet():
    gen = elon_tweet_model.forward()
    return jsonify({'text': gen})

@app.route('/get_mcdonalds_review', methods=['GET'])
def generate_mcdonalds_review():
    gen = mcdonalds_model.forward()
    return jsonify({'text': gen})

@app.route('/get_airline_review', methods=['GET'])
def generate_airline_review():
    gen = airline_model.forward()
    return jsonify({'text': gen})

@app.route("/")
def hello_world():
    return render_template('index.html')