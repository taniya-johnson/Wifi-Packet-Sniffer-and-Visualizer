from scapy.all import sniff, get_if_list
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import datetime

interfaces = get_if_list()
print("Available interfaces:")
for iface in interfaces:
    print(iface)
interface = "Wi-Fi"  # Replace with the correct network interface name from the list

# File to store packet logs
log_file = 'packets_log.csv'

# Function to process and log packets
def packet_callback(packet):
    # Extract packet details
    packet_time = datetime.datetime.fromtimestamp(packet.time)
    source_ip = packet.getlayer('IP').src if packet.haslayer('IP') else 'N/A'
    dest_ip = packet.getlayer('IP').dst if packet.haslayer('IP') else 'N/A'
    length = len(packet)
    
    # Create a DataFrame for the packet
    data = {
        'Time': [packet_time],
        'Source': [source_ip],
        'Destination': [dest_ip],
        'Length': [length],
    }
    df = pd.DataFrame(data)
    
   
    df.to_csv(log_file, mode='a', header=False, index=False)


print(f"Sniffing packets on {interface}...")
sniff(iface=interface, prn=packet_callback, count=50)
df = pd.read_csv(log_file, names=['Time', 'Source', 'Destination', 'Length'])
df['Time'] = pd.to_datetime(df['Time'])
# Define color map for packet lengths
norm = mcolors.Normalize(vmin=df['Length'].min(), vmax=df['Length'].max())
cmap = plt.get_cmap('viridis')

# Plot packet lengths over time with different colors
plt.figure(figsize=(12, 8))
sc = plt.scatter(df['Time'], df['Length'], c=df['Length'], cmap=cmap, norm=norm, alpha=0.7, edgecolors='w', s=80)
cbar = plt.colorbar(sc)
cbar.set_label('Packet Length (bytes)', fontsize=14)

# Improve plot aesthetics
plt.title('Packet Length Over Time', fontsize=16)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Packet Length (bytes)', fontsize=14)
plt.grid(True)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save and show the plot
plt.savefig('packet_length_over_time_colored.png', dpi=300)
plt.show()
