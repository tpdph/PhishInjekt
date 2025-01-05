import logging
import socket
import threading

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            conn = s.connect_ex((target_ip, port))
            if conn == 0:
                logging.info(f"Port {port} is open on {target_ip}")
                return port
    except socket.error as e:
        logging.error(f"Socket error on {target_ip}:{port}: {e}")
        return None

def scan_ports(target_ip, port_range):
    logging.info(f"Starting port scan on {target_ip}:{port_range[0]}-{port_range[1]}")
    open_ports = []
    threads = []
    for port in range(port_range[0], port_range[1] + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for port in range(port_range[0], port_range[1] + 1):
        result = scan_port(target_ip, port)
        if result:
            open_ports.append(result)
    return open_ports

if __name__ == '__main__':
    target_ip = '127.0.0.1'
    port_range = (1, 100)
    open_ports = scan_ports(target_ip, port_range)
    print(f"Open ports on {target_ip}: {open_ports}")
