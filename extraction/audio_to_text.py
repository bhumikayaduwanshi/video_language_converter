import speech_recognition as sr


def audio_to_text(audio_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    try:
        with sr.AudioFile(audio_file_path) as source:
            # Record the entire audio file
            audio_data = recognizer.record(source)

        # Use Google Web Speech API to recognize the text
        text = recognizer.recognize_google(audio_data)

    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

    return text
