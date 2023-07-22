import os
import subprocess
import threading

def run_nmap_scan(target):
    print(f"Running Nmap scan on {target}...")
    nmap_output = subprocess.check_output(['nmap', '-T4', '-A', target])
    with open(f"{target}_nmap_scan.txt", 'wb') as nmap_output_file:
        nmap_output_file.write(nmap_output)
    print(f"Nmap scan completed for {target}.")

def run_nikto_scan(target):
    print(f"Running Nikto scan on {target}...")
    nikto_output = subprocess.check_output(['nikto', '-h', target])
    with open(f"{target}_nikto_scan.txt", 'wb') as nikto_output_file:
        nikto_output_file.write(nikto_output)
    print(f"Nikto scan completed for {target}.")

def main():
    target = input("Enter the target IP address or domain name: ")

    # Run Nmap and Nikto scans in parallel using threading
    nmap_thread = threading.Thread(target=run_nmap_scan, args=(target,))
    nikto_thread = threading.Thread(target=run_nikto_scan, args=(target,))

    nmap_thread.start()
    nikto_thread.start()

    nmap_thread.join()
    nikto_thread.join()

    print("Scans completed successfully.")

if name == "main":
    main()
