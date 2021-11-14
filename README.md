# Hidden Miner Detector

This tool help you to check if your Windows machine has hidden miner.

Miners track when you open antivirus software or task manager and stop theirs work, so sometimes it's hard do detect them. 

You can check your cpu load per core or get list of running processes. If you see strange parameters, or they become lower after you open Task Manager - Most likely you have miner on you machine

## Usage
```
usage: miner_detector.py [-h] [-p] [-c]

Tool for checking cpu usage and for checking running processes

optional arguments:
  -h, --help            show this help message and exit
  -p, --show-processes  Show running processes
  -c, --show-cpu-usage  Show cpu load per thread
```

## Example output
Output is as simple as possible, maybe in the future I'll make it better

Cpu usage: `[3.1, 1.6, 1.6, 1.6, 4.7, 1.6, 18.8, 1.6, 0.0, 4.7, 3.1, 3.1, 0.0, 1.6, 6.2, 4.6]` - 16 threads, value is in percents

Processes:
```
PID     Process name                   CPU Usage
----------------------------------------------------------------------------------------------------  
0       System Idle Process            pcputimes(user=0.0, system=413050.40624999994, children_user=0.0, children_system=0.0)
4       System                         pcputimes(user=0.0, system=422.921875, children_user=0.0, children_system=0.0)
8       svchost.exe                    pcputimes(user=2.734375, system=2.765625, children_user=0.0, children_system=0.0)
188     csrss.exe                      pcputimes(user=0.359375, system=1.890625, children_user=0.0, children_system=0.0)
...
```
