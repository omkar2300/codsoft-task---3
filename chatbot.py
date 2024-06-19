def greet(user_message):
  greetings = ["hi", "hello", "hey"]
  if any(greeting in user_message.lower() for greeting in greetings):
    return f"Hi! How can I help you today?"
  else:
    return "Sorry, I didn't understand that."

def answer_question(user_message):
  questions = {
    "what is your name": "My name is Bard, a simple chatbot.",
    "can you recommend a movie": "Sure! Do you have a preferred genre?"
  }
  for question, answer in questions.items():
    if question in user_message.lower():
      return answer
  return "I can't answer that yet, but I'm still learning!"

def recommend_movie(user_message):
  genres = {
    "comedy": ["The Big Lebowski", "21 Jump Street"],
    "action": ["Mad Max: Fury Road", "Inception"]
  }
  genre = user_message.lower().split()[-1]
  if genre in genres:
    return f"Here are some {genre} movies I recommend: {', '.join(genres[genre])}"
  else:
    return "Sorry, I don't have anolny recommendations for that genre yet."

def main():
  while True:
    user_message = input("You: ")
    response = greet(user_message)
    if response != "Hi! How can I help you today?":
      print(response)
      continue
    response = answer_question(user_message)
    if response != "I can't answer that yet, but I'm still learning!":
      print(response)
      if "movie" in response.lower():
        genre_response = recommend_movie(user_message)
        print(genre_response)
      continue
    print(response)
    break

if __name__ == "__main__":
  main()
