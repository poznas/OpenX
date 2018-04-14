from Blog import Blog

URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_TEST_POSTS = "https://firebasestorage.googleapis.com" \
            "/v0/b/marynarka-fcdf8.appspot.com/o/non_unique_test.json" \
            "?alt=media&token=34fdbcd5-d1a4-44e8-b7a1-1c03d32a23a1"

blog = Blog(URL_USERS, URL_TEST_POSTS)
blog.load()
for post_count in blog.user_post_counts():
    print(post_count)
print("\nnon-unique post titles: " + str(blog.get_post_titles(False)) + "\n")
