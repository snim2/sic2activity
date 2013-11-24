sci2activity
============

RESTful web app to convert UK Standard Industrial Classification codes to 
textual descriptions. All output is in JSON.


There is a reference implementation of this app at: http://sic2activity.herokuapp.com

API Guide
---------

### GET Requests

 * `/api/sics/` - Return a list of all 2007 SIC codes.
 * `/api/sics2007/` - Return a list of all 2007 SIC codes.
 * `/api/sics2003/` - Return a list of all 2003 SIC codes.
 * `/api/activities/` - Return a list of all activity descriptions.
 * `/api/sic/12345/` - Return activity description for 2007 SIC code 12345
 * `/api/sic/2007/12345/` - Return activity description for 2007 SIC code 12345
 * `/api/sic/2003/12345/` - Return activity description for 2003 SIC code 12345
 
### Example Requests and Responses

#### All 2007 SICs

Request:

    /api/sics/
    
Response:

    {
      "sic_2007": [
        "23990", 
        "35230", 
        "61100",
        ...
      ]
    } 


#### All activities

Request:

    /api/activities/

Response:

    {
      "activities": [
        "Office cleaning contractor", 
        "Wood worm preventative treatment service", 
        "Window cleaning", 
        ...
      ]
    }

#### Specific 2007 SIC

Request:

    /api/sic/86230

Response:

    {
      "activity": [
        "Community dental service clinics", 
        "Dental activities in operating rooms", 
        "Dental clinic", 
        "Dental clinic (health service)", 
        "Dental practice activities", 
        "Dental receptionist", 
        "Dental surgeon (not employed full time by a hospital)", 
        "Dentist", 
        "Endodontic dentistry ", 
        "Oral pathology", 
        "Orthodontic activities", 
        "Paediatric dentistry "
      ], 
      "sic": "86230"
    }
