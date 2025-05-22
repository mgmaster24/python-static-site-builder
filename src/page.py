import os
import pathlib
from markdown import markdown_to_htmlnode


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]

    raise ValueError("no title found")


def generate_page(base_path, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        md_contents = f.read()
    with open(template_path) as f:
        template_contents = f.read()

    htmlnode_from_markdown = markdown_to_htmlnode(md_contents)
    title = extract_title(md_contents)
    print(base_path)
    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace(
        "{{ Content }}", htmlnode_from_markdown.to_html()
    )
    template_contents = template_contents.replace('href="/', f'href="{base_path}')
    template_contents = template_contents.replace('src="/', f'src="{base_path}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template_contents)


def generate_pages_recursive(base_path, dir_path_content, template_path, dest_dir_path):
    print(base_path)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, filename)
        dst_path = os.path.join(dest_dir_path, filename)
        print(f" * {src_path} -> {dst_path}")
        if os.path.isfile(src_path):
            dst_path = pathlib.Path(dst_path).with_suffix(".html")

            generate_page(base_path, src_path, template_path, dst_path)
        else:
            generate_pages_recursive(base_path, src_path, template_path, dst_path)
