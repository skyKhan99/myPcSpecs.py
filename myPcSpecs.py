import os
from tkinter import *
from tkinter import ttk
import platform
import psutil

def byteToGb(x):
    #x/=8 #byte
    x/=1024 #kb
    x/=1024 #mb
    x/=1024 #gb
    return x

machine_type = platform.machine()
network_type = platform.node()
operating_system = platform.system()
os_version = platform.platform()

# cpu infos
processor = platform.processor()
physical_cores = psutil.cpu_count(logical=False)
total_cores = psutil.cpu_count(logical=True)
cpu_max_speed = psutil.cpu_freq().max
cpu_min_speed = psutil.cpu_freq().min

# memory infos
svmem = psutil.virtual_memory()
ram_total = svmem.total

#disk infos
partitions = psutil.disk_partitions()
partition_infos = {}
for partition in partitions:
    i = 0
    partition_infos[f"device{i}"] = partition.device.__str__()
    partition_infos[f"mountpoint{i}"] = partition.mountpoint
    partition_infos[f"file_sys_type{i}"] = partition.fstype
    partition_usage = psutil.disk_usage(partition.mountpoint)
    partition_infos[f"part_total_size{i}"] = partition_usage.total
    partition_infos[f"part_used_size{i}"] = partition_usage.used
    partition_infos[f"part_free_size{i}"] = partition_usage.free
    partition_infos[f"part_percent_size{i}"] = partition_usage.percent
    i += 1

# network infos
if_address = psutil.net_if_addrs()
for interface_name, interface_addresses in if_address.items():
    for address in interface_addresses:
        interface = interface_name
        if str(address.family) == 'AddressFamily.AF_INET':
            ip_address = address.address
            netmask = address.netmask
            broadcast_ip = address.broadcast
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            mac_address = address.address
            netmask = address.netmask
            broadcast_mac = address.broadcast

# generating ui
root = Tk()
root.title("My Pc's Specs")
root.resizable(False, False)
title_lbl = Label(root,
                  text="💻MY PC'S SPECS",
                  fg='darkred',
                  font=30).grid(row=0, column=0)

def export_to_txt_file():
    file = open('my_pc_specs.txt', 'w')
    file.write(f"Machine Type: {machine_type}\n"
               f"Network Type: {network_type}\n"
               f"Operating System: {operating_system}\n"
               f"OS Version: {os_version}\n"
               f"Processor: {processor}\n"
               f"Cores (Physical): {physical_cores}\n"
               f"Cores (Total): {total_cores}\n"
               f"Speed Min/Max: ({cpu_min_speed} / {cpu_max_speed})\n"
               f"RAM: {round(byteToGb(ram_total), 2)} GB\n"
               f"IP Address: {ip_address}\n"
               f"Netmask: {netmask}\n"
               f"Broadcast IP: {broadcast_ip}\n")
    file.close()
    try:
        file = open('my_pc_specs.txt', 'a')
        file.write(f"MAC Address: {mac_address}")
        file.close()
    except:
        file = open('my_pc_specs.txt', 'a')
        file.write(f"MAC Address: ")
        file.close()

    os.startfile("my_pc_specs.txt")

Button(root,
       text="📜Export to '.txt' file",
       bg='grey',
       fg='lightblue',
       command=export_to_txt_file).grid(row=0, column=4, sticky='ew')

m_type_lbl = Label(root,
                   text="Machine Type: ",
                   fg='darkblue').grid(row=1, column=0)

m_type_result = Label(root,
                      text=machine_type).grid(row=1, column=1)

n_type_lbl = Label(root,
                   text="Network Type: ",
                   fg='darkblue').grid(row=2, column=0)

n_type_result = Label(root,
                      text=network_type).grid(row=2, column=1)

os_label = Label(root,
                   text="Operating System: ",
                   fg='darkblue').grid(row=3, column=0)

os_result =  Label(root,
                      text=operating_system).grid(row=3, column=1)

os_v_label = Label(root,
                   text="OS Version: ",
                   fg='darkblue').grid(row=4, column=0)

