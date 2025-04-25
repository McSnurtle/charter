#src/utils/clipboard.py
# imports
import os

import copykitten
from PIL import Image


# functions
def copy_image(filepath: str) -> bool:
    """Copies the image file at filepath to the system clipboard.

    :param filepath: str, the filepath to the image to copy.

    :return bool: bool, whether the copy was successful."""

    if os.path.exists(filepath):
        image = Image.open(filepath)
        raw = image.tobytes()
        copykitten.copy_image(raw, image.width, image.height)
        return True
    return False

# def copy_image(filepath: str) -> bool:
#     """Copies the image file at filepath to the system clipboard."""
#     if is_linux_x11():
#         return copy_x11(filepath)
#     elif is_linux_wayland():
#         return copy_wayland(filepath)
#     elif is_macos():
#         return copy_macos(filepath)
#     return False

# def copy_x11(filepath: str) -> bool:
#     """Copies the image file at filepath to the system clipboard of a DirectX 11 based system."""
#     if not shutil.which("xclip"):
#         return False

#     subprocess.run([
#         "xclip", "-selection", "clipboard", "-t", "image/png", "-i", filepath
#     ], check=True)
#     return True


# def copy_wayland(filepath: str) -> bool:
#     """Copies the image file at filepath to the system clipboard of a Wayland based system."""
#     if not os.environ.get("WAYLAND_DISPLAY"):
#         return False

#     with open(filepath, 'rb') as file:
#         subprocess.run(["wl-copy", "--type", "image/png"], stdin=file, check=True)
#         return True


# def copy_macos(filepath: str) -> bool:
#     """Copies the image file at filepath to the system clipboard of a MacOS based system."""
#     subprocess.run([
#         "osascript", "-e", f'set the clipboard to (read (POSIX file "{filepath}") as JPEG picture)'
#     ], check=True)
#     return True
