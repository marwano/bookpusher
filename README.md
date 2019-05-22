# bookpusher
A robot that pushes books of shelves and high places.


![robot](https://user-images.githubusercontent.com/3801994/58211783-9929dc80-7cf5-11e9-816d-cbf1a2a7ffd9.jpg)



## Installation
 - Download and install [Raspbian Stretch with desktop](https://www.raspberrypi.org/downloads/raspbian/).
 - [Enable ssh on Raspbian](https://www.raspberrypi.org/documentation/remote-access/ssh/).
 - update system and reboot
```
$ sudo apt update
$ sudo apt upgrade
$ sudo reboot
```
 - Enable I2C
```
$ sudo raspi-config
$ # select "Interfacing Options" menu item
$ # select "I2C" menu item
$ sudo reboot
```
 - Connect and power on the Crickit board
 - Verify the Crickit i2c address 0x49 is found in the following commands output.
```
$ i2cdetect -y 1
```
 - install python packages
```
$ sudo apt install python3-virtualenv
$ python3 -m virtualenv -p python3 /home/pi/pyenv
$ source /home/pi/pyenv/bin/activate
$ pip install adafruit-circuitpython-crickit tornado
```


## Server
You can start either the bookpusher or remote tornado app with the following commands.
```
$ python -m remote.server
$ python -m bookpusher.server
```


## Teach
The teach.py module makes working with the REPL easier for kids.

```
>>> from teach import r

>>> # DC motor 1 full speed, half speed, off, reverse
>>> r.wheel = 1
>>> r.wheel = 0.5
>>> r.wheel = 0
>>> r.wheel = -1

>>> # servo set angle to 0 and 90 degrees
>>> r.arm = 0
>>> r.arm = 90

>>> # check state of capacitive touch
>>> r.touch
False
```



