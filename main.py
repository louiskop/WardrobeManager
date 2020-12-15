
import requests, json 

somerClothes = ['GroenNetBroek','KhakiNetBroek','SwartNetLangBroek','groenBroek','BlouPatBroek','WitNikeHemp','WitBillaHemp','GrysBillaHemp','WitUniversalHemp','SwartKappaHemp']
wasDuration = 2

class Outfit:
    def __init__(self, id, formal, howHot, clothesinOutfit):
        self.id = id
        self.formal = formal
        self.howHot = howHot
        self.clothesinOutfit = clothesinOutfit
        self.lastWore
    
    def wear(today):
        self.lastWore = today


Outfits = [Outfit(1,True,"Hot",['GroenNetBroek','WitUniversalHemp']),Outfit(2,True,"Hot",['KhakiNetBroek','WitBillaHemp']),Outfit(3,True,"Cold",['SwartNetLangBroek','WitNikeHemp']),Outfit(4,True,"Cold",['groenBroek','GrysBillaHemp']),Outfit(5,True,"Cold",['BlouPatBroek','SwartKappaHemp'])]
 


def main():
    temprature = getCurrentTemprature()
    if temprature == "error":
        print("Oops! That city was not found")
        main()
    
    neat = raw_input("Casual or Formal or Both? (c/f/b)")
    tempList = []
    tempList2 = []
    if neat == f:
        for i in Outfits:
            if i.formal == True:
                tempList.append(i)
        for i in tempList:
            if temprature >= 14:
                if i.howHot == "Hot":
                    tempList2.append(i)
            
            elif temprature < 14:
                if i.howHot == "Cold":
                    tempList2.append(i)



    elif neat == c:
        for i in Outfits:
            if i.formal == false:
                tempList.append(i)
                for i in tempList:
        for i in tempList:
            if temprature >= 14:
                if i.howHot == "Hot":
                    tempList2.append(i)
            
            elif temprature < 14:
                if i.howHot == "Cold":
                    tempList2.append(i)
                
    elif neat == b:
        for i in Outfits:
            if temprature >= 14:
                if i.howHot == "Hot":
                    tempList2.append(i)
            
            elif temprature < 14:
                if i.howHot == "Cold":
                    tempList2.append(i)
    #Generate a random number to chooose the random outfit
    choice = tempList2[len(tempList2 -1)]
    #print the clothing items that are used in outfit
    print()
    #Change the washed date of the outfit and return to the main function


    
    else:
        print("Error no such argument")
        main()
    


def getCurrentTemprature():
    api_key = "709f6ef2dabacc65088df7d37a750a09"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = raw_input("Enter your city Name:")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    response = requests.get(complete_url)
    jsonResponse = response.json()

    if jsonResponse["cod"] != "404":
        main = jsonResponse['main']
        return (main['temp'] - 273.15)

    else:
        return "error"

main()