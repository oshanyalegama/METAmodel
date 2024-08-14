from pydub import AudioSegment

def extract_audio_segment(input_file, start_time, end_time, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    
    # Convert start and end time to milliseconds
    start_time_ms = start_time * 1000
    end_time_ms = end_time * 1000
    
    # Extract the segment
    extracted_segment = audio[start_time_ms:end_time_ms]
    
    # Export the segment
    extracted_segment.export(output_file, format="wav")

# Example usage
input_file = "mix.wav"
start_time =  3 # Start at 30 seconds
end_time = 7.6335    # End at 60 seconds
output_file = "output.wav"

extract_audio_segment(input_file, start_time, end_time, output_file)
