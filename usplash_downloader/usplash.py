import requests
import os
import sys
from typing import Optional


def message(msg: str, die: bool = False) -> None:
    stream = sys.stderr if die else sys.stdout
    print(f"===> {msg}", file=stream)
    if die:
        sys.exit(1)


def download_photo(
    user: Optional[str] = None,
    from_likes: bool = False,
    collection: Optional[str] = None,
    dimensions: Optional[str] = None,
    photo_id: Optional[str] = None,
    keywords: Optional[str] = None,
    save_dir: Optional[str] = None,
    verbose: bool = False,
) -> bool:
    url = "https://source.unsplash.com/random"
    if user:
        url = os.path.dirname(url) + f"/user/{user}"
        if from_likes:
            url += "/likes"
    elif collection:
        url = os.path.dirname(url) + f"/collection/{collection}"
    elif photo_id:
        url = os.path.dirname(url) + f"/{photo_id}"

    if dimensions:
        url += f"/{dimensions}"

    url += "/sig=123"
    if keywords:
        url = url + "?" + ",".join(keywords.split())

    while True:
        message(f"downloading image from url `{url}`")

        response = requests.get(url)
        response.raise_for_status()
        redirect_url = response.history[0].headers["Location"]

        if verbose:
            message(f"redirected to url: `{redirect_url}`")

        redirect_basename = os.path.basename(redirect_url)
        img_filename = redirect_basename[0:redirect_basename.find("?")]
        if img_filename == "source-404":
            message("404: no image found")
            return False

        img_ext = response.headers["Content-Type"].split("/")[-1]

        if save_dir:
            if not os.path.isdir(save_dir):
                os.mkdir(save_dir)
            filename = os.path.join(save_dir, img_filename + "." + img_ext)
        else:
            filename = img_filename + "." + img_ext

        if not os.path.exists(filename):
            break
        else:
            message(
                f"file `{filename}` already downloaded,"
                " retrying next random image..."
            )

    message(f"Saving to file `{filename}`")
    with open(filename, "wb") as out_file:
        for chunk in response.iter_content(1024):
            if chunk:
                out_file.write(chunk)

    return True
