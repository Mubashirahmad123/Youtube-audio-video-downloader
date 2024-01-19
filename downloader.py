from pytube import YouTube
check=input("What do you want to download, Press 1 for video and 2 for audio: ")

if check == "1":

# Prompt the user for a YouTube video URL
  link = input("Please provide the link: ")
  youtube_1 = YouTube(link)

# Filter for progressive video streams
  videos = youtube_1.streams.filter(progressive=True)

# List and enumerate the available video streams
  vid_list = list(enumerate(videos))
  for i, vid in vid_list:
    print(i, ":", vid)

# Prompt the user to select a video stream
  strm = int(input("Please provide the index of the video stream you want to download: "))

# Download the selected video stream
  videos[strm].download()
  print("Video downloaded successfully")

elif check == "2":
  # Prompt the user for a YouTube video URL
    link = input("Please provide the link: ")
    youtube_2 = YouTube(link)
    audio = youtube_2.streams.filter(only_audio=True)

    # List and enumerate the available audio streams
    aud_list = list(enumerate(audio))
    for i, aud in aud_list:
        print(i, ":", aud)

    # Prompt the user to select an audio stream
    strm2 = int(input("Please provide the index of the audio stream you want to download: "))

    # Download the selected audio stream
    audio[strm2].download()
    print("Audio downloaded successfully!")
  

    



