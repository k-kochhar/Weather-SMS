# Weather-SMS

This program takes use of my Email Sender that I made earlier. It basically gets information off of a google form that people enter information regarding their location
and sends them a personalized text at 7:00am EST. The actual sending at the designated time is done using AWS Lambda along with AWS Cloud Watch, which isn't shown in
this repository.

Anyways it uses the information off a google form, specifically their state and city, to generate an API request that includes their current weather stats provided by
the OpenWeather API. Using the information from the API, it then customizes a text sent to their phone, using their name, city, and weather data. 

If you want to sign up for the daily weather text at 7:00am EST, fill out the following Google Form 

https://forms.gle/HE1gpz1LcWa1ocFz5

If you have any questions, please let me know. 
