# Import necessary modules
from PIL import Image
from urllib.request import urlopen
from exit import exit
from allText import *  # Assuming allText contains necessary text constants
from imageTypeConverter import image_type_Converter
from imageResizer import image_Resizer
from fetures import print_imgInfo

# Display a header for the Image Size Compressor
print("*****Image Size Compressor*****")

# Dictionary containing available services
serviceDict = {
    'imgTypeConvert': "Image Type Conversion (PNG --> JPG / JPG --> PNG)",
    'imgSizeCompressor': "Image Size Compressor",
    'imgFilter': "Image Filtering"
}

def main():
    # Get user input for the image file path / address / URL
    imagePath = str(input("Enter the image-file path / address / URL:").rstrip())
    
    # Determine if the image is from a file path or URL, and retrieve the image
    img = img_from_file_path(imagePath) if not imagePath.startswith('http') else img_from_http_request(imagePath)
    
    # Display information about the original image
    print_imgInfo('Actual image details', img)
    
    # Select a service from the available options
    serviceSelected = select_Service()
    
    # Display the selected service
    print(f"{outPutstr}SELECTED SERVICE:", end="")
    
    # Use a match statement to perform actions based on the selected service
    match serviceSelected:
        case 1:
            print(f"{serviceDict['imgTypeConvert']}")
            image_type_Converter(img)
        case 2:
            print(f"{serviceDict['imgSizeCompressor']}")
            image_Resizer(img)
        case 3:
            print(f"{serviceDict['imgFilter']}")
        case _:
            print(f"{errorText}No service selected")
            exit(main)
    
    # Exit the program
    exit(main)

def select_Service():
    # Initialize a counter for displaying service options
    count = 1
    
    # Display available services and prompt the user to select one
    print(f"\nSELECT ONE SERVICE")
    for service in serviceDict:
        print(f"{count}.{serviceDict[service]}")
        count += 1
    
    try:
        # Get user input for the selected service
        selectService = int(input("Select service:"))
    except TypeError:
        print(f"{errorText}Invalid input")
    else:
        # Check if the selected service is within the valid range
        if selectService not in range(1, 4):
            print(f"{errorText} No service available")
            # Recursively call select_Service if the input is invalid
            select_Service()
        else:
            # Return the selected service
            return selectService

def img_from_http_request(URL):
    try:
        # Attempt to open and return the image from the provided URL
        return Image.open(urlopen(URL))
    except ConnectionError:
        print(f"{errorText}Connection failed!!! Check your internet connectivity")
    except OSError:
        print(f"{errorText}Image not found")
        exit(main)

def img_from_file_path(file_path):
    try:
        # Attempt to open and return the image from the provided file path
        return Image.open(file_path)
    except OSError:
        print(f"{errorText}Image not found")
        exit(main)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
