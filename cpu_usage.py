import psutil


def print_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        print(str(cpu_usage).ljust(100, ' '), end='\r')
