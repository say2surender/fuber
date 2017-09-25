# fuber
fuber -  an on call taxi service(test assignment)

Python/Flask

Contents:
app.py - controller
service.py - service
utils.py - utility functions
data.json - db
tests.py - tests
rides.log - logging the fares
requirements.txt - libraries needed to install


Setup:
1. Install Python
2. Git clone the app
3. Navigate to fuber directory
4. run "pip install requirements.txt"
5. run "python app.py"
6. App now runs on 'http://localhost:7777!'

Notes:
I have considered minutes as seconds, to get instant responses
The taxi will not be booked if no taxi is within 50km range from a passenger.
2 types of cars are available: economy, hipster

Sample inputs:
1. localhost:7777/user/taxi/request/  [POST]
   body: {
  	     "loc": {
            "lat": 55,
            "long": 87
          },
  	      "type":"economy"
         }
2. localhost:7777/user/taxi/end/  [POST]
    body: response of the taxi/request with updated end location
