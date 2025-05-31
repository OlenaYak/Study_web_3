from pathlib import Path
import argparse
import logging
from shutil import copyfile
from threading import Thread


""""
--sourse[-s]
--output[-o] default folder = dist
"""

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--sourse", "-s", help="Sourse folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

# print(parser.parse_args())
args = vars(parser.parse_args())
# print(args)

sourse = Path(args.get("sourse"))
output = Path(args.get("output"))

folders = []


def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder/ el.name)
            except OSError as err:
                logging.error(err)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders.append(sourse)
    grabs_folder(sourse)
    print(folders)

    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f"Можна видаляти {sourse}")



