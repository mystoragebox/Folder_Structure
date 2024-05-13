# Ffmpeg Hints
This is where I keep all my command line hints for Ffmpeg that don't fit in the other categories.

## View All Data in a Video File
This is to check the metadata and streams of a video file.

* `ffmpeg -i "Video_file.mkv"`

## Removing Streams from the Video File
Sometimes to save space you may want to remove audio streams that are dubbs for a language you don't understand. Use the view all data command first and keep a note of which streams you want to keep. Then use the -map function in Ffmpeg to copy the streams to a new file.

* `ffmpeg -i "Old_Video.mkv" -map 0:0 -map 0:3 -map 0:6 -map 0:7 "New_Video.mkv"`

If you get an error from converting subtitles you can copy them over using the copy function:

* `ffmpeg -i "Old_Video.mkv" -map 0:0 -map 0:3 -map 0:6 -c:s copy -map 0:7 -c:s copy "New_Video.mkv"`

Finally if you don't want to reencode the video or audio you can use the copy function for them as well:

* `ffmpeg -i "Old_Video.mkv" -map 0:0 -map 0:3 -map 0:6 -c:s copy -map 0:7 -c:s copy -c:v copy -c:a copy "New_Video.mkv"`
