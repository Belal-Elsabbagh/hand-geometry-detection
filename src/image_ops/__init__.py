import cv2

from src.image_ops.image_shape import ImageShape


def get_shape(img):
    """
    Returns an object with data about the given image's shape
    """
    return ImageShape(img)


def read_img(file_path, color_mode=None):
    if color_mode is None:
        color_mode = cv2.IMREAD_UNCHANGED
    return cv2.imread(file_path, color_mode)


def read_img_color(file_path):
    return read_img(file_path, cv2.IMREAD_COLOR)


def read_img_grayscale(file_path):
    return read_img(file_path, cv2.IMREAD_GRAYSCALE)


def show_img(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None


def load_cascade_classifier(xml_path):
    return cv2.CascadeClassifier(xml_path)


def blur_img(img, val):
    return cv2.medianBlur(img, val)


def binarize_img(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def convert_img_to_color(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def put_text_on_image(res, text, x, y):
    return cv2.putText(res, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)


def draw_contours(img, contour, color=(0, 255, 0), thickness=3):
    return cv2.drawContours(img, contour, 0, color, thickness)


def approx_contour(contour):
    return cv2.approxPolyDP(contour, epsilon(contour), True)


def epsilon(contour, coefficient=0.01):
    return coefficient * cv2.arcLength(contour, True)


def scale_img(img, scale_coefficient: float):
    """

    :param img: The given image
    :type img:
    :param scale_coefficient: The value to multiply scale by
    :type scale_coefficient: float
    :return: The resized image
    :rtype:
    """
    width = int(img.shape[1] * scale_coefficient)
    height = int(img.shape[0] * scale_coefficient)
    return resize_img(img, width, height)


def resize_img(img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
