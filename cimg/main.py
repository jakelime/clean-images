from pathlib import Path
from utils import PathFinder
from PIL import Image
import uuid


class ImageCleaner:
    def __init__(self, input_images: list, output_dir: Path):
        if not input_images:
            raise RuntimeError("No input images")
        self.input_images = input_images
        if not output_dir.is_dir():
            raise NotADirectoryError(f"{output_dir=}")
        self.output_dir = output_dir

    def run(
        self, generate_random_id: bool = False, cropbox: tuple = (11, 81, 422, 477)
    ):
        for fp in self.input_images:
            if generate_random_id:
                random_id = str(uuid.uuid4())
                random_id = random_id[-12:]
                new_fp = self.output_dir / f"{random_id}{fp.suffix}"
            else:
                new_fp = self.output_dir / f"{fp.name}"
            with Image.open(fp) as img:
                img = self.crop_image(img, cropbox)
                # img.show()
                img.save(new_fp)
                print(f"cropped and saved to //{new_fp.parent.name}/{new_fp.name}")

    def crop_image(self, img: Image.Image, cropbox: tuple) -> Image.Image:
        img = img.crop(cropbox)  # type: ignore
        return img

    def print_image_details(self, img: Image.Image):
        print(f"  {img.format=}")
        print(f"  {img.size=}")
        print(f"  {img.mode=}")


def main():
    fm = PathFinder()
    imgs = fm.get_image_files(file_ext=".png", exclude_kw="output")
    output_dir = fm.generate_output_dir("output_cleaned_images")
    icc = ImageCleaner(imgs, output_dir)
    icc.run(generate_random_id=True, cropbox=(11, 81, 422, 477))


if __name__ == "__main__":
    main()
