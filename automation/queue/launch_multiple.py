import argparse
import os.path
import sys
from subprocess import Popen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--makedirs', dest='makedirs',
        help='enable ConfigLauncher to create missing directories',
        action='store_true'
    )
    parser.set_defaults(makedirs=False)
    parser.add_argument('--basepath', type=str, help='base path to use for ConfigLauncher', required=True)
    parser.add_argument('--num-launchers', type=int, required=True, help='number of launcher processes to run')
    args = vars(parser.parse_args())

    path_to_launcher = os.path.join(os.path.dirname(__file__), 'run_launcher.py')
    base_path = args['basepath']
    command = [sys.executable, path_to_launcher, '--basepath', base_path]
    if args['makedirs']:
        command.append(' --makedirs')

    num_launchers = args['num_launchers']

    processes = [Popen(command) for _ in range(num_launchers)]

    for p in processes:
        p.wait()


if __name__ == '__main__':
    main()
