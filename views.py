import os
from django.shortcuts import render
from django.conf import settings
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np

# Ensure this path is correct
model_path = 'dl_model\model1.h5'
print(f"Model path: {model_path}")

model = load_model(model_path)
labels = {0: 'Healthy', 1: 'Powdery', 2: 'Rust'}
threshold = 0.5

def get_result(image_path):
    img = load_img(image_path, target_size=(225, 225))
    x = img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x, verbose=0)[0]
    max_prob = np.max(predictions)
    class_idx = np.argmax(predictions)
    if max_prob < threshold:
        return 'This image is not related. Please try again.'
    return labels[class_idx]

def dl_model(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return render(request, 'disease_detection.html', {'error': 'No file part'})
        f = request.FILES['file']
        if f.name == '':
            return render(request, 'disease_detection.html', {'error': 'No selected file'})

        # Define file path and save file
        file_path = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(file_path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        # Get prediction
        try:
            prediction = get_result(file_path)
        except Exception as e:
            return render(request, 'disease_detection.html', {'error': str(e)})

        return render(request, 'disease_detection.html', {'result': prediction})

    return render(request, 'disease_detection.html')
