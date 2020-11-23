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
@click.option("-v", "--verbose", is_flag=True, help="set verbose mode")
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
    verbose,
):
    if not any([user, collection, photo_id, keywords]):
        if not random_images:
            click.echo(click.get_current_context().get_help())
            sys.exit(1)
        else:
            click.secho(":: downloading completely random images\n", bold=True)

    downloaded_images = 0

    for i in range(limit):
        success = Usplash.download_photo(
            user=user,
            save_dir=output_dir,
            from_likes=from_likes,
            collection=collection,
            dimensions=dimensions,
            photo_id=photo_id,
            keywords=keywords,
            verbose=verbose,
        )

        if success:
            downloaded_images += 1
        click.secho(f":: {downloaded_images} image(s) downloaded\n", fg="green", bold=True)

    click.secho("...download complete.", fg="bright_cyan", bold=True)


if __name__ == "__main__":
    main()
