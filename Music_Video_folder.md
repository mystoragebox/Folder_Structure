# Music Video Folder
The folder structure closly mimics the music folder structure. The biggest difference is there is no sub folders for albums. There are a few other points we must do before the folder structure. This guide assumes you are in the root folder for music videos:

`C:\MUSIC VIDEOS\....`

I have also included at the end how to setup the Jellyfin library for the music videos.

## Converting Files
Before we create the folder structure we need to ensure that the files are the proper type. I do this to maximise compatibility with Musicbee and Jellyfin. To find out how to quickly convert the files, se the scripts folder.
> [Music_Video_Conversions](Scripts/Music_Video_Conversions/Readme.md)
## Metadata
Mp4 files can hold a limited amount of metadata that Jellyfin can scrape. Start by adding the mp4's into software like Musicbee. In the metadata, there are four fields I like to edit:
* `Artist`
* `Album`
* `Year`
* `Genre`

Something to keep in mind is you need to exactly match the `Album` field to your CD albums if you have them. This ensures that the music videos can be linked to your music. Also if the music video has no CD album match you can add the `Artist` name to the `Album` field. I would recommend doing this for various artists folders.
## Folder structure
There are two main folder structures that can be used, artist folders and various artists folders which we will get into below but for now lets focus on the common sidecar files in each folder that software like Jellyfin can use. These sidecar files make the browsing experience better Jellyfin.

* `<Artist or Various>\logo.png` The artists logo or any logo you like in png format
* `<Artist or Various>\folder.jpg` The artists image or image you like
* `<Artist or Various>\bannar.jpg`
* `<Artist or Various>\backdrop1.jpg`

### Artist Folders
This folder struture will have the artists name as the folder name and the song title as the filename.
* Backally Boys\Nobody.mp4
* Fort Major\Forget the Name.mp4

`<Artist>\<Title><.ext>`
### Various Artist Folders
Here you can name the folder whatever you like (Soundtracks, Various etc.) and the filename will have the artist, title and year.
* Soundtracks\John Smith - St.Elmo's Water (1984).mp4
* Various Artists 2000-09\Waterfalls of Wayne - Stacy's Dad (2003).mp4

`<Foldername>\<Artist> - <Title> (<Year>)<.ext>`
## Jellyfin Library Setup
This step you will only need to do once if you use Jellyfin. The following fields are important to fill out when making a music video library, you can change any other fields you like but I found these are the minimum to get it to work.
* `Content Type` change to Music Videos
* `Prefer Embedded Titles Over Filenames` selected
* `Metadata Downloaders` unselect all
* `Automatically Refresh Metadata From the Internet` select Never
* `Metadata Savers` unselect
It's a very simple setup where you will stop internet scraping of metadata and prioritise metadata embedded in the files.
