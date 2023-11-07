# hex2dat
Quick utility converts manual SPI flash memory dumps from hexadecimal strings to raw data for firmware analysis.  
Developed for use with DIY flash chip readers (*see https://github.com/jrabinowitz2/DIY-Flash-Reader-SOIC16*)

## Usage
```
usage: hex2dat.py [-h] -i INFILE [-o OUTFILE]

Quick utility converts manual SPI flash memory dumps from hexadecimal strings to raw data for firmware analysis.

optional arguments:
  -h, --help            show this help message and exit
  -i, --infile INFILE
                        File containing serialized (hexadecimal) flash memory dump
  -o, --outfile OUTFILE
                        Converted, usable (raw data) firmware image (default is out.bin)
```

## Example
Input: logged serial output from "bit-banged" SPI flash dump
![Screen Shot 2023-11-07 at 5 03 10 PM](https://github.com/jrabinowitz2/hex2dat/assets/45504513/05ce7644-915a-427f-bbf2-a062b72b35bc)

Output: binary image ready for firmware extraction & analysis  
![Screen Shot 2023-11-07 at 5 04 21 PM](https://github.com/jrabinowitz2/hex2dat/assets/45504513/a5b329c5-4511-4986-97fd-6c05722a7690)

