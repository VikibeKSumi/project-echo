from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get('/analyse')
def sentiment_analyzer (text: str):
  if "happy" in text.lower():
    return "Positive"
  else:
    return "Negative"


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  uvicorn.run (app, host="0.0.0.0", port=port)
