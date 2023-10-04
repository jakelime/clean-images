from pathlib import Path


class PathFinder:
    def __init__(self, resources_name: str = "resources"):
        self.cwd = Path(__file__).parent.parent
        self.resources_path = self.get_resources()

    def get_resources(self, name: str = "resources") -> Path:
        path = self.cwd / name
        if not path.is_dir():
            raise NotADirectoryError(f"{path=}")
        return path

    def get_image_files(self, file_ext: str = ".png", exclude_kw: str = ""):
        if exclude_kw:
            imgs = [
                fp
                for fp in self.resources_path.rglob(f"*{file_ext}")
                if exclude_kw not in fp.stem
            ]
        else:
            imgs = [fp for fp in self.resources_path.rglob(f"*{file_ext}")]

        if not imgs:
            raise FileNotFoundError(f"no files found {file_ext=}")
        return imgs

    def generate_output_dir(self, name: str = "output"):
        output_dir = self.resources_path / name
        if not output_dir.is_dir():
            output_dir.mkdir()
        return output_dir


def main():
    fm = PathFinder()
    imgs = fm.get_image_files(".png")
    [print(x) for x in imgs]


if __name__ == "__main__":
    main()
