# 1st 
import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employee_list = []

with open(r'D:\git hub\DS140823-1\employee.json', 'r') as json_file:
    data = json.load(json_file)
    for employee_data in data:
        name = employee_data["name"]
        dob = employee_data["DOB"]
        height = employee_data["height"]
        city = employee_data["city"]
        state = employee_data["state"]
        
        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")
"""
expected output
Name: Alice Johnson, DOB: 1992-08-10, Height: 5'6", City: San Francisco, State: California
Name: Bob Smith, DOB: 1988-03-25, Height: 5'10", City: Miami, State: Florida
Name: Eva Martinez, DOB: 1995-11-18, Height: 5'4", City: Houston, State: Texas
Name: David Wilson, DOB: 1990-06-03, Height: 6'0", City: Denver, State: Colorado
Name: Grace Davis, DOB: 1987-09-15, Height: 5'7", City: Seattle, State: Washington

"""
"""
json data
[
    {
      "name": "Alice Johnson",
      "DOB": "1992-08-10",
      "height": "5'6\"",
      "city": "San Francisco",
      "state": "California"
    },
    {
      "name": "Bob Smith",
      "DOB": "1988-03-25",
      "height": "5'10\"",
      "city": "Miami",
      "state": "Florida"
    },
    {
      "name": "Eva Martinez",
      "DOB": "1995-11-18",
      "height": "5'4\"",
      "city": "Houston",
      "state": "Texas"
    },
    {
      "name": "David Wilson",
      "DOB": "1990-06-03",
      "height": "6'0\"",
      "city": "Denver",
      "state": "Colorado"
    },
    {
      "name": "Grace Davis",
      "DOB": "1987-09-15",
      "height": "5'7\"",
      "city": "Seattle",
      "state": "Washington"
    }
  ]
  """

# 2nd
import json

indian_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

with open('indian_capitals.json', 'w') as json_file:
    json.dump(indian_capitals, json_file)

print("Data has been written to 'indian_capitals.json' successfully.")