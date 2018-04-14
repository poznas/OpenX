from Blog import Blog

URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"


blog = Blog(URL_USERS, URL_POSTS)
blog.load()
for post_count in blog.user_post_counts():
    print(post_count)
print("\nnon-unique post titles: " + str(blog.get_post_titles(False)) + "\n")
for user in blog.users:
    neighbour = user.get_neighbour(blog.users)
    print(user.username + " neighbour:\t" + neighbour.username)
