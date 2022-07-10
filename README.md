# Control computer volume using hand gestures

This is a simple program that uses hand gestures to control the volume of a computer. I created this repo for fun and to learn more about computer vision.

## How it works?

1. If you clap then your computer will be muted.
2. By decreasing and increasing the distance between your thumb and index fingers you can control the computer volume.

## Requirements

* A computer with a webcam
* Python 3.8+
* Install `libasound2-dev` using the followng command:
```sudo apt-get install libasound2-dev```
* Install the required packages using one of the followings:
  * `pip install requirements.txt`
  * `pipenv install`
  * `pipenv install -d` (for development/contribution)

## How to run it?

`python main.py`

## Note

* This code has been tested on a Ubuntu 20.04 LTS computer and I guess you'll need different sound packages for other operating systems. I suggest that take a look at following for:
  * [Mac](https://stackoverflow.com/a/45772468/5326238)
  * [Windows](https://techoverflow.net/2020/04/04/how-to-set-windows-audio-volume-using-python/)

## Resources

* https://www.computervision.zone/courses/gesture-volume-control/
* https://www.section.io/engineering-education/creating-a-hand-gesture-volume-controller-using-python-and-pycharm/
