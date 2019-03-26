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

# Streaming sensor data from your smartphone to your raspberry pi:
First of all make sure you have installed *PhonePi app* as instructed above. Now connect your smartphone to the same network as your raspberry. Then follow the commands given below:
 * First clone the project as shown below

```sh
$ git clone https://github.com/Naman1997/Raspberry_smartwatch
```
* Now find out the ip of your Raspberry Pi
```sh
$ ifconfig
```
* Your ip would be in the second line next to *inet*. Note it down, it will be useful later. I will refer it as YOUR_IP
* Next cd into the 'Raspberry_smartwatch' directory and run the following command
```sh
$ python3 PhonePi.py
```
* This will start your flask server and expose port 5000 in the network. Now open the PhonePi app in your smartphone and in the text enrty field type
```sh
$ YOUR_IP:5000
```
* You should now be able to send various sensor data streams to your Pi by toggling them in the app.
