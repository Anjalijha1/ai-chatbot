from fastapi import FastAPI
app=FastAPI()
@app.get():
return {"message": "backend working"}
