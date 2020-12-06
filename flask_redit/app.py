import praw
from flask import Flask,render_template, request, flash

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        subr=request.form.get("subr").lower()
        keywrd=request.form.get("keywords").lower()

        #making sure the text is going to be interpretable by the program
        subr=subr.replace("r/","")
        subr=subr.split(" + ")
        keywrd=keywrd.split(" + ")
        
        #flash("result obtained :")
        #reddit_bot(subr,keywrd)
        return render_template("index.html", msg='Understood ! You will get notified every time '+keywrd+' get posted on '+subr+'.')

    return render_template("index.html")



def bot_login():
    reddit = praw.Reddit(
        username='EliouzBot',
        password='crD6t12sANeK',
        client_id='2s5whtB65tV4Lw',
        client_secret='1MtZr_8Xbc6IvQikT5HpNsd78c8',
        user_agent="Reddit Notify",
    )
    return reddit

def reddit_bot(subreddits,keywords):
    reddit = bot_login()
    sub='+'.join(subreddits)
    subreddit = reddit.subreddit(sub)
    print(sub)
    print(keywords)
    for submission in subreddit.stream.submissions():
        process_submission(submission,keywords)


def process_submission(submission,keywords):
    normalized_title = submission.title.lower()
    for k in keywords:
        if k in normalized_title:
            #if keyword in title of the submission of the set subreddit
            #flash("result obtained :")
            print("result obtained !")
            print(submission.url)
            break

if __name__ == "__main__":
    app.run()
