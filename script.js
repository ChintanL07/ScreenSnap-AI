// Existing code for generating instructions on button click
document.getElementById('generate').addEventListener('click', function() {
  const context = document.getElementById('context').value;
  const screenshots = document.getElementById('screenshots').files;

  if (screenshots.length === 0) {
    alert('Please upload at least one screenshot.');
    return;
  }

  const output = document.getElementById('output');
  output.innerHTML = "Processing...";

  // Create FormData to send images and context
  const formData = new FormData();
  formData.append('context', context);
  
  // Append each screenshot to the FormData object
  for (let i = 0; i < screenshots.length; i++) {
    formData.append('screenshots', screenshots[i]);
  }

  // Send the form data to the back-end using fetch
  fetch('http://127.0.0.1:5000/generate-instructions', {
    method: 'POST',
    body: formData,
  })
  .then(response => response.json())
  .then(data => {
    if (data.instructions) {
      output.innerHTML = data.instructions;
    } else {
      output.innerHTML = "Error: " + data.error;
    }
  })
  .catch(error => {
    output.innerHTML = "An error occurred: " + error;
  });
});

// New code to display uploaded file names
document.getElementById('screenshots').addEventListener('change', function () {
  const fileInput = document.getElementById('screenshots');
  const fileNamesDiv = document.getElementById('file-names');
  fileNamesDiv.innerHTML = ''; // Clear previous names

  for (let i = 0; i < fileInput.files.length; i++) {
    const fileName = document.createElement('p');
    fileName.textContent = fileInput.files[i].name;
    fileNamesDiv.appendChild(fileName); // Display file names
  }
});
