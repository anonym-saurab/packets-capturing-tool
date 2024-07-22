## A TOOL CREATED USING PYTHON, SCAPY(LIBRARY), AND TKINTER(GUI) FOR CREATING AND CAPTURING PACKETS SENT TO A DESTINATION ADDRESS

from scapy.all import *

from tkinter import *
from tkinter import ttk
admin = Tk()
admin.title("Network Analyze Tool")
admin.geometry("500x900")
e = Entry(admin, width=60, borderwidth=5)
e.grid(row=1, column=0, columnspan=2)

Label(admin, text="Please enter a destination addr. below :").grid(row=0, column=0, columnspan=2)
# creating a packet
def creating_packet(dst):
    dst=e.get()
    packet=IP(dst=dst)/ICMP()
    e.delete(0, END)
    send(packet)
# buttons for sending packets
button_send = Button(admin, text="send the packet", padx=40, pady=20, command= lambda: creating_packet('Packet sent to destination address'))
button_send.grid(row=2, column=0, columnspan=2)


# sniffing packets
def sniffing_packets():
    sniff_packet = e.get()
    packets = sniff(filter=sniff_packet, count=10, timeout=20)
    e.delete(0, END)
    packets.show()
    for packet in packets:
        sniffed_packets_list.insert(END, packet.summary())  ## displaying captured packets
## buttons to sniff
button_sniff = Button(admin, text= "capture the packets", command=sniffing_packets)
button_sniff.grid(row=6, column=1)


# creating a dropdown/multi-choice options for the filter
Label(admin, text="Please choose any one for filter to apply").grid(row=3, column=1)
filter_variable = StringVar()
filter_options = ["tcp and port 80", "ip and port 443", "udp and port 443", "ftp and port 25", "tcp and port 443"]
## using 'Combobox' for multiple options
filter_dropdown = ttk.Combobox(admin, textvariable=filter_variable, values=filter_options)
filter_dropdown.grid(row=4, column=1)
filter_dropdown.current(0) ## sets the default value

## disaplaying the sniffed packets
sniffed_packets_list = Listbox(admin, width=50, height=10)
sniffed_packets_list.grid(row=5, column=1)

## button to clear everything
def clear():
    e.delete(0, END)

admin.mainloop()