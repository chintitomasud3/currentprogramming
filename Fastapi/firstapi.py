from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World haire"}

@app.get("/about/{designation}")
async def about(designation):
    return {"message":f"we are the best bank in bangladesh i am {designation}"}

@app.get("/dpost/{dpost}/{comment}")
async def dpost(dpost,comment):
    
   # return {"message":f"your postname is {dpost} "}
    return {"messages":{
         "comment":f"your post name is {dpost}",
          "custome":f"I am your boss of {comment}"
    }}

