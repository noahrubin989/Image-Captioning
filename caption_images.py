import os
import numpy as np

from typing import List
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import ImageDescription


def setup_client() -> ComputerVisionClient:
    """
    Sets up the Azure Computer Vision client using environment variables.

    Returns:
        ComputerVisionClient: An authenticated Computer Vision client.
    """
    load_dotenv()
    region = os.environ["AI_SERVICE_REGION"]
    key = os.environ["AI_SERVICE_KEY"]

    credentials = CognitiveServicesCredentials(key)
    client = ComputerVisionClient(
        endpoint=f"https://{region}.api.cognitive.microsoft.com/",
        credentials=credentials
    )
    return client


def get_image_paths(folder_path: str) -> List[str]:
    """
    Retrieves all image file paths (JPG, JPEG, PNG) within the specified folder.

    Args:
        folder_path (str): The path to the folder containing images.

    Returns:
        List[str]: A list of absolute file paths for images in the folder.
    """
    valid_extensions = ('.jpg', '.jpeg', '.png')
    images = [
        os.path.join(folder_path, file_name)
        for file_name in os.listdir(folder_path)
        if file_name.lower().endswith(valid_extensions)
    ]
    return images


def generate_captions(
    client: ComputerVisionClient,
    image_path: str,
    language: str = "en",
    max_candidates: int = 1
) -> ImageDescription:
    """
    Generates captions using the Computer Vision client for a given image.

    Args:
        client (ComputerVisionClient): The Azure Computer Vision client.
        image_path (str): The path to the image file.
        language (str, optional): The language for the caption. Defaults to "en".
        max_candidates (int, optional): The maximum number of candidate captions. Defaults to 1.

    Returns:
        Description: A Description object containing captions and related metadata.
    """
    with open(image_path, "rb") as image_stream:
        analysis = client.describe_image_in_stream(
            image=image_stream,
            max_candidates=max_candidates,
            language=language
        )
    return analysis


def main() -> None:
    """
    Main function that sets up the Computer Vision client, processes each image in the `./images` folder,
    and prints out the generated captions along with confidence scores.
    """
    client = setup_client()
    image_folder = "./images"

    # Ensure the folder exists or handle the case where it does not
    if not os.path.isdir(image_folder):
        print(f"Folder '{image_folder}' does not exist. Exiting...")
        return

    image_paths = get_image_paths(image_folder)

    if not image_paths:
        print(f"No valid images found in '{image_folder}'. Exiting...")
        return

    for image_path in image_paths:
        analysis = generate_captions(client, image_path, language="en", max_candidates=1)
        if analysis.captions:
            # Print out each caption with confidence
            for caption in analysis.captions:
                print(f"Image: {os.path.basename(image_path)}")
                print(f"  Caption: {caption.text}")
                print(f"  Confidence: {np.round(caption.confidence, 2)}")
                print()
        else:
            # Fallback if no captions are returned
            print(f"No captions found for image: {os.path.basename(image_path)}")

if __name__ == "__main__":
    main()
