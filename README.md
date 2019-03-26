# Raspberry Smartwatch Simulator

[![N|Solid](https://raw.githubusercontent.com/iiiypuk/rpi-icon/master/256.png)](https://www.raspberrypi.org/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This is a college project that I made using a raspberry pi and some python. Functionalities of the project include: 

  - Ability to read messages you recieve on your phone on the smartwatch(Raspberry Pi)
  - Ability to read .txt files
  - Read your phone's sensor data
  - Estimate number of steps you've taken
  - And most importantly, execute shell commands remotely from your smartphone to your linux based smartwatch/laptop!

This project uses a number of open source projects and apps to work properly:

* [Pushbullet App](https://play.google.com/store/apps/details?id=com.pushbullet.android&referrer=utm_source%3Dpushbullet.com) - Send your mesages and files across different paltforms using a single app!
* [Pushbullet API](https://docs.pushbullet.com/) - API used for enabling cross platform communication.
* [PhonePI App](https://play.google.com/store/apps/details?id=com.phonepi&hl=en_IE) - For streaming sensor data to our Raspberry Pi.
* [PhonePI Sample Server](https://github.com/priyankark/PhonePi_SampleServer) - Sample server from the creator of the awesome app.
* [Python 3.6.8](https://www.python.org/downloads/release/python-368/) - Any other version of Python 3 should aslo work
