import threading,time
import requests
def run(n):
    semaphore.acquire()
    # time.sleep(1)
    res=requests.get(n)
    print("访问了一个专业链接: %s" %res.status_code)
    semaphore.release()
def funcs():
    urllist = ['https://www.anglia.ac.uk/study/undergraduate/abnormal-and-clinical-psychology',
               'https://www.anglia.ac.uk/study/undergraduate/accounting-and-finance-peterborough',
               'https://www.anglia.ac.uk/study/undergraduate/accounting-and-finance',
               'https://www.anglia.ac.uk/study/undergraduate/acute-care-top-up',
               'https://www.anglia.ac.uk/study/undergraduate/animal-behaviour',
               'https://www.anglia.ac.uk/study/undergraduate/animal-behaviour-with-foundation-year',
               'https://www.anglia.ac.uk/study/undergraduate/applied-computer-science-west-anglia',
               'https://www.anglia.ac.uk/study/undergraduate/applied-nutritional-science',
               'https://www.anglia.ac.uk/study/undergraduate/applied-nutritional-science-with-foundation-year',
               'https://www.anglia.ac.uk/study/undergraduate/archaeology-and-landscape-history-peterborough',
               'https://www.anglia.ac.uk/study/undergraduate/architectural-technology',]
    for i in urllist:
        t = threading.Thread(target=run, args=(i,))
        t.start()
        # t.join()
if __name__ == '__main__':
    num= 0
    starttime = time.time()
    semaphore  = threading.BoundedSemaphore(10) #最多允许5个线程同时运行
    funcs()
while threading.active_count() != 1:
    pass
else:
    print('----all threads done---')
    print(num)
    endtime = time.time()
    print(endtime - starttime)