# Mashup Generator: Extract Audio from YouTube Videos

This is a simple Streamlit web application that allows users to extract audio from YouTube videos and create mashups. The app uses the `youtube_dl` and `moviepy` libraries to download YouTube videos' audio and process them.

## Features

- Input the name of a singer.
- Specify the number of YouTube videos to download audio from.
- Set the desired duration for each audio clip.
- Enter the desired output audio file name.
- Click the "Extract Audio" button to create the audio mashup.
- A success message will be displayed upon successful audio extraction.

## Installation and Usage

1. **Install Dependencies**: Before running the app, make sure you have the necessary Python libraries installed. You can install them using the following command:

   ```bash
   pip install youtube_dl moviepy streamlit
2. **Run the Streamlit App**: Run the Streamlit app by executing the following command in your terminal( Replace app.py with the actual name of your Python script.):

   ```bash
   streamlit run app.py
3. **Interact with the App**: Once the app is running, open a web browser and navigate to the URL provided in the terminal (usually http://localhost:8501). You will be able to interact with the app's user interface.
4. **Input Information**:  Input the singer's name, the number of videos to download audio from, the desired audio duration, and the output file name.
5. **Extract Audio**: Click the "Extract Audio" button to initiate the audio extraction process. The app will download the audio from the specified number of YouTube videos and create a mashup audio file.

**<p align= "center">Made with ❤️ by Pranvee</p>**


