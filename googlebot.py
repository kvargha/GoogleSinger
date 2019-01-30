from google.cloud import texttospeech
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
from google.oauth2 import service_account

def constructMP3(lyrics, songName):
    credentials = service_account.Credentials.from_service_account_file("GoogleKeys.json")
    
    # Instantiates a client
    client = texttospeech.TextToSpeechClient(credentials = credentials)
    
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text = lyrics)
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
    
    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    
    # The response's audio_content is binary.
    with open(os.path.join('Output', songName + '.mp3'), 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file ' + songName + '.mp3')
        
     