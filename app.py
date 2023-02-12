import sys
import youtube_dl
import moviepy.editor as mp
import os

import streamlit as st
st.set_page_config(page_title="Extracting audio from YouTube videos",
                   page_icon=":musical_note:",
                   layout="centered")

st.markdown("<h1 style='text-align: center; color: gray;'>Mashup Generator</h1>", unsafe_allow_html=True)





def extract_audio(singer_name, num_of_videos, audio_duration, output_file_name):
    youtube_dl_options = {
        "default_search": "ytsearch",
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": "%(id)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }
    num_of_videos = int(num_of_videos)
    with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
        result = ydl.extract_info(f"{singer_name} audio", False)
        videos = result["entries"]

    clips = []
    for video in videos[:num_of_videos]:
        clip = mp.VideoFileClip(video["id"] + ".mp3")
        clip = clip.subclip(0, audio_duration)
        clips.append(clip)

    final_audio = mp.concatenate_audioclips(clips)
    final_audio.write_audiofile(output_file_name)

if __name__ == "__main__":

    singer_name = st.text_input("Enter Singer Name:")
    num_of_videos = int(st.number_input("Enter Number of Videos:"))
    audio_duration = int(st.number_input("Enter Audio Duration (in seconds):"))
    output_file_name = st.text_input("Enter Output File Name:")

    if st.button("Extract Audio"):
        extract_audio(singer_name, num_of_videos, audio_duration, output_file_name)
        st.success("Audio Extracted Successfully")

st.markdown("---")
st.markdown("<center>Made with ❤️ by Pranvee Vashisht</center>", unsafe_allow_html=True)

