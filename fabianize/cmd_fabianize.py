import shutil
import subprocess
from pathlib import Path

import click
import pkg_resources


@click.command()
def cmd_fabianize():

    commands = [
        #'fc-cache -f',
    ]

    src_dst = [
        ('bashrc', '~/.bashrc'),
        ('bashrc_alias', '~/.bashrc_alias'),
        ('dircolors', '~/.dircolors'),
        ('fonts', '~/.fonts'),
        ('Xresources', '~/.Xresources'),
        ('vimrc', '~/.vimrc'),
        ('vim', '~/.vim'),
        ('geany.conf', '~/.config/geany/geany.conf'),
        ('geany_colorschemes', '~/.config/geany/colorschemes'),
    ]

    for src,dst in src_dst:

        src_filename = Path(pkg_resources.resource_filename('fabianize', f'files/{src}'))
        dst_filename = Path(dst).expanduser()

        click.echo(f'{src_filename} -> {dst_filename}')

        dst_filename.parent.mkdir(exist_ok=True, parents=True)

        if src_filename.is_file():
            shutil.copy2(src_filename, dst_filename, follow_symlinks=True)
            continue

        shutil.rmtree(dst_filename, ignore_errors=True)
        shutil.copytree(src_filename, dst_filename)

    for command in commands:
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            print(out.decode())
        if err:
            print(err.decode())



if __name__ == '__main__':
    cmd_fabianize()
