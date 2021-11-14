import argparse

parser = argparse.ArgumentParser(description='Tool for checking cpu usage and for checking running processes')

parser.add_argument('-p', '--show-processes', action='store_const', const=True, default=False,
                    help='Show running processes')

parser.add_argument('-c', '--show-cpu-usage', action='store_const', const=True, default=False,
                    help='Show cpu load per thread')


args = parser.parse_args()
