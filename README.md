# PITT-CS-Indoor-Navigation

## Demo
Python 3.8 and Pip required

In your terminal, run
```console
git clone git@github.com:kevinzhao81/PITT-CS-Indoor-Navigation.git
```
```console
cd PITT-CS-Indoor-Navigation
```
```console
pip install django networkx matplotlib numpy
```
```console
python manage.py runserver
```

Now you can open <http://127.0.0.1:8000/process/> in your browser to enter room numbers and navigate!

You can also enter the source room id in the URL, e.g., <http://127.0.0.1:8000/process/?room=6150>

## Test on your phone
Connect your computer and your phone in the same local network. Add the IP address of your computer to the `ALLOWED_HOSTS` in `myproject/settings.py`.

Then in your terminal run
```console
python manage.py runserver 0.0.0.0:8000
```

Now open <http:/YOUR_IP_ADDRESS:8000/process/> on the browser on your phone. Done!

## Developer notes
`myapp/views.py` is the basic develping file. It contains the navigation and web rendering modules.

`myapp/templates` folder contains the web html files.

`static` folder contains the needed resources, including map images and staff head portraits.

`myproject/settings.py` is responsible for all the settings for the project. You can config the database connection in this file.


