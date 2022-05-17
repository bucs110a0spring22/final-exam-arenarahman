import requests 

class InspirationalQuote:
  def __init__(self):
    """constructor for InspirationalQuote class and self saves the url
    args:none
    return: none """
    self.api_url = "https://api.goprogram.ai/inspiration"
  
  def get(self): 
    """retrieves the json file of the api
    args: none
    return: none"""
    req = requests.get(self.api_url)
    self.encourage = req.json()

  def result(self):
    """returns the dictionary of the api
    args: none
    return: returns the dictonary """
    return self.encourage
    
  
    