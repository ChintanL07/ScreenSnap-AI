# ScreenSnap AI 

This project is a web application that allows users to upload screenshots and generate image descriptions using a model. It is built using Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Features
- Upload multiple screenshots
- Generate image descriptions using the BLIP model from Hugging Face
- Simple UI with file upload and instructions generation
- Optional context input to enhance descriptions.

## Technologies Used
- Flask (Python)
- JavaScript (for front-end interactions)
- BLIP model (for image description generation)
- HTML5/CSS3 (for front-end design)

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Basic knowledge of Flask and web development.
- An IDE or text editor for editing the code.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 2. Install Dependencies

Make sure you have Python and Flask installed. You can create a virtual environment and install the required dependencies.

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install flask torch transformers pillow
```

### 3. Run the Application

Start the Flask app:

```bash
python app.py
```

The application will run at `http://127.0.0.1:5000`.

### 4. How to Use

1. Open the web application in your browser.
2. Upload screenshots using the "Upload Screenshots" button.
3. Optionally, add context in the "Optional Context" field.
4. Click "Describe Image" to generate descriptions based on the screenshots.

### 5. API Endpoints

- **POST `/generate-instructions`**: This endpoint accepts uploaded screenshots and context. It returns the generated image descriptions.

#### Request Format

- **Form Data**:
  - `context` (string): Optional text to provide context.
  - `screenshots` (file): The images to be processed.

#### Response Format

- **Success**: Returns a JSON object containing the generated instructions.
- **Error**: Returns a JSON object with error messages.

### 6. Example Usage

Here’s an example of how to use the API with cURL:

```bash
curl -X POST -F 'context=Your context here' -F 'screenshots=@path_to_your_image.png' http://127.0.0.1:5000/generate-instructions
```

## Contribution Guidelines

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (e.g., `feature/YourFeature`).
3. Make your changes and commit them.
4. Push to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the MIT License. Feel free to modify and distribute as needed.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the BLIP model.
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework.

## Contact

If you have any questions or feedback, please reach out to me at b22me036@iitj.ac.in.
```

### Key Additions:
- **Prerequisites**: List any requirements that need to be fulfilled before running the project.
- **API Endpoints**: Description of the main API endpoint(s), including request and response formats.
- **Example Usage**: How to use the API with an example.
- **Contribution Guidelines**: Instructions for others who want to contribute to your project.
- **Contact Information**: A way for others to reach you for questions or feedback.

Feel free to modify it further based on your specific project needs! Let me know if you have any more adjustments or if you need further assistance.
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
