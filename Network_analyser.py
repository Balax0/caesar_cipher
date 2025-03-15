#task 5


from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    """Function to process captured packets"""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"\n[Packet Captured] Source: {src_ip} → Destination: {dst_ip} | Protocol: {protocol}")

        # Handling TCP Packets
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"TCP Packet | Src Port: {src_port}, Dst Port: {dst_port}")

        # Handling UDP Packets
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"UDP Packet | Src Port: {src_port}, Dst Port: {dst_port}")

        # Handling ICMP Packets
        elif ICMP in packet:
            print("ICMP Packet Detected")

# Sniff network packets (Requires admin/root privileges)
print("Starting packet sniffer...")
sniff(prn=packet_callback, store=False)
