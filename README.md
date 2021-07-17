# WeatherAPI
**This Project is deals with fetch the data from openweatherapi and using the DRF.**

**Use https://openweathermap.org/ One Call API to fetch and store the target location’s weather
with metadata (e.g. current weather, hourly forecast for 48 hours, daily forecast for 7 days) for a
particular latitude and longitude and create an MVT using Django and the Django REST
Framework.
The MVP should contain the following API endpoints:**
<ul>
  <li>1. API 1 to trigger a weather search for a particular lat long. (e.g.
lat=33.441792&lon=-94.037689 ).</li>
     <ul>
       <li>a. Trigger search for lat, long sent in request </li>
       <li>b. Fetch weather data from openweathermap’s Once Call API and store a normalized and curated version of the weather data.</li>
       <li>c. Architect appropriate database and schema keeping redundancy and query simplicity in mind.</li>
     </ul>
  <li>2. API 2 to return stored weather data and their metadata based on applied filters/search.</li>
     <ul>
       <li>a. API should be paginated</li>
       <li>b. It must support text search for text data.</li>
       <li>c. It must have sorting available by date time, text, etc</li>
       <li>d. API should have filters like main weather description (Rain, Thunderstorm),
timezone (America/Chicago), temp, pressure, humidity, wind_speed, visibility, etc
(the more, the merrier) in such a way that:</li>
       <ul>
         <li>i. Data range filter in case of date column</li>
         <li>ii. Less than, greater than, equal to filter in case of integer column (e.g.
wind_speed)</li>
         <li>iii. Start with, ends with, contains, exact match in case of string column (e.g.
timezone)</li>
       </ul>
       <li>3. API 3 to export filtered data as CSV with selected columns of your choice (whichever
columns make more sense to have in csv for lets say someone who wants to perform
some analysis on it)</li>
     </ul>
</ul>


## Steps to Run 
1. Download or Clone the Repository:    **https://github.com/ankurpython/trueqc_project.git**
2. Make sure to install requirements.txt file:  **https://github.com/ankurpython/trueqc_project/blob/master/weather/requirements.txt**
* ```pip install -r requirments.txt```*
   
4. After all the installation complete use the django command to runserver:   ```py manage.py runserver```
5. Open the browser: **http://localhost:8000**


## Screenshots

### 1. **Base Page**

![base_page](https://user-images.githubusercontent.com/48859058/126047142-48d5412f-7bdf-4047-9c8d-07b77db94311.png)


### 2. **Weather Data Trigger with lat=33.441792&lon=-94.037689**

![Trigger_search](https://user-images.githubusercontent.com/48859058/126047279-c2168f5a-2e42-40b1-a220-9b918e65bd71.png)


### 3. **Weather Data Trigger with Dubai lat= 25.276987 & lon= 55.296249**

![Dubai lat   lon weather data](https://user-images.githubusercontent.com/48859058/126047344-144e60e3-9717-4319-b2f8-577aab8a487f.png)


### 4. **Filteration with temp__gt value**

![filteration of gt](https://user-images.githubusercontent.com/48859058/126047383-74bb625d-d0b2-4643-a4fc-1a45c64eec9a.png)

### 5. **Generate of CSV File**

![weather_csv file](https://user-images.githubusercontent.com/48859058/126047404-c81e4ba4-9af8-4b68-a817-344e693ea873.png)

## Thank You, If you have any query please feel free to reach.
