import click
import sys
from usplash_downloader.usplash import Usplash


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
@click.option(
    "-r",
    "--random-images",
    is_flag=True,
    help="download completely random images",
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
    random_images,
):
    if not any([user, collection, photo_id, keywords]):
        if not random_images:
            click.echo(click.get_current_context().get_help())
            sys.exit(1)
        else:
            click.echo(":: downloading completely random images\n")

    for i in range(limit):
        Usplash.download_photo(
            user=user,
            save_dir=output_dir,
            from_likes=from_likes,
            collection=collection,
            dimensions=dimensions,
            photo_id=photo_id,
            keywords=keywords,
        )
        click.echo(f":: {i + 1} image(s) downloaded\n")


if __name__ == "__main__":
    main()
