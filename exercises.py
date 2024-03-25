import time
import concurrent.futures
import requests
from multiprocessing import Process, Pool
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

def download(url):
    img_data = requests.get(url).content
    img_name = url.split("/")[3]
    img_name = f"{img_name}.jpg"

    with open(img_name, "wb") as image_file:
        image_file.write(img_data)
        print(f"{img_name} Download Completed!")



#Total Time: 17.797471284866333
# for url in img_urls:
#     download(url)

#Total Time: 13.900304794311523
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(download, img_urls)

if __name__ == "__main__":
    start = time.time()

    p = Pool(10)
    values = p.map(download, img_urls)
    p.close()

    end = time.time()
    print(f"Total Time: {end-start}")





# import multiprocessing
# import time
# from multiprocessing import Process, Pool
#
# def print_cube(num):
#     print("Cube: {}".format(num**3))
#
#
# def print_square(num):
#     time.sleep(num)
#     print("Square: {}".format(num**2))
#     return "Square: {}".format(num**2)
#
# if __name__ == "__main__":
#     # p1 = Process(target=print_cube, args=(10,))
#     # p2 = Process(target=print_square, args=(10,))
#     #
#     # p1.start()
#     # p2.start()
#     #
#     # p1.join()
#     # p2.join()
#     #
#     # print("Done")
#
#     nums = [4, 7, 2, 15]
#     p = Pool(2)
#     values = p.map(print_square, nums)
#     p.close()
#     # print(values)

















