import argparse
from scapy.all import *

# Define the destination
target = "192.168.1.1"  # Replace with the target IP

def send_icmp_timestamp_request(target, timeout):

	#Craft an ICMP Timestamp Request
	packet = IP(dst=target) / ICMP(type=13, code=0)
	
	#send packet and wait for response
	response = sr1(packet, timeout=timeout, verbose=0)
	
	if response:
		print(f"Reply received from {response.src}")
		icmp = response[ICMP]
		if icmp.type == 14: #ICMP Timestamp Reply
			print("ICMP Timestamp Reply received")
			print(f"Originate Timestamp: {icmp.ts_ori}")
			print(f"Receive Timestamp: {icmp.ts_rx}")
			print(f"Transmit Timestamp: {icmp.ts_tx}")
	else:
		print("No reply recieved")
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Send ICMP Timestamp Request to a target.")
	parser.add_argument("target", type=str, help="Target IP address to send the ICMP Timestamp Request")
	parser.add_argument("--timeout", type=int, default=2, help="Timeout for waiting for a reply (in seconds)")
	
	args = parser.parse_args()
	
	send_icmp_timestamp_request(args.target, args.timeout)
	
