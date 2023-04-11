import face_recognition
import os
import shutil
import sys
from PIL import Image
import numpy as np

def resize_image(image_path, max_size=1024):
    image = Image.open(image_path)
    width, height = image.size

    if max(width, height) > max_size:
        ratio = max_size / max(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        image = image.resize((new_width, new_height), Image.LANCZOS)

    # Convert the PIL image object to a NumPy array
    image_array = np.array(image)

    return image_array

def get_face_encodings(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)

    return face_encodings

def find_matching_faces(input_folder, ref_image_path, output_folder, tolerance=0.6):
    # Load the reference image and generate its encoding
    ref_image = resize_image(ref_image_path)
    # ref_image = face_recognition.load_image_file(ref_image)
    ref_image_encoding = face_recognition.face_encodings(ref_image)[0]

    # Loop through all the images in the input folder
    for file in os.listdir(input_folder):
        try:
            print(f"Processing file: {file}")

            # Load the image
            image_path = os.path.join(input_folder, file)
            image = resize_image(image_path)

            # Find face encodings in the image
            face_encodings = face_recognition.face_encodings(image)

            for face_encoding in face_encodings:
                # Compare the face encoding with the reference image encoding
                match = face_recognition.compare_faces([ref_image_encoding], face_encoding, tolerance=tolerance)

                if match[0]:
                    print(f"Found a match for {file}")
                    shutil.copy(image_path, os.path.join(output_folder, file))
                    break
        except Exception as e:
            print(f"Error processing file {file}: {e}")
            continue

def find_matching_faces_old(input_folder, ref_image_path, output_folder, tolerance=0.6):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get face encodings for the reference image
    ref_face_encodings = get_face_encodings(ref_image_path)

    # Check if there is at least one face in the reference image
    if not ref_face_encodings:
        print("No face found in the reference image.")
        return

    ref_face_encoding = ref_face_encodings[0]

    # Iterate through all images in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        print(f"Processing file: {file_name}")
        # Check if the current file is an image
        if not os.path.isfile(file_path) or not file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        print("Processing file inside")
        # Get face encodings for the current image
        face_encodings = get_face_encodings(file_path)

        # Check each face encoding against the reference face encoding
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([ref_face_encoding], face_encoding, tolerance)

            if match[0]:
                # If a match is found, copy the image to the output folder
                shutil.copy(file_path, output_folder)
                print(f"Match found: {file_path}")
                break

if __name__ == "__main__":
    input_folder = "input_images"
    ref_image_path = "reference_image/input.jpg"
    output_folder = "output_images"
    print("Starting..")
    tolerance = 0.6
    # if len(sys.argv) >= 2:
    #     ref_image_path = sys.argv[1]

    # if len(sys.argv) >= 3:
    #     tolerance = float(sys.argv[2])
    print(f"{ref_image_path} {tolerance}")

    find_matching_faces(input_folder, ref_image_path, output_folder, tolerance)
