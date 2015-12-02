import boto
import urllib2


response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
keys = response.read().split(':')

print boto.Version
print keys[0]
print keys[1]

