import math


class User:

    def __init__(self, user_id, username, lat, lng) -> None:
        self.id = user_id
        self.username = username
        self.lat = float(lat)
        self.lng = float(lng)
        self.posts = []
        self.neighbour = None

    def link_posts(self, posts):
        for post in posts:
            if post.user_id is self.id:
                self.posts.append(post)

    def get_neighbour(self, users):
        if self.neighbour is None:
            lowest_distance = math.inf
            for user in users:
                if user is self:
                    continue
                distance = math.sqrt(
                    pow(self.lat - user.lat, 2)
                    + pow(self.lng - user.lng, 2))

                if distance < lowest_distance:
                    lowest_distance = distance
                    self.neighbour = user

        return self.neighbour


