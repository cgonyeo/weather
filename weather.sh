wget -q -O /tmp/weather.html http://www.wunderground.com/cgi-bin/findweather/getForecast?query=14623

python weather.py /tmp/weather.html 3

rm /tmp/weather.html
