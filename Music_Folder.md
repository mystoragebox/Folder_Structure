# Music Folder Structure
Like I said in the readme file, this will mostly follow the well established method of music folder structure. This Github readme is mostly to keep Musicbee renaming templates in one place and to keep important metadata fields in order. All the templates below assume you are already in the root music folder.

For example:
`C:\MUSIC\.....`

## Track File Types
My main goal with the music collection is to keep at least CD quality files. This is so that I don't have to keep ripping my CD's. Sometimes FLAC quality is impossible, in those cases I try to use 320k MP3. If you have larger file types and want to convert them eg: SACD ISO to DSF or DSF to FLAC, I have some lines of code in the scripts folder.

> [Music_Conversions](Scripts/Music_Conversions/Readme.md)

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
* Grouping `This field is used for country of origin or a special cd set`
* Track Rating
* Language
* Keywords `Can be used for anything including a flag for automatic playlists`
#### Metadata Tips
If the album is simply labeled as _Greatest Hits_ I like to put the artists name in square brackets inside of the album field as well.
* Greatest Hits[Blue Day]

With multichannel music (quadraphonic or 5.1) I like to add _[Mch]_ to the track title and _Mch_ to the genre to make sorting easier.

I use _[MyCD]_ in the album field when I made my own CD thats not in the online databases. This seperates these CD's from the collection that can use the online databases.
## CD from One Artist
This template is for cd's that come from a single artist.

* `Zminzm\Curtain Pull (2005)[flac]\01 - Intro.flac`
* `Def Tiger\COLLECTED (2005)[flac]\1-01 - Pour Some Sugar On Me.flac`
> `<Album Artist>\<Album> (<Year>)[<.Ext>]\<Disc-Track#> - <Title>`

## CD Compilation Disc
The compilation folder is anything you want it to be. For example, have a folder for movie soundtracks and another for mix CD's.

* `Soundtracks\Gone in 20 Minutes OST (2000)[flac]\01 - Painted On My Lungs.flac`
* `Various Artists\100% 90s (2008)[flac]\1-01 - Faithless - Epic.flac`
> `<Album Artist>\<Album> (<Year>)[<.Ext>]\<Disc-Track#> - <Artist> - <Title>`

## Single Tracks
You may have single tracks laying around in your storage. I found these sorting options work well.
> If you use software that scrapes metadata for your CD collection, you may want to put these files in a seperate root folder: C:\RANDOM MUSIC\.....
### Single Tracks by Decade
`1980-1989 [D05]\Ultra Group - Don't Turn Back (1984).flac`
> `<Album> [D<Disc#>]\<Artist> - <Title> (<Year>)`
### Single Tracks by Alphabet
`VA T\tinnitus D - Accolade (2001) [D06].flac`
> `<Album>\<Artist> - <Title> (<Year>) [D<Disc#>]`

## Musicbee File Organiser
I use exceptions when using the file organiser in Musicbee. I start with the root drive then change the naming template to match what I want to happen. When you add an exception take note of the order, Musicbee starts from the last exception and works up from there. These are my exceptions when used with the above templates:

C:\ `MUSIC\_CD from One Artist template_`
Album contains 'MyCD' `MUSIC VA\_CD from One Artist template_`
any of Album Artist is 'Various Artists', Album Artist is 'Soundtrack' `MUSIC\_CD Compilation Disc_`
any of Album is 'Various Artists', Album is 'Various Soundtrack' `MUSIC VA\_Single Tracks by Decade_`
