# Automated Image Captioning

## Overview

The following is a python script that uses the Azure Computer Vision API, in particular, the `ComputerVisionClient` class.

This script is beneficial for businesses that want to automatically generate descriptive captions from images, reducing manual effort, improving accessibility, and assisting visually impaired individuals in which images can then be explained using text-to-speech systems.

## Usage

**1. Set Environment Variables**

* Create a `.env` file in the root of your project with the following variables:
```
AI_SERVICE_REGION=your_region
AI_SERVICE_KEY=your_key
```

**2. Prepare Your Images**

* Place all the images you want to caption inside the ./images folder.
* Supported file types by default are `.jpg`, `.jpeg`, and `.png`.

**3. Run the Script**

* Use the following snippet to run the script:
  `python3 caption_images.py`

**4. View Captions**

* The script will iterate over each image in the `./images` folder.
* For each image, it will print out the caption and confidence score to the console.

## Example output

Suppose there are three images in an `images` folder; 'street.jpg', 'person.jpg', 'building.jpg'. The output would be as follows:

**Image**: street.jpg

**Caption**: a person walking a dog on a street

**Confidence**: 0.46

---

**Image**: person.jpg

**Caption**: a man wearing glasses

**Confidence**: 0.46

---

**Image**: building.jpg

**Caption**: a large white building with a dome and a green lawn in front with United States Capitol in the background

**Confidence**: 0.46
