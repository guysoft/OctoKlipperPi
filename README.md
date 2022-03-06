# OctoKlipperPi
![image](https://raw.githubusercontent.com/guysoft/OctoKlipperPi/main/media/OctoKlipperPi.png)

*The latest OctoPi release with the latest Klipper already included*

A [Raspberry Pi](http://www.raspberrypi.org/) distribution for 3d printers. It includes the [OctoPrint](http://octoprint.org) host software for 3d printers and [Klipper](https://github.com/KevinOConnor/klipper/) firmware service, out of the box and [mjpg-streamer with RaspiCam support](https://github.com/jacksonliam/mjpg-streamer) for live viewing of prints and timelapse video creation.

This repository contains the source script to generate the distribution out of an existing [OctoPi](https://github.com/guysoft/OctoPi/) distro image.

# Where to get it?

Official mirror is [here](https://github.com/guysoft/OctoKlipperPi/releases)

Nightly builds are available [here](https://github.com/guysoft/OctoKlipperPi/actions/workflows/build.yml)

## How to use it?

1. Unzip the image and install it to an sd card `like any other Raspberry Pi image <https://www.raspberrypi.org/documentation/installation/installing-images/README.md>`_
2. Configure your WiFi by editing ``octopi-wpa-supplicant.txt`` on the root of the flashed card when using it like a thumb drive
3. Boot the Pi from the card
4. Log into your Pi via SSH (it is located at ``octopi.local`` `if your computer supports bonjour <https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview>`_ or the IP address assigned by your router), default username is "pi", default password is "raspberry". Run ``sudo raspi-config``. Once that is open:

    1. Change the password via "Change User Password"
    2. Optionally: Change the configured timezone via "Localization Options" > "Timezone".
    3. Optionally: Change the hostname via "Network Options" > "Hostname". Your OctoKlipperPi instance will then no longer be reachable under ``octopi.local`` but rather the hostname you chose postfixed with ``.local``, so keep that in mind.
  
   You can navigate in the menus using the arrow keys and Enter. To switch to selecting the buttons at the bottom use Tab.
   
   You do not need to expand the filesystem, current versions of OctoKlipperPi do this automatically.

OctoPrint is located at `http://octopi.local <http://octopi.local>`_ and also at `https://octopi.local <https://octopi.local>`_. Since the SSL certificate is self signed (and generated upon first boot), you will get a certificate warning at the latter location, please ignore it.

To install plugins from the commandline instead of OctoPrint's built-in plugin manager, :code:`pip` may be found at :code:`/home/pi/oprint/bin/pip`.  Thus, an example install cmd may be:  :code:`/home/pi/oprint/bin/pip install <plugin-uri>`

If a USB webcam or the Raspberry Pi camera is detected, MJPG-streamer will be started automatically as webcam server. OctoPrint on OctoPi ships with correctly configured stream and snapshot URLs pointing at it. If necessary, you can reach it under `http://octopi.local/webcam/?action=stream <http://octopi.local/webcam/?action=stream>`_ and SSL respectively, or directly on its configured port 8080: `http://octopi.local:8080/?action=stream <octopi.local:8080/?action=stream>`_.

# Features

* [OctoPrint](http://octoprint.org) host software for 3d printers out of the box. Settings pre-set for klipper.
* [Klipper](https://github.com/KevinOConnor/klipper/) host firmware for 3d printers out of the box
* [OctoKlipper plugin](https://plugins.octoprint.org/plugins/klipper/) to get OctoPrint to work better with Klipper.
* [Raspbian](http://www.raspbian.org/) tweaked for maximum performance for printing out of the box
* [mjpg-streamer with RaspiCam support](https://github.com/jacksonliam/mjpg-streamer) for live viewing of prints and timelapse video creation.


# Developing

## What is this repo doing?

This repository automatically adds klipper installation on the latest OctoPi image
and provides the resulting image ready to flash. Checkout the [releases](https://github.com/guysoft/OctoKlipperPi-CustoPiZer/releases).

## How does this work?

A simple update script is run via [CustoPiZer](https://github.com/OctoPrint/CustoPiZer).

## Can I do something like this as well?

Sure, check out [CustoPiZer's README](https://github.com/OctoPrint/CustoPiZer) for 
instructions on how to set up your own image build for modified but clean OctoPi images!

## I have a problem where can I get help?

If you need support with OctoPrint or OctoPi, [please get in touch on the OctoPrint Community Forums](https://community.octoprint.org).
If you have a bug specific to OctoKlipperPi use the issue tracker
