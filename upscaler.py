import sys
import os
import cv2
import shutil

''' Export frames from video to cache folder '''
def export_images(filename, cache_path):

    print("Exporting frames to cache")

    cap= cv2.VideoCapture(filename)

    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        res = cv2.imwrite(os.path.join(cache_path, str(i) + '.jpg'),frame)
        i+=1

    cap.release()
    cv2.destroyAllWindows()



def resize(src, scale=10):
    width = int(src.shape[1] * scale / 100)
    height = int(src.shape[0] * scale / 100)
    dsize = (width, height)

    return cv2.resize(src, dsize)

def compare_frames(frame1, frame2):

    rframe1 = resize(frame1)
    rframe2 = resize(frame2)

    difference = cv2.subtract(rframe1, rframe2)
    b, g, r = cv2.split(difference)

    return sum(sum(b)) + sum(sum(g)) + sum(sum(r))


def process_video(path_pre, path_post):

    frame1 = cv2.imread(os.path.join(path_pre, '537.jpg'))
    frame2 = cv2.imread(os.path.join(path_pre, '538.jpg'))

    print(compare_frames(frame1, frame2))



''' Deletes images in the cache '''
def delete_cache(cache_path):
    shutil.rmtree(cache_path)




def main(args):

    filename = args[0]

    # Create cache folder/subfolders if not existing
    cache_path = os.getenv('APPDATA') + "\srgan-upscaler\cache"
    cache_path_pre = os.getenv('APPDATA') + "\srgan-upscaler\cache\pre"
    cache_path_post = os.getenv('APPDATA') + "\srgan-upscaler\cache\post"

    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
        os.makedirs(cache_path_pre)
        os.makedirs(cache_path_post)
        

    ### STARTING PROCESS ### 
    # export_images(filename, cache_path_pre)
    process_video(cache_path_pre, cache_path_post)
    # delete_cache(cache_path)

if __name__ == '__main__':
    main(sys.argv[1:])
