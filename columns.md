Index(['FL_DATE', 'OP_CARRIER', 'OP_CARRIER_FL_NUM', 'ORIGIN', 'DEST',
       'CRS_DEP_TIME', 'DEP_TIME', 'DEP_DELAY', 'TAXI_OUT', 'WHEELS_OFF',
       'WHEELS_ON', 'TAXI_IN', 'CRS_ARR_TIME', 'ARR_TIME', 'ARR_DELAY',
       'CANCELLED', 'CANCELLATION_CODE', 'DIVERTED', 'CRS_ELAPSED_TIME',
       'ACTUAL_ELAPSED_TIME', 'AIR_TIME', 'DISTANCE', 'CARRIER_DELAY',
       'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY',
       'Unnamed: 27'],
      dtype='object')

 #   Column               Dtype  
---  ------               -----  
 0   FL_DATE              object 
 1   OP_CARRIER           object 
 2   OP_CARRIER_FL_NUM    int64  
 3   ORIGIN               object 
 4   DEST                 object 
 5   CRS_DEP_TIME         int64  
 6   DEP_TIME             float64
 7   DEP_DELAY            float64
 8   TAXI_OUT             float64
 9   WHEELS_OFF           float64
 10  WHEELS_ON            float64
 11  TAXI_IN              float64
 12  CRS_ARR_TIME         int64  
 13  ARR_TIME             float64
 14  ARR_DELAY            float64
 15  CANCELLED            float64
 16  CANCELLATION_CODE    object 
 17  DIVERTED             float64
 18  CRS_ELAPSED_TIME     float64
 19  ACTUAL_ELAPSED_TIME  float64
 26  LATE_AIRCRAFT_DELAY  float64
 27  Unnamed: 27          float64


 
FL_DATE: The flight date.
OP_CARRIER: The airline carrier code.
OP_CARRIER_FL_NUM: The flight number for that airline carrier.
ORIGIN: The airport code for the origin airport.
DEST: The airport code for the destination airport.
CRS_DEP_TIME: The scheduled departure time.
DEP_TIME: The actual departure time.
DEP_DELAY: The difference in minutes between the scheduled and actual departure time.
TAXI_OUT: The amount of time in minutes it took for the plane to taxi from the gate to the runway.
WHEELS_OFF: The actual time when the plane left the gate.
CRS_ELAPSED_TIME: The scheduled flight time in minutes.
ACTUAL_ELAPSED_TIME: The actual flight time in minutes.
AIR_TIME: The amount of time in minutes that the plane was in the air.
DISTANCE: The distance between the origin and destination airports in miles.
CARRIER_DELAY: The amount of time in minutes that the delay was due to the airline.
WEATHER_DELAY: The amount of time in minutes that the delay was due to weather.
NAS_DELAY: The amount of time in minutes that the delay was due to the National Airspace System.
SECURITY_DELAY: The amount of time in minutes that the delay was due to security issues.
LATE_AIRCRAFT_DELAY: The amount of time in minutes that the delay was due to a previous flight using the same aircraft arriving late.