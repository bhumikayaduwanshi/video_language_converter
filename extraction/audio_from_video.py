from moviepy.editor import VideoFileClip


def audio_from_video(video_file_name, audio_file_name):
    # Create a video clip from the MP4 file
    video_clip = VideoFileClip(video_file_name)

    # Extract the audio
    audio_clip = video_clip.audio

    # Save the extracted audio to a file
    audio_clip.write_audiofile(audio_file_name)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()
