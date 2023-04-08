import json

d = [{"Name" :"Preethi", "DOB" : "B+", "Height" : "4.5", "City" : "chennai", "State" : "TamilNadu"},
     {"Name" :"shinchan", "DOB" : "B+", "Height" : "5.5", "City" : "Anantapur", "State" : "Andhra"},
     {"Name" :"Suresh", "DOB" : "A-", "Height" : "6", "City" : "Panjali", "State" : "Goa"},
     {"Name" :"Kumar", "DOB" : "A+", "Height" : "4.5", "City" : "Palakkad", "State" : "Kerala"},
     {"Name" :"Jeni", "DOB" : "O+", "Height" : "5", "City" : "Solapur", "State" : "Maharashtra"}]  

with open('cricket.json', 'w') as f:
    json.dump(d, f)