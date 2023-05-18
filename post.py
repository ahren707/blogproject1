
import requests

class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.blog_url)
        self.all_posts = self.response.json()

    def get_post(self, num):
        num = int(num)
        for post in self.all_posts:
            if post["id"] == num:
                correct_post = post
                return correct_post
            else:
                pass
