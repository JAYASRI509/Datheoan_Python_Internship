import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

categories = {
    "Documents": [".pdf", ".docx", ".txt", ".doc"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".java", ".c", ".cpp", ".html"],
    "Audio": [".mp3", ".wav"]
}


def get_category(extension):
    for folder, extensions in categories.items():
        if extension.lower() in extensions:
            return folder
    return "Others"


def get_unique_path(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            destination.stem + "_" +
            str(counter) + destination.suffix
        )

        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):

    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        logging.error("Invalid folder path!")
        return

    moved = 0
    failed = 0

    for file in list(folder.iterdir()):

        if not file.is_file():
            continue

        if file.resolve() == Path(__file__).resolve():
            continue

        category = get_category(file.suffix)

        try:
            target_folder = folder / category
            target_folder.mkdir(exist_ok=True)

            destination = get_unique_path(
                target_folder / file.name
            )

            shutil.move(str(file), str(destination))

            logging.info(
                f"Moved {file.name} to {category}"
            )

            moved += 1

        except PermissionError:
            logging.error(f"Permission denied: {file.name}")
            failed += 1

        except OSError as error:
            logging.error(f"Could not move {file.name}: {error}")
            failed += 1

    print("\n===== ORGANIZATION SUMMARY =====")
    print("Total files moved:", moved)
    print("Failed operations:", failed)
    print("Organization completed!")


print("AUTOMATED FILE ORGANIZER")
print("------------------------")

path = input("Enter folder path to organize: ")

organize_files(path)