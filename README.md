# # Face Recognition Script

This Python application identifies and extracts images of a specific person from a collection of photos. Utilizing the `face_recognition` library, it analyzes facial features, compares them to a user-provided reference image, and saves matched images to an output folder. The application is dockerized for convenient deployment and scalability across various environments.


## Prerequisites
1.  Install [Docker](https://www.docker.com/get-started) on your system (Windows or Mac).
    
2.  Clone this repository or download the source files.
## Directory Structure


```markdown
face_recognition_script/
│
├── Dockerfile
├── requirements.txt
├── face_recognition.py
├── input_images/
│ ├── .gitkeep
├── reference_images/
│ ├── .gitkeep
└── output_images/
├── .gitkeep
```
-   Place the images you want to process in the `input_images` folder.
-   Place the reference image containing the face of the person you want to match in the `reference_images` folder.

## Building the Docker Image

1.  Open a terminal (Mac) or PowerShell (Windows) and navigate to the `face_recognition_script` directory.
    
2.  Build the Docker image using the following command:
```bash
docker build -t face-recognition-image .
```
This command will create a Docker image named `face-recognition-image`.

## Running the Application
1.  Run the application using the following command:
```
docker run -v "$(pwd)/input_images:/app/input_images" -v "$(pwd)/reference_images:/app/reference_images" -v "$(pwd)/output_images:/app/output_images" face-recognition-image input_images reference_images/reference_image.jpg output_images
```
-   Replace `reference_images/reference_image.jpg` with the path to your reference image inside the `reference_images` folder.

2.  The matched images will be saved in the `output_images` folder.

## Customizing Tolerance Level
By default, the application uses a tolerance level of 0.6. To use a custom tolerance level, pass it as an additional argument when running the Docker container:

```
docker run -v "$(pwd)/input_images:/app/input_images" -v "$(pwd)/reference_images:/app/reference_images" -v "$(pwd)/output_images:/app/output_images" face-recognition-image input_images reference_images/reference_image.jpg output_images 0.5
```
-   Replace `0.5` with your desired tolerance level.
## License
This project is licensed under the MIT License.
