class Post:

    def __init__(self, post_id, user_id, title) -> None:
        self.id = post_id
        self.user_id = user_id
        self.title = title

    def is_unique_title(self, posts) -> bool:
        for post in posts:
            if post.title == self.title and post.id != self.id:
                return False
        return True

