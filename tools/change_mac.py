# This Tool requires katana framework
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from os import system as sysc
import random, sys, re, optparse, hashlib, re
# END LIBRARIES

class init:

    Author      = "0xicl33n"
    Description = "Changemac - change mac for interface"
    var         = {}
    Arguments   = {

        'i':[True ,'interface to change mac'],
        'm':[False,'specific mac'],
        'r':[False,'ramdom mac']
    }

def Main():

    MAC=""
    picks = ['katana','k4tan4','KAtAn4','K4TanA','K4TaNA','KATANA','ANATAK','|<474/\/A']
    a = hashlib.md5(random.choice(picks))
    b = a.hexdigest()
    as_int = int(b, 16)
    random.seed(bin(as_int)[2:])

    mac = [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

    if init.var['r'] == "enable" or init.var['m']=="null":
	MAC=':'.join(map(lambda x: "%02x" % x, mac))

    if init.var['m']!="null":
        MAC=init.var['m']

    if NET.CheckIfExistInterface(init.var['i']):
        printk.inf("Changing MAC to "+init.var['i'])
        sysc("sudo airmon-ng check kill >/dev/null 2>&1")
        sysc("sudo ifconfig "+init.var['i']+" down >/dev/null 2>&1")
        sysc("sudo ifconfig "+init.var['i']+" hw ether "+MAC+" >/dev/null 2>&1")
        sysc("sudo ifconfig "+init.var['i']+" up >/dev/null 2>&1")
        sysc("sudo service NetworkManager start >/dev/null 2>&1")
	printk.suff("MAC Address was Changed "+MAC)
        return
