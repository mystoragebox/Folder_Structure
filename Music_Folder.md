# Music Folder Structure
Like I said in the readme file, this will mostly follow the well established method of music folder structure. This Github readme is mostly to keep Musicbee renaming templates in one place and to keep important metadata fields in order. All the templates below assume you are already in the root music folder.

For example:
`C:\MUSIC\.....`

## Track File Types
My main goal with the music collection is to keep at least CD quality files. This is so that I don't have to keep ripping my CD's. Sometimes that is impossible but most of the collection is in FLAC with the rest being MP3. If you have larger file types and want to convert them eg: DSF to FLAC, I have some lines of code in the scripts folder.

## Metadata
The metadata embedded into the music file is important. Here is a list of useful metadata fields. Most of these fields need no explanation but I have provided explanation where appropriate.

* Track Title
* Artist
* Album Artist `This has the folder name ie: Hilltop Hats, Soundtracks etc. This is so you can sort by album-artist in your software of choice.`
* Album
* Year
* Track `track number`
* Disc `disc number, if one disc leave empty`
* Genre
* Grouping `This field is used for country of origin`
* Track Rating
* Language
* Keywords `Can be used for anything including a flag for automatic playlists`
## Images
These are the most useful images and the naming convention for them. This mostly follows the recommendations from Jellyfin because that's a good service for streaming around the home.
* logo.png
* backdrop.jpg
* backdrop1.jpg
* banner.jpg
* folder.jpg `Artist photo`
* folder.jpg `Album cover`

To give an example:
* `Limp Donutz\Still Great (2021)[flac]\`folder.jpg `Album cover`
* `Limp Donutz\`backdrop.jpg
* `Limp Donutz\`backdrop1.jpg
* `Limp Donutz\`banner.jpg
* `Limp Donutz\`folder.jpg `Artist photo`
* `Limp Donutz\`logo.png
## Single CD Album from One Artist
This template is for cd's that come from a single artist.

* `Zminzm\Curtain Pull (2005)[flac]\01 - Intro.flac`
* `Dream Cinema\Greatest Hit (2008)[flac]\01 - Pull Me Under (2007 Remix).flac`
> `<Artist>\<Album> (<Year>)[<.Ext>]\<Track#> - <Title>`
### Multiple CD Albums from One Artist
* `Massive Repel\COLLECTED (2006)[flac]\1-01 - SAFE FROM HARM.flac`
* `Def Tiger\COLLECTED (2005)[flac]\1-01 - Pour Some Sugar On Me.flac`
> `<Artist>\<Album> (<Year>)[<.Ext>]\<Disc-Track#> - <Title>`
## Single CD Compilation Disc
The compilation folder is anything you want it to be. For example, have a folder for movie soundtracks and another for mix CD's.

* `Soundtracks\Gone in 20 Minutes OST (2000)[flac]\01 - Painted On My Lungs.flac`
* `Various Artists\LATER The Hits Of Spring (2009)[flac]\01 - David Clooney - When Love Takes Over.flac`
> `<compilation folder>\<Album> (<Year>)[<.Ext>]\<Track> - <Artist> - <Title>`
### Multiple CD Compilation Disc
* `Soundtracks\The Best TV Album In The World Ever (2008)[flac]\1-01 - Goo Gaa Plushie - Iris.flac`
* `Various Artists\100% 90s (2008)[flac]\1-01 - Faithless - Epic.flac`
> `<compilation folder>\<Album> (<Year>)[<.Ext>]\<Disc-Track#> - <Artist> - <Title>`
## Single Tracks
You may have single tracks laying around in your storage. You can choose between two kinds of sorting. `[Mixed]` in this context shows that there are different types of music files; flac, mp3 etc.
> If you use software that scrapes metadata for your CD collection, you may want to put these files in a seperate root folder: C:\RANDOM MUSIC\.....
### Single Tracks by Decade
`Various Artists\1980-1989[Mixed]\Ultra Group - Don't Turn Back.flac`
> `<compilation folder>\<Decade>[<.Ext>]\<Artist> - <Title>`
### Single Tracks by Alphabet
`Various Artists\T[Mixed]\tinnitus D - Accolade (2001).flac`
> `<compilation folder>\<Letter>[<.Ext>]\<Artist> - <Title> (<Year>)`
