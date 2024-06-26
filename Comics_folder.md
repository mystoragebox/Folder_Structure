# Comic Folder Structure
This is a guide on how to organise comics in a folder structure that is easy to navigate and prioritises using a program to bring the comics together into collections. You can use seperate root folders for comics, manga, manwha etc. but if you have a small collection maybe one root folder is all you need. This guide assumes that the comics are all in one root folder:

`C:\SEQUENTIAL-ART\.....`
## Metadata
There are two methods to have metadata for comics, the first is to have a comicinfo.xml file in the same folder as the comic files. The next is to have a comicinfo.xml embedded into the comic file. There are pros and cons to each method but the overview is with a commicinfo.xml in the folder you will be limited to the information of the comic series while the embedded file can hold metadata for each volume or chapter of the comic.

There are many ways to make the metadata for the comics but the best way is to find a metadata scraper on github and use that. 
## Files
In the world of digital comics there are two main file types that are used to store the comic images, these are cbz and cbr file types. For compatibility with Jellyfin this guide will use the cbz file type. Jellyfin cannot read and cannot create posters for each volume or chapter if cbr is used.
### Convert Files
If your comics are in cbr and you wish to convert them to cbz, there is a Python script here to help with that. The script unpacks and repacks the file with no quality loss to the images in the file.
> [CBR_to_CBZ](Scripts/CBR_to_CBZ/start.py)
## Folder Structure
Keeping the folder structure consistant is key. Using metadata collectors like anilist or comics.org lets us decide what folders we need. These websites will dictate what comics can go altogether in one folder or if they need to be split into seperate folders. For example:

The Mad Mick comics that were made for the Mad Mick: Fury Street movie are all chapters from the same story and when you search on comics.org you can see one page holds all the metadata. The file structure would look like:

* `Mad Mick - Fury Street\Mad Mick - Fury Street Ch.01 - Nux and Immortan Joe.cbz`
* `Mad Mick - Fury Street\Mad Mick - Fury Street Ch.02 - Furiosa.cbz`
* `....`

Conversly, if you have a multi-series comic like Men in Blue you will need multiple folders because the metadata provider has seperate pages for them:

* `Men in Blue Long Cry\Men in Blue Long Cry (1997).cbz`
* `Men in Blue Punishment\Men in Blue Punishment (1997).cbz`

This will explain in a bit more detail the files contained in the folders.

* `Pasturama` Write the page number from the metadata provider here
* `Pasturama\folder.jpg` cover for the folder
* `Pasturama\ComicInfo.xml` metadata for the comic series
* `Pasturama\Pasturama Vol.01.cbz` Vol. is short for volume
* `Pasturama\Pasturama Vol.01-poster.jpg` Front cover of the file
* `Pasturama\Pasturama Ch.059.cbz` Ch. is short for chapter. Use 3 digits for chapter.

