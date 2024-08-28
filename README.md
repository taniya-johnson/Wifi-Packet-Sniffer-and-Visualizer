__Wi-Fi Packet Sniffer and Visualizer__

Welcome to my Wi-Fi Packet Sniffer and Visualizer project! 📡

This Python script captures Wi-Fi network packets, logs them to a CSV file, and visualizes packet lengths over time using Matplotlib. It leverages Scapy for packet sniffing, Pandas for data handling, and Matplotlib for plotting.

__📋 Features__

Network Interface Detection: Lists available network interfaces to choose from for sniffing.
Packet Sniffing: Captures packets on the selected network interface.
Packet Logging: Logs packet details (time, source IP, destination IP, and length) to a CSV file.
Data Visualization: Plots packet lengths over time with color mapping for enhanced insights.


__🛠️ Requirements__

Python 3.x

Scapy: For packet sniffing.

Pandas: For data manipulation and logging.

Matplotlib: For data visualization.


__📝 Code Explanation__

List Network Interfaces: The script prints available network interfaces using get_if_list() from Scapy.

Define Interface: Set the interface for packet sniffing. Replace "Wi-Fi" with the appropriate interface name from the list printed by the script.

Packet Callback Function: Defines packet_callback(packet) to process and log packet details:

Extracts packet time, source IP, destination IP, and length.

Appends packet data to a CSV file.

Sniff Packets: Captures 50 packets on the specified interface and processes them using sniff().

__Data Loading and Visualization:__

Loads packet data from the CSV file into a Pandas DataFrame.

Converts the Time column to datetime format.

Defines a color map and plots packet lengths over time using Matplotlib, with different colors representing different packet lengths.

Saves the plot as a PNG file and displays it.


Feel free to explore the project and contribute! If you have any questions or suggestions, don’t hesitate to open an issue or submit a pull request. Happy coding! 🚀

Regards,
__Taniya Johnson__
