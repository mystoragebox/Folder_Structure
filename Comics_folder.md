# Comic Folder Structure
This is a guide on how to organise comics in a folder structure that is easy to navigate and prioritises using a program to bring the comics together into collections. You can use seperate root folders for comics, manga, manwha etc. but if you have a small collection maybe one root folder is all you need. This guide assumes that the comics are all in one root folder:

`C:\SEQUENTIAL-ART\.....`
## Metadata
There are two methods to have metadata for comics, the first is to have a comicinfo.xml file in the same folder as the comics. The next is to have a comicinfo.xml embedded into the comic file. There are pros and cons to each method but the overview is with a commicinfo.xml in the folder you will be limited to the information for all volumes of that comic of that comic while the embedded file can hold metadata for each volume or chapter of the comic.

There are many ways to make the metadata for the comics but the best way is to find a metadata scraper on github and use that. There is a python script that I have made scraping data using anilist api that is in the scripts folder. See the script for more information.
## Files
In the world of digital comics there are two main file types that are used to store the comics, these are cbz and cbr file types. For compadability with Jellyfin this guide will use the cbz file type. Jellyfin cannot read and cannot create posters for each volume or chapter if cbr is used.
### Convert Files
If your comics are in cbr and you wish to convert them to cbz, there is a Python script here to help with that. The script unpacks and repacks the file with no quality loss to the images in the file.
## Folder Structure
Keeping the folder structure consistant is key. To help with this you can look at the metadata collectors like anilist or comics.org. These websites will dictate what comics can go altogether in one folder or if they need to be split into seperate folders. For example:

The Mad Max comics that were made for the Mad Max: Fury Road movie are all chapters from the same story and when you search on comics.org you can see one page holds all the metadata. The file structure would look like:
`Mad Max - Fury Road[Comics-1452865]\Mad Max - Fury Road Ch.01 - Nux and Immortan Joe.cbz`
`Mad Max - Fury Road[Comics-1452865]\Mad Max - Fury Road Ch.02 - Furiosa.cbz`
`....`

Conversly, if you have a multi-series comic like Men in Black you will need multiple folders because the metadata provider has seperate pages for them:
`Men in Black Far Cry[Comics-81813]\Men in Black Far Cry (1997).cbz`
`Men in Black Retribution[Comics-692003]\Men in Black Retribution (1997).cbz`

This will explain in a bit more detail the files contained in the folders.

* `Futurama[comics-15319]` Write the page number from the metadata provider here
* `Futurama[comics-15319]\folder.jpg` cover for the folder
* `Futurama[comics-15319]\ComicInfo.xml` metadata for the comic series
* `Futurama[comics-15319]\Futurama Vol.01.cbz` Vol. is short for volume
* `Futurama[comics-15319]\Futurama Vol.01-poster.jpg` Front cover of the file
* `Futurama[comics-15319]\Futurama Ch.059.cbz` Ch. is short for chapter. Use 3 digits for chapter.

