import os
import shutil
import sys
from markdown_to_html_node import markdown_to_html_node


def copy_directory(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination, filename)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied {source_path} -> {destination_path}")
        else:
            copy_directory(source_path, destination_path)


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No h1 header found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(
        f"Generating page from {from_path} "
        f"to {dest_path} using {template_path}"
    )

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    destination_directory = os.path.dirname(dest_path)

    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)


def generate_pages_recursive(
    dir_path_content,
    template_path,
    dest_dir_path,
    basepath
):
    for filename in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, filename)

        if os.path.isfile(content_path):
            if filename.endswith(".md"):
                html_filename = filename[:-3] + ".html"
                dest_path = os.path.join(dest_dir_path, html_filename)

                generate_page(
                    content_path,
                    template_path,
                    dest_path,
                    basepath
                )

        else:
            new_dest_dir = os.path.join(dest_dir_path, filename)

            os.makedirs(new_dest_dir, exist_ok=True)

            generate_pages_recursive(
                content_path,
                template_path,
                new_dest_dir,
                basepath
            )


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_directory("static", "docs")

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
    )


main()
