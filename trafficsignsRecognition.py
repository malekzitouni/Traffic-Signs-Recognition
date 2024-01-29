#Detect traffic signs via IPWebcam
import cv2
import numpy as np
import requests

def detect_traffic_light_color(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hue = hsv[0][0][0]  # Get the hue value

    # Define hue ranges for different colors
    red_range = (0, 5)  # Red has a wrap-around at 0-5 hue values
    orange_range = (6, 22)
    green_range = (33, 78)
    blue_range = (79, 131)  # Assuming a hue of 131 represents blue
    # Note: Adjust these ranges based on your specific color detection criteria

    # Check which color range the detected hue falls into
    if hue <= red_range[1] or hue < red_range[0]:
        print("The detected color is: Red")
    elif orange_range[0] < hue <= orange_range[1]:
        print("The detected color is: Orange")
    elif green_range[0] < hue <= green_range[1]:
        print("The detected color is: Green")
    elif blue_range[0] < hue <= blue_range[1]:
        print("The detected color is: Blue")
    else:
        print("The detected color is: Unknown")

def main():
    url = "http://192.168.2.149:4343/shot.jpg"

    while True:
        try:
            response = requests.get(url)
            img_arr = np.array(bytearray(response.content), dtype=np.uint8)
            frame = cv2.imdecode(img_arr, -1)
            frame = cv2.resize(frame, (400, 400))
            cv2.imshow("androidcam", frame)

            # Call the detect_traffic_light_color function
            detect_traffic_light_color(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(f"Error: {e}")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
