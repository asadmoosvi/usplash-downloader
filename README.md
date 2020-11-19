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
  -r, --random-images    download completely random images
  -h, --help             Show this message and exit.
```

# usage

## download images by a user

```
# download an image by user named unsplash
$ usdl -u unsplash

# download 10 images by a user named unsplash
$ usdl -u unsplash -l 10

# download 10 images from a user's likes
$ usdl -u unsplash -l 10 --from-likes

# download images from a user named unsplash and save it in a directory with the same name
$ usdl -u unsplash -l 10 -o unsplash
```


## download images based on keywords

```
# download images with the the following keywords: sunset beach wallpapers
$ usdl -k 'sunset beach wallpapers' -o wallpapers -l 5
```


## download images with a certain dimension
```
# download science and tech images with a dimension of 1920x1080
$ usdl -k 'science tech' -d '1920x1080' -l 20 -o science-tech
```


## download completely random images
`$ usdl -r -l 25 -o random-images`
