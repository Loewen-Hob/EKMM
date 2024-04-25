from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import numpy as np
import cv2
import math

# scripts for crop images
def crop_image(img, position):
    def distance(x1,y1,x2,y2):
        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))    
    position = position.tolist()
    for i in range(4):
        for j in range(i+1, 4):
            if(position[i][0] > position[j][0]):
                tmp = position[j]
                position[j] = position[i]
                position[i] = tmp
    if position[0][1] > position[1][1]:
        tmp = position[0]
        position[0] = position[1]
        position[1] = tmp

    if position[2][1] > position[3][1]:
        tmp = position[2]
        position[2] = position[3]
        position[3] = tmp

    x1, y1 = position[0][0], position[0][1]
    x2, y2 = position[2][0], position[2][1]
    x3, y3 = position[3][0], position[3][1]
    x4, y4 = position[1][0], position[1][1]

    corners = np.zeros((4,2), np.float32)
    corners[0] = [x1, y1]
    corners[1] = [x2, y2]
    corners[2] = [x4, y4]
    corners[3] = [x3, y3]

    img_width = distance((x1+x4)/2, (y1+y4)/2, (x2+x3)/2, (y2+y3)/2)
    img_height = distance((x1+x2)/2, (y1+y2)/2, (x4+x3)/2, (y4+y3)/2)

    corners_trans = np.zeros((4,2), np.float32)
    corners_trans[0] = [0, 0]
    corners_trans[1] = [img_width - 1, 0]
    corners_trans[2] = [0, img_height - 1]
    corners_trans[3] = [img_width - 1, img_height - 1]

    transform = cv2.getPerspectiveTransform(corners, corners_trans)
    dst = cv2.warpPerspective(img, transform, (int(img_width), int(img_height)))
    return dst

def order_point(coor):
    arr = np.array(coor).reshape([4, 2])
    sum_ = np.sum(arr, 0)
    centroid = sum_ / arr.shape[0]
    theta = np.arctan2(arr[:, 1] - centroid[1], arr[:, 0] - centroid[0])
    sort_points = arr[np.argsort(theta)]
    sort_points = sort_points.reshape([4, -1])
    if sort_points[0][0] > centroid[0]:
        sort_points = np.concatenate([sort_points[3:], sort_points[:3]])
    sort_points = sort_points.reshape([4, 2]).astype('float32')
    return sort_points

def process_image_to_text(img_path, ocr_det_model=None, ocr_recog_model=None):
    try:
        # Read the image from the path
        image_full = cv2.imread(img_path)

        # Check if image is loaded properly
        if image_full is None:
            raise ValueError("Image could not be read.")

        # Perform OCR detection
        det_result = ocr_det_model(image_full)
        det_result = det_result['polygons']

        results = []

        for i in range(det_result.shape[0]):
            # Order points for cropping
            pts = order_point(det_result[i])

            # Crop the image based on detected points
            image_crop = crop_image(image_full, pts)
            
            # Perform OCR recognition on the cropped image
            result = ocr_recog_model(image_crop)
            text = result['text']

            # If the OCR text is a list, join it to make a single string
            if isinstance(text, list):
                text = ''.join(text)

            # Collect each detection's point and corresponding text
            results.append({'points': pts.tolist(), 'text': text})

        return results

    except Exception as e:
        # In case of any error during the process
        print(f"An error occurred: {str(e)}")
        return []


def main(img_path):
    # Load OCR models
    ocr_detection = pipeline(Tasks.ocr_detection, model='damo/cv_resnet18_ocr-detection-line-level_damo')
    ocr_recognition = pipeline(Tasks.ocr_recognition, model='damo/cv_convnextTiny_ocr-recognition-general_damo')

    # Process the image and get results
    results = process_image_to_text(img_path, ocr_det_model=ocr_detection, ocr_recog_model=ocr_recognition)
    return results