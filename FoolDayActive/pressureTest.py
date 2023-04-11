import threading
import time
import requests
import cProfile

# 定义一个方法作为线程的执行体
def run(count):
    for i in range(count):
        response = requests.get('https://www.example.com')
        print(f'[{threading.current_thread().name}] {i}: status code {response.status_code}')

if __name__ == '__main__':
    # 创建10个线程，并启动它们
    threads = []
    for i in range(10):
        thread = threading.Thread(target=run, args=(5,))
        #设置线程保护
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)

    # 等待所有线程执行完毕
    for thread in threads:
        print(thread.join())

    # 输出性能分析结果
    profiler = cProfile.Profile()
    profiler.print_stats()