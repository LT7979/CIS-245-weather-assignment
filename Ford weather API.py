import requests
import json
def main():
    #asks for zipcode
    zip = input("welcome to the weather getter! Weather will be shown in imperial units (fahrenheit,MPH) \n please enter your US zipcode to see the current weather: ")
    #sends API request with zip code
    try:
        response2 = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&units=imperial&appid=f2b31e94ffa61826806d46f2b74ed462")
    except:
        print ("\nerror, could not connect to API service (check your connection)\n")
        main()
    #prints status code
    print (response2.status_code)
    #checks if status code is valid, if not it will prompt user for valid input
    if response2.status_code == 200:
        print("zipcode: OK")
    elif response2.status_code == 404:
        print("error, invalid zip code. Please enter valid zip code")
        main()
    else:
        print (response2.status_code)
        print ("error, please read response code above \n")
        main()

    #creates dictionary using the received json data after converting the data to string format
    dict1 = json.loads(response2.text)
    #creates dictionary to store weather data
    dict2 = {}
    
#uses multiple for loops to parse out what data needs to be displayed and stores it in dict2
    for val in dict1["weather"][0]:
        dict2[val] = dict1["weather"][0][val]
    for val in dict1["main"]:
        dict2[val] = dict1["main"][val]
    #prints keys and values in dict 2 for displaying
    for key, val in dict2.items():
        print ("{}: {}".format(key,val))
    print ("windspeed: " , dict1["wind"]["speed"] , " MPH")
    print ("Location Name: " , dict1["name"])
    restartpr()
#typical restart function
def restartpr():
    restart = input("would you like to restart the program? Y/N: ")
    if restart.upper() == "Y":
        main()
    if restart.upper() == "N":
        exit
    else:
        print("please enter valid choice")
        restartpr()



main()


