# Automated Image Captioning

## Overview

The following is a python script that uses the Computer Vision API, in particular, the `ComputerVisionClient` class.

This script is beneficial for businesses that want to automatically generate descriptive captions from images, reducing manual effort, improving accessibility, and assisting visually impaired individuals in whicvh images can then be explained using text-to-speech systems.

## Usage

1. Set Environment Variables

Create a `.env` file in the root of your project with the following variables:
  AI_SERVICE_REGION=your-azure-region-here
  AI_SERVICE_KEY=your-azure-computer-vision-key-here

2. Prepare Your Images

Place all the images you want to caption inside the ./images folder.
Supported file types by default are .jpg, .jpeg, and .png.
Run the Script

bash
Copy
python main.py
Where main.py (or whichever name you have chosen) contains the script that uses Azure Cognitive Services to caption your images.

View Captions

The script will iterate over each image in the ./images folder.
For each image, it will print out the caption(s) and confidence scores to the console.
