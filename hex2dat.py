#!/usr/bin/python

#####################################################
#######            'hex2dat'               ##########
#                                                   #
# Usage: python hex2dat.py -i [infile] -o [outfile] #
#                                                   #
# Example:                                          #
# python hex2dat.py -i screenlog.0 -o flashdump.bin #
#                                                   #
#           Author: Josh Rabinowitz                 #
#####################################################

import binascii
import argparse

parser = argparse.ArgumentParser(description='Quick utility converts manual SPI flash memory dumps from hexadecimal strings to raw data for firmware analysis.')

parser.add_argument('-i','--infile',dest='infile',required=True,help='File containing serialized (hexadecimal) flash memory dump')
parser.add_argument('-o','--outfile',dest='outfile',default='out.bin',help='Converted, usable (raw data) firmware image')
args = parser.parse_args()
infile = args.infile
outfile = args.outfile

with open(infile,'r') as fp: text = fp.read()
        text = text.strip()
data = binascii.unhexlify(text)
with open(outfile,'w+') as fp2: fp2.write(data)