os_v_result = Label(root,
                      text=os_version).grid(row=4, column=1)

ttk.Separator(root, orient='vertical').grid(row=1,column=2, sticky='ns')
ttk.Separator(root, orient='vertical').grid(row=2,column=2, sticky='ns')
ttk.Separator(root, orient='vertical').grid(row=3,column=2, sticky='ns')
ttk.Separator(root, orient='vertical').grid(row=4,column=2, sticky='ns')

processor_label = Label(root,
                   text="Processor: ",
                   fg='darkblue').grid(row=1, column=3)

processor_result = Label(root,
                      text=processor).grid(row=1, column=4)

physical_cores_label = Label(root,
                   text="Cores (Physical): ",
                   fg='darkblue').grid(row=2, column=3)

physical_cores_result = Label(root,
                      text=physical_cores).grid(row=2, column=4)

total_cores_label = Label(root,
                   text="Cores (Total): ",
                   fg='darkblue').grid(row=3, column=3)

total_cores_result = Label(root,
                      text=total_cores).grid(row=3, column=4)
0
cpu_min_max_speed_label = Label(root,
                   text="Speed Min/Max: ",
                   fg='darkblue').grid(row=4, column=3)

cpu_min_max_speed_result = Label(root,
                      text=f"({cpu_min_speed} / {cpu_max_speed})").grid(row=4, column=4)

ttk.Separator(root, orient='horizontal').grid(row=5,column=0, sticky='ew')
ttk.Separator(root, orient='horizontal').grid(row=5,column=1, sticky='ew')
ttk.Separator(root, orient='horizontal').grid(row=5,column=2, sticky='ew')
ttk.Separator(root, orient='horizontal').grid(row=5,column=3, sticky='ew')
ttk.Separator(root, orient='horizontal').grid(row=5,column=4, sticky='ew')
ram_total_label = Label(root,
                   text="RAM: ",
                   fg='darkblue').grid(row=6, column=0)

ram_total_result = Label(root,
                      text=f"{round(byteToGb(ram_total), 2)} GB").grid(row=6, column=1)

Label(root,
    text="Partition: ",
    fg='darkblue').grid(row=7, column=0)

Label(root,
    text=partition_infos['device0']).grid(row=7, column=1)

Label(root,
      text="Usage:",
      fg='darkblue').grid(row=7, column=3)

Label(root,
      text=f"%{partition_infos['part_percent_size0']}   {round(byteToGb(partition_infos['part_used_size0']),2)}GB/{round(byteToGb(partition_infos['part_total_size0']),2)}GB").grid(row=7, column=4)

