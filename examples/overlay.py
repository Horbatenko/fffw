from fffw.encoding import *

ff = FFMPEG()

source = ff < input_file('input.mp4')
logo = ff < input_file('logo.png')

# pass first video stream (from source input file) as bottom
# layer to overlay filter.
overlay = ff.video | Overlay(x=1720, y=100)
# scale logo to 100x100 and pass as top layer to overlay filter
logo | Scale(width=100, height=100) | overlay

# tell ffmpeg that it'll output something to destination file
output = ff > output_file('output.mp4')
# output video with logo to destination file
overlay > output
