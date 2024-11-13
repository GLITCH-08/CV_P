import cv2
import sys

# Get user-supplied values
mode = sys.argv[1]  # 'img' for image, 'vid' for live video
imagePath = sys.argv[2] if mode == 'img' else None
cascPath = "haarcascade_frontalface_default.xml"

# Create the Haar Cascade
faceCascade = cv2.CascadeClassifier(cascPath)
if faceCascade.empty():
    print("Error loading cascade classifier.")
    sys.exit()

def detect_and_display(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(10, 10)
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Faces found", image)

if mode == 'img':
    # Image mode
    image = cv2.imread(imagePath)
    if image is None:
        print("Could not open or find the image.")
        sys.exit()
    detect_and_display(image)
    cv2.waitKey(0)

elif mode == 'vid':
    # Video mode
    cap = cv2.VideoCapture(0)  # Start webcam feed
    if not cap.isOpened():
        print("Error: Could not open video.")
        sys.exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        detect_and_display(frame)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release video capture

cv2.destroyAllWindows()  # Close all OpenCV windows
