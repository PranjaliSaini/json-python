#NAME : Sakshi saini
#Roll number : 2017092

import urllib.request
from datetime import date,datetime,timedelta


f=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=Delhi&APPID=2ab136be1543b5789451a5994364c0d3')
json=f.read().decode()


# function to get weather response
def weather_response(location, API_key):
    try:
        f=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key)
        json=f.read().decode()
        return (json)
    except:
        pass
  # write your code 

# function to check for valid response 
def has_error(location,json):
  # write your code
    search=json.find(location)
    if search >=0:
        return(False)
    else:
        return(True)


# function to get attributes on nth day
def get_temperature (json, n=0,time='21:00:00'):
    try :
        n>=0 and n<=4
        days=n
          #getting today's date
        today_date=date.today()
    
          #modifying date i.e adding n days to the present date
        modified_date=today_date + timedelta(days=n)
    
          #makig a final substring something like 2017-08-09 21:00:00
        substring=str(modified_date) + time
    
          #finding the index of the final substring
        f_index=json.find(substring)
    
          #finding the word "temp" using reverse find function
        index=json.rfind('"temp"',0,f_index)
    
          #returning thevalue of temperature using slicing
        return(float(json[index+7:index+14]))
    except:
        pass
    

def get_humidity(json, n=0,time='21:00:00'):

    # write your code
    try :
        n>=0 and n<=4
        days=n
          #getting today's date
        today_date=date.today()

      #modifying date i.e adding n days to the present date
        modified_date=today_date + timedelta(days=n)

      #makig a final substring something like 2017-08-09 21:00:00
        substring=str(modified_date) + time
    
      #finding the index of the final substring
        f_index=json.find(substring)

      #finding the word "temp" using reverse find function
        index=json.rfind('"humidity"',0,f_index)

      #returning thevalue of temperature using slicing
        return(float(json[index+11:index+13]))
        print(modified_date)
    except:
        pass

  

def get_pressure(json, n=0,time='21:00:00'):
  # write your code
    try :
        n>=0 and n<=4
        days=n
      #getting today's date
        today_date=date.today()
      #modifying date i.e adding n days to the present date
        modified_date=today_date + timedelta(days=n)

      #makig a final substring something like 2017-08-09 21:00:00
        substring=str(modified_date) + time

      #finding the index of the final substring
        f_index=json.find(substring)

      #finding the word "temp" using reverse find function
        index=json.rfind('"pressure"',0,f_index)

      #returning thevalue of temperature using slicing
        return(float(json[index+11:index+16]))
    except:
        pass
  



def get_wind(json, n=0,time='21:00:00'):
  # write your code
  try :
        n>=0 and n<=4
        days=n
      #getting today's date
        today_date=date.today()
    
      #modifying date i.e adding n days to the present date
        modified_date=today_date + timedelta(days=n)
    
      #makig a final substring something like 2017-08-09 21:00:00
        substring=str(modified_date) + time

      #finding the index of the final substring
        f_index=json.find(substring)

      #finding the word "speed" using reverse find function
        index=json.rfind('"speed"',0,f_index)

      #returning thevalue of temperature using slicing
        return(float(json[index+8:index+12]))
  except:
      pass



def get_sealevel(json, n=0,time='21:00:00'):
  # write your code
    try :
        n>=0 and n <=4
        days=n
      #getting today's date
        today_date=date.today()
      #modifying date i.e adding n days to the present date
        modified_date=today_date + timedelta(days=n)
      #makig a final substring something like 2017-08-09 21:00:00
        substring=str(modified_date) + time

      #finding the index of the final substring
        f_index=json.find(substring)

      #finding the word "sealevel" using reverse find function
        index=json.rfind('"sea_level"',0,f_index)

      #returning thevalue of temperature using slicing
        return(float(json[index+12:index+19]))
    
    except:
        pass
    