try:
    Label(root,
          text=partition_infos['device1']).grid(row=8, column=1)

    Label(root,
          text="Usage:",
          fg='darkblue').grid(row=8, column=3)

    Label(root,
          text=f"%{partition_infos['part_percent_size1']}   {round(byteToGb(partition_infos['part_used_size1']), 2)}GB/{round(byteToGb(partition_infos['part_total_size1']), 2)}GB").grid(
        row=8, column=4)

    try:
        Label(root,
              text=partition_infos['device2']).grid(row=9, column=1)

        Label(root,
              text="Usage:",
              fg='darkblue').grid(row=9, column=3)

        Label(root,
              text=f"%{partition_infos['part_percent_size2']}   {round(byteToGb(partition_infos['part_used_size2']), 2)}GB/{round(byteToGb(partition_infos['part_total_size2']), 2)}GB").grid(
            row=9, column=4)

        try:
            Label(root,
                  text=partition_infos['device3']).grid(row=10, column=1)

            Label(root,
                  text="Usage:",
                  fg='darkblue').grid(row=10, column=3)

            Label(root,
                  text=f"%{partition_infos['part_percent_size3']}   {round(byteToGb(partition_infos['part_used_size3']), 2)}GB/{round(byteToGb(partition_infos['part_total_size3']), 2)}GB").grid(
                row=10, column=4)

            try:
                Label(root,
                      text=partition_infos['device4']).grid(row=11, column=1)

                Label(root,
                      text="Usage:",
                      fg='darkblue').grid(row=11, column=3)

                Label(root,
                      text=f"%{partition_infos['part_percent_size4']}   {round(byteToGb(partition_infos['part_used_size4']), 2)}GB/{round(byteToGb(partition_infos['part_total_size4']), 2)}GB").grid(
                    row=11, column=4)

                try:
                    Label(root,
                          text=partition_infos['device5']).grid(row=12, column=1)

                    Label(root,
                          text="Usage:",
                          fg='darkblue').grid(row=12, column=3)

                    Label(root,
                          text=f"%{partition_infos['part_percent_size5']}   {round(byteToGb(partition_infos['part_used_size5']), 2)}GB/{round(byteToGb(partition_infos['part_total_size5']), 2)}GB").grid(
                        row=12, column=4)

                    ttk.Separator(root, orient='horizontal').grid(row=13, column=0, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=13, column=1, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=13, column=2, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=13, column=3, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=13, column=4, sticky='ew')
                except:
                    ttk.Separator(root, orient='horizontal').grid(row=12, column=0, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=12, column=1, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=12, column=2, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=12, column=3, sticky='ew')
                    ttk.Separator(root, orient='horizontal').grid(row=12, column=4, sticky='ew')
            except:
                ttk.Separator(root, orient='horizontal').grid(row=11, column=0, sticky='ew')
                ttk.Separator(root, orient='horizontal').grid(row=11, column=1, sticky='ew')
                ttk.Separator(root, orient='horizontal').grid(row=11, column=2, sticky='ew')
                ttk.Separator(root, orient='horizontal').grid(row=11, column=3, sticky='ew')
                ttk.Separator(root, orient='horizontal').grid(row=11, column=4, sticky='ew')
        except:
            ttk.Separator(root, orient='horizontal').grid(row=10, column=0, sticky='ew')
            ttk.Separator(root, orient='horizontal').grid(row=10, column=1, sticky='ew')
            ttk.Separator(root, orient='horizontal').grid(row=10, column=2, sticky='ew')
            ttk.Separator(root, orient='horizontal').grid(row=10, column=3, sticky='ew')
            ttk.Separator(root, orient='horizontal').grid(row=10, column=4, sticky='ew')
    except:
        ttk.Separator(root, orient='horizontal').grid(row=9, column=0, sticky='ew')
        ttk.Separator(root, orient='horizontal').grid(row=9, column=1, sticky='ew')
        ttk.Separator(root, orient='horizontal').grid(row=9, column=2, sticky='ew')
        ttk.Separator(root, orient='horizontal').grid(row=9, column=3, sticky='ew')
        ttk.Separator(root, orient='horizontal').grid(row=9, column=4, sticky='ew')
except:
    ttk.Separator(root, orient='horizontal').grid(row=8, column=0, sticky='ew')
    ttk.Separator(root, orient='horizontal').grid(row=8, column=1, sticky='ew')
    ttk.Separator(root, orient='horizontal').grid(row=8, column=2, sticky='ew')
    ttk.Separator(root, orient='horizontal').grid(row=8, column=3, sticky='ew')
    ttk.Separator(root, orient='horizontal').grid(row=8, column=4, sticky='ew')

Label(root,
        text="IP Address:",
        fg='darkblue').grid(row=9, column=0)

Label(root,
      text=ip_address).grid(row=9, column=1)

Label(root,
        text="Netmask:",
        fg='darkblue').grid(row=10, column=0)

Label(root,
      text=netmask).grid(row=10, column=1)

Label(root,
        text="Broadcast IP:",
        fg='darkblue').grid(row=11, column=0)

Label(root,
      text=broadcast_ip).grid(row=11, column=1)

Label(root,
        text="MAC Address:",
        fg='darkblue').grid(row=12, column=0)

try:
    Label(root,
          text=mac_address).grid(row=12, column=1)
except:
    Label(root,
          text="").grid(row=12, column=1)

root.mainloop()