import json
import urllib.request

from beans.Post import Post
from beans.User import User


class Blog:

    def __init__(self, url_users, url_posts) -> None:
        self.users = []
        self.posts = []
        self.url_users = url_users
        self.url_posts = url_posts

    def load(self):
        self.load_users(self.url_users)
        self.load_posts(self.url_posts)
        for user in self.users:
            user.link_posts(self.posts)

    def user_post_counts(self):
        post_count_strings = []
        for user in self.users:
            post_count_strings.append(
                user.username + " wrote " + str(len(user.posts)) + " posts.")

        return post_count_strings

    def load_users(self, link):
        with urllib.request.urlopen(link) as url:
            users_data = json.loads(url.read().decode('utf8'))
            for user in users_data:
                self.users.append(
                    User(user["id"],
                         user["username"],
                         user["address"]["geo"]["lat"],
                         user["address"]["geo"]["lng"]))

    def load_posts(self, link):
        with urllib.request.urlopen(link) as url:
            posts_data = json.loads(url.read().decode('utf8'))
            for post in posts_data:
                self.posts.append(
                    Post(post["id"],
                         post["userId"],
                         post["title"]))

    def get_post_titles(self, unique):
        titles = []
        for post in self.posts:
            if post.is_unique_title(self.posts) is unique:
                if post.title not in titles:
                    titles.append(post.title)

        return titles
