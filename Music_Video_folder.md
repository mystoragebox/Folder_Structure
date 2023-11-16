# Music Video Folder
The folder structure closly mimics the music folder structure. The biggest difference is there is no sub folders for albums. There are a few other points we must do before the folder structure. This guide assumes you are in the root folder for music videos:

`C:\MUSIC VIDEOS\....`

## Converting Files
Before we create the folder structure we need to ensure that the files are the proper type. I do this to maximise compatibility with Musicbee and Jellyfin. This next part is for Windows only. For this you need ffmpeg installed and command line open. Navigate to the folder with the videos inside then type in the address bar **cmd** to bring up command. Copy and past the one of the lines below to convert all files in the folder.

Convert to mp4 with no conversion of video or audio (change mkv to the files extension)

`for /R %f IN (*.mkv) DO ffmpeg -i "%f" -c copy "%~nf.mp4"`

That piece of code will not convert audio, to convert audio if you get an error use this (change mkv to the files extension)

`for /R %f IN (*.mkv) DO ffmpeg -i "%f" -acodec aac_coder -q -vcodec copy "%~nf.mp4"`
