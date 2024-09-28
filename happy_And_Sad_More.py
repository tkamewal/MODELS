# Load the model
model = tf.keras.models.load_model("happy_And_Sad_More.keras")

image_H = "256"
image_W = "256"

# Load the image
img_path = r"C:\Users\tanma\Pictures\happy.jpg"
img = image.load_img(img_path,target_size=(int(image_H), int(image_W)))  # Use the same height and width as in your model

# Convert the image to an array
img_array = image.img_to_array(img)

# Rescale pixel values if necessary (usually you need to divide by 255 if the model was trained on normalized images)
img_array = img_array / 255.0

# Expand the dimensions to match the input shape of the model (add a batch dimension)
img_array = np.expand_dims(img_array, axis=0)

# Predict the class of the image
prediction = model.predict(img_array)
