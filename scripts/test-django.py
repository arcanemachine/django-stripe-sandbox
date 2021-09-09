#!/usr/bin/python3

# NOT WORKING DUE TO ISSUES USING PIPES IN PYTHON SCRIPTS
# stackoverflow.com/questions/13332268/how-to-use-subprocess-command-with-pipes

import argparse
import os
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument(
    '--echo',
    '-e',
    action="store_true",
    help="Echoes the command(s) to the bash console as they are run")
parser.add_argument(
    '--echo',
    '-e',
    action="store_true",
    help="Echoes the command(s) to the bash console as they are run")
parser.add_argument(
    '--keepdb',
    '-k',
    action="store_true",
    help="Do not recreate database when running tests")
args_in = parser.parse_args()


def main():
    # directory
    directory = os.environ.get('DJANGO_BASE_DIR')
    if not directory:
        directory = '/home/serv/code/django/django-stripe-sandbox'
        print("\nDJANGO_BASE_DIR not present in environment variables."
              "\nUsing f'{directory}'...")

    # output args
    args_out = ""
    if args_in.keepdb:
        args_out += '--keepdb '
        print("\n-k: Preserving the database between test runs...")

    bash_command = f"python3 {directory}/manage.py test {args_out}"

    if args_in.watch:
        module = args_in.module.split('.')[0]
        file = args_in.watch.split('.')[1]
        files = f"find {directory}/{module} -name {file}.py"
        bash_command =\
            f"{cmd} entr python3 {directory}/manage.py test {args_out}"
        print("\nWatching test files for changes...")
    elif args_in.module:
        bash_command =\
            f"python3 {directory}/manage.py test {args_in.module} {args_out}"
        print(f"\nTesting module '{args_in.module}'...")

    if args_in.echo:
        print(f"\n{bash_command}\n")

    try:
        res = subprocess.check_output(bash_command.split())
    except subprocess.CalledProcessError:
        print("\nThe command could not be executed. "
              "Are you in the right directory?\n")
        return False

    for line in res.splitlines():
        print(line)


if __name__ == "__main__":
    main()
