import cv2
import dropbox
import time
import random
start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while (result):
        ret,frame = videoCaptureObject.read()
        img_name = 'img' + str(number) + '.png' 
        img_counter = img_counter + 1
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False

    return img_name
    print("snapshot taken =)")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    acces_token="sl.AveDyPM4jNDxcR8lLr3ubijvdhV4vbRcO5Ragk32GL6kvah947ILrcMGyKfZsys1T6wtOwYqFv_QS2A0GIXDD4tgHeXhRy0KdydFsPqibqqP6bTkhTMEPfoyLmNZLkjNMkBxc6w"
    file = img_name
    file_from = file
    file_to = '/NewFolder1/' + img_name
    dbx = dropbox.Dropbox(acces_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded successfully =)")

def main():
    while(True):
        if(( time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file = name
if __name__ == "__main__":
    main()
