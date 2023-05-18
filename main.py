from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def create_post(num):
    num = int(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    for post in all_posts:
        if post["id"] == num:
            correct_post = post
            return render_template("post.html", post=correct_post)

if __name__ == "__main__":
    app.run(debug=True)
