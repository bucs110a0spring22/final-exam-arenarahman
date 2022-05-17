import requests

class RandomAdvice:
  def __init__(self):
   """the constructor for RandomAdvice class and self stores api
    args: None
    return: None"""
    self.api_url = 'https://api.adviceslip.com/advice'

  def get(self):
    """retrieves the json file of the dictonary from the api
    args: None
    return: None"""
    req = requests.get(self.api_url)
    self.response = req.json()
    
    
    
  def motivate(self):
    """returns the json file containing the dictonary
    args:None
    return: (str) returns dictionary of random advice"""
    return self.response
    