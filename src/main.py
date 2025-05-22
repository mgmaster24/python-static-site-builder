import os, shutil, sys
from page import generate_pages_recursive


def delete_directory_contents(dir: str):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def copy_files(src: str, dst: str):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for filename in os.listdir(src):
        src_path = os.path.join(src, filename)
        dst_path = os.path.join(dst, filename)
        print(f" * {src_path} -> {dst_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_files(src_path, dst_path)


def copy_static_files(src_dir: str, dest_dir: str):
    if not os.path.exists(src_dir):
        raise NotADirectoryError(f"source directory {src_dir} does not exist")

    delete_directory_contents(dest_dir)
    copy_files(src_dir, dest_dir)


def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    print(sys.argv)
    print(base_path)
    src = "./static"
    dst = "./docs"
    print(f"Copying files from {src} to {dst}")
    copy_static_files(src, dst)

    generate_pages_recursive(base_path, "./content", "template.html", dst)


main()
