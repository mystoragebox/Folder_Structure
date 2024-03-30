# Music Conversions
Here I have a few lines of code used in Windows command line. These are for converting higher quality music into filetypes that are either smaller in size or easier to handle.

## SACD ISO to DSF
This line of code will create DSF tracks from all the SACD ISO's in a given folder. Run command from the same folder that you have your ISO's and be sure the exe program is in that same folder.

2 channel
> for /R %f in (*.iso) DO "sacd_extract.exe" -P -C -s -2 -i "%f"

Multi channel
> for /R %f in (*.iso) DO "sacd_extract.exe" -P -C -s -m -i "%f"

This is the exe you need to extract the tracks from the ISO file.

> [sacd_extract.exe](http://sacd-ripper.github.io/)

## DFF to DSF
This is a simple script to convert DFF files to DSF. It uses a fork of SOX originally posted by [Mansa](https://github.com/mansr/sox), here is the forum [post](https://audiophilestyle.com/forums/topic/24911-dsd-encoding-with-sox/) if you would like to read about it. I used the exe file from [turbulentie](https://github.com/turbulentie/sox-dsd-win/blob/main/README.md) on github.

I'm not sure if it changes the quality of the file, there are many settings you can use in SOX, this is simply to batch encode DSF files from DFF.
> for /R %f in (*.dff) DO "x86_64-w64-mingw32-sox.exe" -e floating-point "%f" "%~nf.dsf"

## DSF to FLAC

If you can't use DSF files you can convert them using this line of code. I like to convert them to higher than CD quality but if you need to save space you can change 's32' to 's16' for 16 bit, lowpass to '22000' and change '88200' to '44100' for the sample rate. Make sure FFMPEG is installed on your system. Run command from the folder with all your DSF files you want to convert.

Some DSF files may have a low volume, in this case you can change the volume variable to 6dB or 3dB. This will be a bit of trial and error to get right.

> for /R %f IN (*.dsf) DO ffmpeg -i "%f" -af "lowpass=40000, volume=0dB" -sample_fmt s32 -ar 88200 "%~nf.flac"
