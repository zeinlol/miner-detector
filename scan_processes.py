import psutil


def show_running_processes():
    cpu_count = psutil.cpu_count()
    processes_info = []
    table_info = f"{'PID'.ljust(7, ' ')} {'Process name'.ljust(30, ' ')} CPU Usage\n{'-'*100}"
    print(table_info)
    # while True:
    for proc in psutil.process_iter():
        try:
            process = proc.as_dict(attrs=['pid', 'cpu_percent', 'name'])
            current_process = psutil.Process(pid=process['pid'])
            process["cpu_percent"] = current_process.cpu_times()
            processes_info.append(process)
        except psutil.NoSuchProcess:
            pass
    output = ''.join(
        f"{str(each['pid']).ljust(7, ' ')} {each['name'].ljust(30, ' ')} {each['cpu_percent']}\n"
        for each in processes_info
    )
    print(output)
