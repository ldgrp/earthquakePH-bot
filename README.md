EarthquakePH Bot
===================

This is a Python bot that tweets when earthquakes occur in the Philippines. Created for the [@earthquakePH](http://twitter.com/earthquakePH) twitter account.

Uses the [USGS API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) to get earthquake data.


```
http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson
```

Dependency
-----

You will need to install Python 3 on your system. After that, you will also need the [tweepy](https://github.com/tweepy/tweepy) library. You can do so by running the following command:

```pip install tweepy```

Usage
-------
Once you've provided the necessary API keys, run the bot from the commandline
```python main.py
```
