import paramiko
import time

# SSH连接参数
hostname = '192.168.43.90'
port = 22
username = 'buwai'
password = '852456'

# 定义多个文件路径
file_paths = [
    '/home/buwai/yolov5-seg/photoelecricity1020/img/img/识别1.jpg',
    '/home/buwai/yolov5-seg/photoelecricity1020/img/img/识别2.jpg',
    '/home/buwai/yolov5-seg/photoelecricity1020/img/img/识别3.jpg',
    '/home/buwai/yolov5-seg/photoelecricity1020/img/img/规划1.jpg',
    '/home/buwai/yolov5-seg/photoelecricity1020/img/img/规划2.jpg',
    # 添加更多文件路径
]

# 循环下载文件
while True:
    for remote_file_path in file_paths:
        # 连接到SSH服务器
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, port, username, password)

        # 提取文件名
        file_name = remote_file_path.split('/')[-1]
        downloaded_file_path = f'D:/ssh link/buwai/yolov5-seg/photoelecricity1020/img/img/{file_name}'

        sftp = ssh_client.open_sftp()
        sftp.get(remote_file_path, downloaded_file_path)
        sftp.close()

        print(f'Downloaded {remote_file_path} to {downloaded_file_path}')

        # 关闭SSH连接
        ssh_client.close()

    # 暂停五秒
    time.sleep(5)
