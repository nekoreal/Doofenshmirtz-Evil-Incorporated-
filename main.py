from fastapi import FastAPI
import uvicorn

 

app = FastAPI(title="Doofenshmirtz Evil Inc API")

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    #uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000) 
    #пока в разработке запуск fastapi dev main.py ,
    #потом же можно расскоментировать uvicorn.run и запускать через py main.py, так в докере понятнее будет
    pass