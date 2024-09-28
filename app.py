from flask import Flask, request, jsonify
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io
import logging

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the BLIP model and processor from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)


# Route to handle the POST request from the front-end
@app.route('/generate-instructions', methods=['POST'])
def generate_instructions():
    try:
        # Log the form data to check if images are being received
        context = request.form.get('context', '')
        screenshots = request.files.getlist('screenshots')
        
        # Log how many screenshots have been uploaded
        print(f"Received {len(screenshots)} screenshots")
        
        if not screenshots:
            return jsonify({'error': 'No screenshots uploaded.'}), 400

        # Process the images as before
        captions = []
        for screenshot in screenshots:
            image = Image.open(screenshot)
            logging.info(f'Processing image: {screenshot.filename}')
            
            # Convert image to BLIP processor format and generate caption
            inputs = processor(images=image, return_tensors="pt").to(device)
            output = model.generate(**inputs)
            caption = processor.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
            logging.info(f'Generated caption: {caption}')
            captions.append(caption)

        # Combine captions and context to form testing instructions
        response = generate_test_instructions(captions, context)
        
        # Return the generated instructions
        return jsonify({'instructions': response}), 200
    
    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return jsonify({'error': str(e)}), 500


# Function to generate testing instructions based on image captions and context
def generate_test_instructions(captions, context):
    # Simple strategy to generate test cases from captions
    test_cases = f"Context: {context}\n\n"
    for caption in captions:
        # test_cases += f"Test Case {i}:\n"
        test_cases += f"{caption}\n"
        # test_cases += f"Pre-conditions: Ensure the app is at the correct screen for this test.\n"
        # test_cases += f"Testing Steps: Follow the image's functionality as described in the caption.\n"
        # test_cases += f"Expected Result: The functionality described should work as intended.\n\n"
    return test_cases

if __name__ == '__main__':
    app.run(debug=True)
