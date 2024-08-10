
import cv2
from pyzbar.pyzbar import decode

def decode_qr_code(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Decode the QR code
    decoded_objects = decode(img)
    # Iterate over all decoded objects
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))

        # Draw the bounding box
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        
        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(img, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # Display the image
    cv2.imshow("QR Code Decoder", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter the path to the QR code image: ")
    decode_qr_code(image_path)
