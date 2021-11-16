
from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel
app = FastAPI()
from random import randrange
class Post(BaseModel):
    title: str 
    content: str
    published: bool = True

#POSTS CRUD 
my_posts = [{"title" : "title of post 1" , "content" : "content of post 1", "id": 1}, {"title" : "title of post 2" , "content" : "content of post 2", "id": 2}]


def find_post(id):
    for post in my_posts:
        if id == post["id"]:
            return post
        else:
            return "sorry doesnt exist"
    

#Create New Post
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"]= randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}
#Read all posts
@app.get("/posts")
def read_posts(post: Post):
    return my_posts
#Read specific post
@app.get("/posts/{id}")
def read_post(id: int):
    return find_post(id)
    
    
#Update post
@app.put("/posts/{id}")
def update_post(post: Post):
    return
@app.delete('/posts/{id}')
def delete_post(post: Post):
    return
