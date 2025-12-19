from app import sentiment_analyzer 

def test_sentiment():
  assert sentiment_analyzer("i am happy") == "Positive"
  assert sentiment_analyzer ("This is sad") == "Negative"
