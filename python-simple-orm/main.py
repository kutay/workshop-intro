from orm import Database
from post import Post

db = Database('db.sqlite')
Post.db = db

# Insert data
post = Post('Hello World').save()
print(post.id)

db.commit()

objects = Post.manager(db)
print(list(objects.all()))

db.close()