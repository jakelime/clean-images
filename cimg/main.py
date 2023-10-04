from pathlib import Path
from utils import PathFinder
from PIL import Image


class ImageCleaner:
    def __init__(self, input_images: list, output_dir: Path):
        if not input_images:
            raise RuntimeError("No input images")
        self.input_images = input_images
        if not output_dir.is_dir():
            raise NotADirectoryError(f"{output_dir=}")
        self.output_dir = output_dir

    def run(self):
        for fp in self.input_images:
            new_fp = self.output_dir / f"{fp.name}"
            with Image.open(fp) as img:
                img = self.crop_image(img)
                # img.show()
                img.save(new_fp)
                print(f"cropped and saved to //{new_fp.parent.name}/{new_fp.name}")


    def crop_image(
        self, img: Image.Image, cropbox: tuple = (11, 81, 422, 477)
    ) -> Image.Image:
        img = img.crop(cropbox)  # type: ignore
        return img

    def display_image(self, fp: Path):
        with Image.open(fp) as img:
            print(type(img))
            print(f"{fp.name}")
            img.load()
            # img.show()
            self.print_image_details(img)

            img = img.crop((11, 81, 422, 477))
            self.print_image_details(img)
            img.show()

    def print_image_details(self, img: Image.Image):
        print(f"  {img.format=}")
        print(f"  {img.size=}")
        print(f"  {img.mode=}")


def main():
    fm = PathFinder()
    imgs = fm.get_image_files(".png", exclude_kw="output")
    output_dir = fm.generate_output_dir("cleaned_images")
    icc = ImageCleaner(imgs, output_dir)
    icc.run()


if __name__ == "__main__":
    main()
