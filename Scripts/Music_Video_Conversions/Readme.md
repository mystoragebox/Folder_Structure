# Music Video Conversions
I have a quick and easy way to convert videos to mp4. This is really useful for converting many music videos to a format that can hold metadata from Musicbee and be read by Jellyfin. These commands are for Windows only. For this you need ffmpeg installed and command line open. Converting to mp4 will give us access to the metadata fields in Musicbee that can be used in Jellyfin. Navigate to the folder with the videos inside then type in the address bar **cmd** to bring up command. Copy and past one of the lines below to convert all files in the folder.


Convert to mp4 with no conversion of video or audio (change mkv to mp4). If your file is not mkv you can change the code to suit.

`for /R %f IN (*.mkv) DO ffmpeg -i "%f" -c copy "%~nf.mp4"`

Sometimes you will encounter an error that a file couldn't be coverted, the main reason this occours is because the audio cannot be contained in the mp4 container. The solution is to convert the audio to a known audio codec for mp4 and try to keep the video codec the same. The code below will convert the audio for you.

`for /R %f IN (*.mkv) DO ffmpeg -i "%f" -acodec aac_coder -q -vcodec copy "%~nf.mp4"`

If the video codec cannot be contained in mp4, Ffmpeg will automatically convert it for you. You can use Handbrake if you want more fine controls over the output however, this works fine in most cases.
