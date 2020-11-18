# usplash-downloader

command line utility to download random images from [unsplash.com](https://www.unsplash.com)


# installation

run `pip install .` after going into the root of this project

# options provided
```
Usage: usdl [OPTIONS]

  download random images from unsplash.com

Options:
  -u, --user TEXT        download images by a certain user
  -o, --output-dir TEXT  destination directory to save images in
  -l, --limit INTEGER    limit the number of images to be downloaded
                         [default: 1]

  -f, --from-likes       download images from a user's likes
  -c, --collection TEXT  download images from a collection
  -d, --dimensions TEXT  dimensions of the images to download
  -i, --photo-id TEXT    id of image to download
  -k, --keywords TEXT    space separated keywords of images to download
  -h, --help             Show this message and exit.
```
