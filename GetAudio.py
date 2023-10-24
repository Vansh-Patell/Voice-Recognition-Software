import pyaudio

# Create an instance of the PyAudio class
p = pyaudio.PyAudio()

# Open a streaming stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

print("Recording Audio...")

# Start capturing audio
while True:
    data = stream.read(1024)  # Adjust the buffer size as needed
    # Process the audio here

# Close the stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()
