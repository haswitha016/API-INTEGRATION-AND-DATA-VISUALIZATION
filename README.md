# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY NAME*: CODTEC IT SOLUTIONS

*NAME*: CHERUKURI HASWITHA

*INTERN ID*: CT04DN1446

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

*DESCRIPTION OF MY TASK(API Integration and Data Visualization Using Python)*

          This Task focuses on developing hands-on skills in *API integration* and *data visualization* using Python. This task is designed to introduce interns to the foundational principles of working with real-time data from web APIs and representing that data graphically to extract insights. In this task, the intern(me) is required to retrieve weather data for a specific location — Anantapur — and visually present key weather parameters.
## Objective
The core objective of this task is to understand how to:
* Connect to a third-party weather API (OpenWeatherMap)
* Fetch and process real-time data for Anantapur town
* Create a meaningful visualization using Python libraries like Matplotlib.
The focus is on integrating real-world data into a Python program and demonstrating its relevance through clear and concise visual output. This task builds critical skills that are useful in software development, data analysis, and machine learning pipelines.
## Tools and Technologies used
1. *Python*: The primary programming language used due to its simplicity and powerful data handling capabilities.
2. *OpenWeatherMap API*: A popular web service that provides weather information in real time for any city globally. It returns data in JSON format, which is easy to parse and use in Python.
3. *VS code*: an app used to run the code and to get teh outputs
4. *Requests Library*: This Python library is used for making HTTP requests to the weather API.
5. *Matplotlib*: A robust plotting library used to generate bar charts that visually represent temperature, humidity, and wind speed.
## Implementation Steps
1. *API Key Setup*: The user needs to register on OpenWeatherMap.org and obtain a free API key. This key is used to authenticate requests and access weather data.
2. *Fetching Weather Data*: A Python function is created using the `requests` library to send a GET request to the API. The request includes the city name (“Anantapur,IN”) and the API key. The response is parsed from JSON to extract key parameters like temperature, humidity, wind speed, and weather description.
3. *Data Handling*: The extracted data is stored in a Python dictionary for ease of access. Proper error handling is implemented to catch and report failed API calls (e.g., wrong city name or invalid API key).
4. *Data Visualization*: Using the Matplotlib library, a bar chart is generated to represent the key weather parameters. The chart is clearly labeled with axes, gridlines, and a title that includes the weather description. The use of color coding for different parameters improves readability.
## Key Outcomes of the task
*Practical API Integration*: Interns learn how to connect Python applications to external APIs and work with JSON data structures, which is a crucial skill in web and data applications.
*Visualization Skills*: By using Matplotlib, interns gain experience in transforming raw data into intuitive visual formats that aid in decision-making and analysis.
*Real-World Data Handling*: Working with live data helps interns understand issues like API limits, error codes, data refresh intervals, and the importance of clean and efficient data extraction.
## Applications of the task
This task not only serves as a basic introduction to API and visualization but also lays the groundwork for more advanced projects such as:
Weather dashboards,
IoT-based environmental monitoring systems,
Smart city data analytics,
Climate trend analysis tools, and more.
## Conclusion of the task
In this task, I learned how to get live weather data using an API and show it with simple graphs. It helped me understand how to connect Python with real-time data. This is useful for many real-world projects like weather apps or dashboards.
