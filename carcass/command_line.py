import argparse
import os
import tempfile
import shutil
import atexit

from options import Options
from core import Core

class readable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace,self.dest,prospective_dir)
        else:
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))

def main(package_name, package_path, force=False):
    pick_list = Options().pick()
    options = [i[0] for i in pick_list]
    package_path = os.path.join(package_path, package_name)
    core = Core(package_name, package_path, force=force)
    core.create(optional_template=options)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'carcass is a Python package to generate python package scaffolding based on best practices')
    parser.add_argument('-P', '--path', action=readable_dir, default=os.path.expanduser('~'), help='Path to generate template package')
    parser.add_argument('-N', '--name', help='The package name to generate a template for')
    parser.add_argument('-F', '--force', help='Force the creation of a template package', action='store_true')

    args = parser.parse_args()
    if not args.name:
        raise Exception('Exiting because you must provide a name of your template python package.')
    main(args.name, args.path, force=args.force)