import streamlit as st
from PIL import Image
import requests

# Define the main function that Streamlit will run
def main():
    st.title("GreenScore: AI-Powered Sustainability Insight")
    st.write("Upload an image of a product for analysis:")

    # Upload image
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png"])

    if uploaded_image is not None:
        # Load the uploaded image into a PIL image
        image = Image.open(uploaded_image)

        # Display the uploaded image
        st.image(image, caption="Uploaded image", use_column_width=True)

        # Process the image with your Hugging Face model
        # (This is just a placeholder, you'll need to replace it with the actual model processing code)
        response = analyze_image(uploaded_image)

        # Display the analysis results
        st.write("Analysis results:")
        st.write(response)

# Define the function that sends the image to the Hugging Face model and returns the analysis results
def analyze_image(image):
    MODEL_URL = "https://huggingface.co/your-model"
    response = requests.post(MODEL_URL, files={"image": image.getvalue()})
    result = response.json()
    return result

# Run the main function
if __name__ == "__main__":
    main()
