import click
from usplash import download_photo


@click.command(help="download random images from unsplash.com")
@click.option("-u", "--user", help="download images by a certain user")
@click.option(
    "-o", "--output-dir", help="destination directory to save images in"
)
@click.option(
    "-l",
    "--limit",
    help="limit the number of images to be downloaded",
    default=1,
    show_default=True,
)
@click.option(
    "-f",
    "--from-likes",
    is_flag=True,
    help="download images from a user's likes",
)
@click.option("-c", "--collection", help="download images from a collection")
@click.option(
    "-d", "--dimensions", help="dimensions of the images to download"
)
@click.option("-i", "--photo-id", help="id of image to download")
@click.option(
    "-k", "--keywords", help="space separated keywords of images to download"
)
@click.help_option("-h", "--help")
def main(
    user,
    output_dir,
    limit,
    from_likes,
    collection,
    dimensions,
    photo_id,
    keywords,
):
    for i in range(limit):
        download_photo(
            user=user,
            save_dir=output_dir,
            from_likes=from_likes,
            collection=collection,
            dimensions=dimensions,
            photo_id=photo_id,
            keywords=keywords,
        )
        click.echo()


if __name__ == "__main__":
    main()
