from arguments import args
from cpu_usage import print_cpu_usage
from scan_processes import show_running_processes


def main():
    if args.show_processes:
        show_running_processes()
    if args.show_cpu_usage:
        print_cpu_usage()
    return


if __name__ == '__main__':
    main()
