import pathlib
import zipfile


def make_archive(filepaths, destination):
    dest_path = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            path = pathlib.Path(filepath)
            archive.write(filepath, arcname=path.name)


if __name__ == "__main__":
    make_archive(filepaths=["/files/averages.py", "/files/bonus16.py"], destination="/files")
