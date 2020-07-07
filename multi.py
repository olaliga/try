from multiprocessing import Pool, cpu_count
import os
import time


def long_time_task(i):
    print('子程序: {} - 任務{}'.format(os.getpid(), i))
    time.sleep(2)
    print("結果: {}".format(8 ** 20))

print("CPU核心數:{}".format(cpu_count()))
print('當前母程序: {}'.format(os.getpid()))
start = time.time()
p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print('等待所有子程序完成。')
p.close()
p.join()
end = time.time()
print("總共用時{}秒".format((end - start)))