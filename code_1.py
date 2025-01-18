from moviepy.editor import VideoFileClip

def convert_video_to_wav(video_path, output_wav_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_path = output_wav_path\
            .replace(".wav", "_temp_audio.mp3")
        video_clip.audio.write_audiofile(audio_path)
        
        print(f"Audio extracted to {audio_path}")
        return audio_path
    
    except Exception as e:
        print(f"Error during audio extraction: {e}")
        return None


from pydub import AudioSegment

def resample_audio(input_audio_path, output_audio_path,\
        target_sample_rate=16000):
    try:
        audio = AudioSegment.from_file(input_audio_path)
        audio = audio.set_frame_rate(target_sample_rate)
        audio.export(output_audio_path, format="wav")
        
        print(f"Resampled audio saved to {output_audio_path}")
    except Exception as e:
        print(f"Error during audio resampling: {e}")
        
