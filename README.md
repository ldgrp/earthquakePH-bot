EarthquakePH Bot
===================

This is a Python bot that tweets when earthquakes occur in the Philippines. Created for the [@earthquakePH](http://twitter.com/earthquakePH) twitter account, based on the [WAGG-Earthquake-Bot](https://github.com/WAGGNews/WAGG-Earthquake-Bot)

Uses the [USGS API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) to acquire earthquake data.


Dependency
-----

You will need to install Python 3 on your system. After that, you will also need the [tweepy](https://github.com/tweepy/tweepy) and [requests](https://github.com/kennethreitz/requests) library. You can do so by running the following commands:

```pip install tweepy
pip install requests
```

Usage
-------
Once you've provided the necessary API keys, run the bot from the commandline
```python main.py```
