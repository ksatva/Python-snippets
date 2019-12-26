"""
Now, since we are using JSON as our data format, we were able to take a nice shortcut here: 
the json argument to post. If we use that, requests will do the following for us:

    Convert that into a JSON representation string, à la json.dumps()
    Set the requests’ content type to "application/json" (by adding an HTTP header)
"""


# The shortcut
resp = requests.post('https://todolist.example.com/tasks/', json=task)
# The equivalent longer version
resp = requests.post('https://todolist.example.com/tasks/',
                     data=json.dumps(task),
                     headers={'Content-Type':'application/json'},

