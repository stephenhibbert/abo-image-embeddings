from moviepy.editor import VideoFileClip

def convert_video_to_gif(video_path, gif_path, max_width=640):
    """
    Convert a video to a low-size GIF.

    Args:
    video_path (str): The path to the source video file.
    gif_path (str): The path to save the GIF file.
    max_width (int): The maximum width of the GIF. The height is adjusted accordingly to maintain aspect ratio.
    """
    # Load the video
    video = VideoFileClip(video_path)

    # Calculate new height to maintain aspect ratio
    aspect_ratio = video.size[1] / video.size[0]
    new_height = int(max_width * aspect_ratio)

    # Resize the video and write it as a GIF
    video.resize((max_width, new_height)).write_gif(gif_path, fps=10)  # fps can be adjusted for smoother animation

    print(f"GIF saved to {gif_path}")

# Example usage
video_path = 'tensorboard.mov'  # Replace with your video file path
gif_path = 'tensorboard.gif'  # Replace with your desired output GIF path
convert_video_to_gif(video_path, gif_path)
