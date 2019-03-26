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

### Installation

Install the dependencies as shown:

```sh
$ pip3 install flask
$ pip3 install flask_sockets
$ pip3 install asyncio
$ pip3 install traceback
$ pip3 install subprocess
$ pip3 install asyncpushbullet
$ pip3 install matplotlib
$ pip3 install scipy
$ pip3 install numpy
```

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
* Your ip would be in the second line next to *inet*. Note it down, it will be useful later. I will refer to it as YOUR_IP
* Next cd into the 'Raspberry_smartwatch' directory and run the following command
```sh
$ python3 PhonePi.py
```
* This will start your flask server and expose port 5000 in the network. Now open the PhonePi app in your smartphone and in the text enrty field type
```sh
$ YOUR_IP:5000
```
* You should now be able to send various sensor data streams to your Pi by toggling them in the app.
* When you close the app, your data steams will be saved in their respected files inside the same directory.

# Counting steps with your smartphone's accelerometer:
Once you've completed the instructions given above, then you can run the script for counting steps. Follow the commands given below:
 * Start the server as shown above
 * Open your PhonePi App
 * Toggle only the *Accelerometer* switch
 * Now walk with the app still running
 * Toggle the switch again and close the app
 * You might have to press Ctrl+C to stop the server on your Raspberry Pi
 * Your data should have been saved. To check it open *acceleometer.txt* file and check.
 * Now that you have the data; run:

```sh
$ python3 step_counter_peaks.py
```
* This will generate a graph and print out the number of steps taken in the terminal.
* Your accuracy might vary depending upon the quality of sensor and the value height you set inside *accelerometer.py*. You might need to tinker around with the height value(on line 33) till you get accurate results.

# Recieving your smartphone notifications on your RPi smartwatch:
Follow the commands given below:
 * Go to [Pushbullet's Website](https://www.pushbullet.com/) and sign into your account.
 * Go to *Settings* and click on *Create Access Token*
 * This will give you an access token with which you can access your phone's messsges.
 * Copy the access token
 * Edit the data.py file and instead of #YOUR API KEY(on line 13), paste your access token.
 * Now run the python script
```sh
$ python3 data.py
```
* Now open your Pushbullet App in your smartphone and send a message to *All devices* to check if the connection has established.

# Sending commands and to-do files to your RPi smartwatch:
I'll be assuming that you completed the section just above this one. Follow the commands given below:
 * Run the command to start the service
```sh
$ python3 data.py
```
 * Open your Pushbullet App in your smartphone and attach a .txt to-do file to all devices. The script will recieve the file and print out its contents in the terminal.
* In order to run shell commands from your smartphone, type a '$' sign before sending the instruction from your smartphone.
* For example: To download a file on your smartwatch, type the following in your Pushbullet smartphone app
```sh
$ wget APP_LINK
```
* Here APP_LINK refers to the link address of the file you want to downlaod
* This can come in handy if you want to download files on your PC as well. Just run the same script on your linux PC and *voila!*
