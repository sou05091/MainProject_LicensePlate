document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('result');

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    resultDiv.innerHTML = '<p>Uploading and predicting...</p>';

    try {
        const response = await fetch('/', {
            method: 'POST',
            body: formData,
        });
        const imgUrl = await response.url;
        resultDiv.innerHTML = `<p>Prediction Result:</p><img src="${imgUrl}" alt="Prediction Result">`;
    } catch (error) {
        console.error('Error:', error);
        resultDiv.innerHTML = '<p>Error occurred. Please try again.</p>';
    }
});