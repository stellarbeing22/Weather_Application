import customtkinter as ct
from geopy.geocoders import Nominatim
from datetime import datetime 
from timezonefinder import TimezoneFinder
import requests
import pytz

#setting up root
root = ct.CTk()
root.title("Weather App")
root.iconbitmap("logo.png")
ct.set_appearance_mode("system")
ct.set_default_color_theme("dark-blue")
root.geometry("800x500")
root.resizable(False, False)
temp_for_func = []

def api_(location):
    # weather
    apikey = "ef1569cd4031b8e068ea28a278453c95"
    lon = str(round(location.latitude,2))
    lat = str(round(location.longitude,2))
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+ lon + "&lon="+ lat +"&units=metric&appid="+ apikey 
    fetch_data(api)

def fetch_data(api):
    json_data =requests.get(api).json()
    temp = json_data["main"]["temp"] 
    feels_like = json_data["main"]["feels_like"]
    humi_dity= json_data["main"]["humidity"]
    prea_ssure = json_data["main"]["pressure"]
    wind = json_data["wind"]["speed"]
    winddirection = json_data["wind"]["deg"]
    descri_ption= json_data["weather"][0]["description"]
    temp_min = json_data["main"]['temp_min']
    temp_max = json_data["main"]['temp_max']
    sunrise_time = json_data['sys']['sunrise']
    sunset_time = json_data['sys']['sunset']
    visibility = json_data["visibility"]/1000
    clouds = json_data["clouds"]["all"]
    name = json_data["name"]    
    #updates
    Temperature.configure(text = str(round(temp))+'°C')
    Feelslike.configure(text = "Feels Like"+ str(round(feels_like))+'°C')
    Humidity_data.configure(text = str(humi_dity)+'%')
    Preassure_data.configure(text = str(prea_ssure)+' mbar')
    Wind_speed_data.configure(text = str(wind)+'m/s')
    Description.configure(text = descri_ption)
    min_temp.configure(text = "Low: "+ str(round(temp_min)) + ' °C')
    max_temp.configure(text = "High: "+ str(round(temp_max)) + ' °C')
    risetime.configure(text = unixtotime(sunrise_time))
    settime.configure(text = unixtotime(sunset_time))
    Wind_direction_data.configure(text = str(winddirection)+" deg")
    visibility_data.configure(text = str(visibility)+" Km")
    clouds_data.configure(text = str(clouds)+"%")
    label.configure(text = name)
    temp_for_func.append(temp)
    temp_for_func.append(feels_like)
    temp_for_func.append(temp_min)
    temp_for_func.append(temp_max) 
    
def unixtotime(a):
        import datetime
        timestamp = datetime.datetime.fromtimestamp(a)
        return timestamp.strftime('%I:%M %p')

