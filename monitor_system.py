# # import psutil
# # memory = psutil.virtual_memory()
# # print(f"Total memory: {memory.total / (1024 ** 3):.2f} GB")
# # print(f"used memory: {memory.percent}%")

# # # CPU usage
# # cpu_usage = psutil.cpu_percent(interval=1)
# # print(f"CPU usage: {cpu_usage}%")
# # # system mein kitne kaam chal rhe h 
# # p_ids = psutil.pids()
# # print(f"Total processes running: {len(p_ids)}")


# import psutil
# import time
# import os

# while True:
#     os.system('clear')
#     memory = psutil.virtual_memory()
#     cpu = psutil.cpu_percent(interval=1)
#     processes = len(psutil.pids())
#     print("---MASTER'S SYSTEM MONITOR---")
#     print(f"RAM Used: {memory.percent}%")
#     print(f"CPU Used: {cpu}%")
#     print(f"active Tasks: {processes}")
#     print('------------------------------')
#     print('Press Ctrl+C to exit')
# #     time.sleep(2)

# import psutil
# import time
# import os
# import logging
# logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')
# cpu_threshold = float(os.getenv('MY_CPU_LIMIT', 80.0))
# while True:
#     try:
#         os.system('clear')
#         cpu = psutil.cpu_percent(interval=1)
#         memory = psutil.virtual_memory()
#         print("---MASTER'S MNC-GRADE MONITOR---")
#         print(f"Curent CPU Usage: {cpu}% (limit: {cpu_threshold}%)")
#         print(f"Current RAM Usage: {memory.percent}%")
#         if cpu > cpu_threshold:
#             print("ALERT: CPU usage high hai!")
#             logging.warning(f"High CPU detected: {cpu}%")
#         logging.info(f"normal check - CPU: {cpu}%, RAM: {memory.percent}%")
#     except Exception as e:
#         print(f"Master, kuch gadbad hui: {e}")
#         logging.error(f"Error occurred: {e}")    
#         break
#     print("\nPress Ctrl+C to exit")
#     time.sleep(2)

# Git (Code ka Time Machine)///////////////////////////////////////////////////
