import requests
import adviceAPI
import inspirationalAPI

def main():
  text = "Here is some random advice and inspirational quotes during your final season to make you smile."
  print(text)
  response = adviceAPI.RandomAdvice()
  response.get()
  info = response.motivate()
  print("Your random advice is:" + info["advice"])
  
  inspo = inspirationalAPI.InspirationalQuote()
  inspo.get()
  data = inspo.result()
  print("Your inspirational quote is: " + data["quote"])








main()