def getweather():
    if entry.get() != "":
        city = entry.get()
    else:
        label.configure(text ="enter a valid location")
    print(city)
    geolocator = Nominatim(user_agent = "geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lat = location.latitude, lng = location.longitude)  # type: ignore
    Timezone.configure(text = result)
    long_lat.configure(text = f"{round(location.latitude, 4)}°N,{round(location.longitude,4)}°E")# type: ignore
    home = pytz.timezone(result)# type: ignore
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    Time.configure(text = current_time)
    api_(location)
    print(result,home)

def currentlocation():
    import geocoder
    geolocator = Nominatim(user_agent="geoapiExercises")
    g = geocoder.ip('me')
    latlong = g.latlng
    Latitude = latlong[0]
    Longitude = latlong[1]
    location = geolocator.reverse(str(Latitude)+","+str(Longitude))
    obj = TimezoneFinder()
    result = obj.timezone_at(lat = location.latitude, lng = location.longitude)  # type: ignore
    Timezone.configure(text = result)
    long_lat.configure(text = f"{round(location.latitude, 4)}°N,{round(location.longitude,4)}°E")# type: ignore
    home = pytz.timezone(result)# type: ignore
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    Time.configure(text = current_time)
    api_(location)
    print(result,home)

def C_to_F():
    if temp_for_func != []:
        temp = temp_for_func[0]
        feels_like = temp_for_func[1]
        temp_min = temp_for_func[2]
        temp_max = temp_for_func[3]
        Ftemp = (temp+32)*9/5
        F_feelslike = (feels_like +32)*9/5
        F_tempmax = (temp_max +32)*9/5
        F_tempmin = (temp_min +32)*9/5
        Temperature.configure(text = str(round(Ftemp))+'°F')
        Feelslike.configure(text = "Feels Like"+ str(round(F_feelslike))+'°F')
        min_temp.configure(text = "Low: "+ str(round(F_tempmin)) + ' °F')
        max_temp.configure(text = "High: "+ str(round(F_tempmax)) + ' °F')
    else: 
        pass

def F_to_C():
    if temp_for_func != []:
        temp = temp_for_func[0]
        feels_like = temp_for_func[1]
        temp_min = temp_for_func[2]
        temp_max = temp_for_func[3]
        Temperature.configure(text = str(round(temp))+'°C')
        Feelslike.configure(text = "Feels Like"+ str(round(feels_like))+'°C')
        min_temp.configure(text = "Low: "+ str(round(temp_min)) + ' °C')
        max_temp.configure(text = "High: "+ str(round(temp_max)) + ' °C')
    else:
        pass

#frame
frame = ct.CTkFrame(master=root)
frame.pack(
    pady = "25",
        padx = "25", 
            fill = "both", 
                expand = "true")

frame0 = ct.CTkFrame(master = root,
    height = 40,
        width=200,
            fg_color= "grey30")
frame0.place(x= 70, y = 300)

frame1 = ct.CTkFrame(master = root,
    height = 40,
        width=200,
            fg_color= "grey30")
frame1.place(x= 300, y = 300)

frame2 = ct.CTkFrame(master = root,
    height = 40,
        width=200,
            fg_color= "grey30")
frame2.place(x= 530, y = 300)

frame3 = ct.CTkFrame(master = root,
    height = 40,
        width=200,
            fg_color= "grey30")
frame3.place(x= 70, y = 370)

frame4 = ct.CTkFrame(master = root,
    height = 40,
        width=200,
            fg_color= "grey30")
frame4.place(x= 300, y = 370)

frame5 = ct.CTkFrame(master = root,
    height = 40,
        width=200,
            fg_color= "grey30")
frame5.place(x= 530, y = 370)

#attributes
Temperature= ct.CTkLabel(master = frame, 
    text = " 00°C",  
        font = ("Helvetica",42))
Temperature.place(x = 50, y=110+20)

Feelslike = ct.CTkLabel(master = frame, 
    text = "feels like 00 °C",  
        font = ("Helvetica",16))
Feelslike.place(x = 50, y=160+20)

min_temp = ct.CTkLabel(master = frame,
    text = "low",
        font = ("Helvetica",16))
min_temp.place(x = 170, y = 160+20)

max_temp = ct.CTkLabel(master = frame,
    text = "high",
        font = ("Helvetica",16))
max_temp.place(x = 170, y = 135+20)

#sunrise time
riselabel = ct.CTkLabel(master = frame,
    text = "sunrise: ",
        font=("Helvetica",16))
riselabel.place(x = 570,y=150)

#sunset time
setlabel = ct.CTkLabel(master = frame,
    text = "sunset : ",
        font=("Helvetica",16))
setlabel.place(x = 570,y=170)

# Wind_speed
Wind_speed = ct.CTkLabel(master = frame0, 
    text = "Wind speed: ", 
        font = ("Helvetica",18 ),
            bg_color="gray30")
Wind_speed.place(x = 7, y = 6)

# Preassure
Preassure = ct.CTkLabel(master = frame1, 
    text = "Preassure: ", 
        font = ("Helvetica",18),
            bg_color="grey30")
Preassure.place(x = 7, y = 6)

# Humidity
Humidity = ct.CTkLabel(master = frame2, 
    text = "Humidity: ", 
        font = ("Helvetica",18),
            bg_color="gray30")
Humidity.place(x = 7, y = 6)

# Wind direction
Wind_direction= ct.CTkLabel(master = frame3, 
    text = "Wind direction: ", 
        font = ("Helvetica",18),
            bg_color="gray30")
Wind_direction.place(x = 7, y = 6)

# visibility
visibility = ct.CTkLabel(master = frame4, 
    text = "Visibility: ", 
        font = ("Helvetica",18),
            bg_color="gray30")
visibility.place(x = 7, y = 6)

# clouds
clouds= ct.CTkLabel(master = frame5, 
    text = "Clouds: ", 
        font = ("Helvetica",18),
            bg_color="gray30")
clouds.place(x = 7, y = 6)

label = ct.CTkLabel(master = frame,
        text = "",
            font = ("Helvetica",18))
label.place(x= 30,y=10)

# Description
Description = ct.CTkLabel(master = frame, 
    text = "--",
        font = ("Helvetica",16))
Description.place(x = 170, y = 110+20)

# Time
Time = ct.CTkLabel(master = frame, 
    text = "00:00",
        font = ("Helvetica",32))
Time.place(x = 570, y = 100)

#timezone
Timezone = ct.CTkLabel(master = frame,
        text="--",
    font = ("Helvetica",22))
Timezone.place(x = 570, y = 20)

long_lat = ct.CTkLabel(master = frame,
        text="--°N, --°E",
    font = ("Helvetica",16))
long_lat.place(x = 570, y = 45)

# Location
entry = ct.CTkEntry(
    master = frame, 
        placeholder_text= "Enter location", 
        width = 200, 
            height = 35,
                font= ("poppins",18, "bold")
            )
entry.place(x = 30, y = 50)

# Search
Search = ct.CTkButton(
    master = frame, 
        text = "🔍",
            font = ("Helvetica",24),
                height= 35,
                    width= 30,
                        command= getweather)
Search.place(x =250, y = 50)

current_location = ct.CTkButton(
    master = frame, 
        text = "use current location",
            font = ("Helvetica",18),
                height= 35,
                    width= 150,
                        command= currentlocation)
current_location.place(x =300, y = 50)

ctof = ct.CTkButton(
    master = frame, 
        text = "°F",
            font = ("Helvetica",16),
                height= 35,
                    width= 30,
                        command= C_to_F)
ctof.place(x =270, y = 165)

ftoc = ct.CTkButton(
    master = frame, 
        text = "°C",
            font = ("Helvetica",16),
                height= 35,
                    width= 30,
                        command= F_to_C)
ftoc.place(x =310, y = 165)

# Data
risetime = ct.CTkLabel(master=frame, 
    text = "00:00",
        font=("Helvetica",16))
risetime.place(x = 630, y= 150)

settime = ct.CTkLabel(master=frame, 
    text = "00:00",
        font=("Helvetica",16))
settime.place(x = 630, y= 170)

Wind_speed_data= ct.CTkLabel(master = frame0, 
    text = "       --", 
        font = ("Helvetica",18),
            bg_color="gray30")
Wind_speed_data.place(x = 115, y=6)

Preassure_data= ct.CTkLabel(master = frame1, 
    text = "     --", 
        font = ("Helvetica",18),
            bg_color="gray30")
Preassure_data.place(x = 100, y=6)

Humidity_data = ct.CTkLabel(master = frame2, 
    text = "      --", 
        font = ("Helvetica",18),
            bg_color="gray30")
Humidity_data.place(x = 85, y=6)

Wind_direction_data = ct.CTkLabel(master = frame3, 
    text = "    --", 
        font = ("Helvetica",18),
            bg_color="gray30")
Wind_direction_data.place(x = 131, y=6)

visibility_data = ct.CTkLabel(master = frame4, 
    text = "         --", 
        font = ("Helvetica",18),
            bg_color="gray30")
visibility_data.place(x = 80, y=6)

clouds_data = ct.CTkLabel(master = frame5, 
    text = "        --  ", 
        font = ("Helvetica",18),
            bg_color="gray30")
clouds_data.place(x = 75, y=6)

root.mainloop()