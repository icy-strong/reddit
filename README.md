# Reddit Video Generator
### Description
Have you ever seen videos of a still image, overlayed with a robot voice reading content farmed from a public form, and thought "wow, this is such easy content! Anyone could do it"?

Well now, even a robot can!

This program uses the praw api to get reddit posts, then uses the python tts library to read it out loud over a still image with the text overlayed.

### Known Issues
Currently, the program uses the average wpm of the tts audio, and generates a list of clips of user provided length. It decides how many words to put on each clip from the wpm and length of clips, but because the wpm isn't consitant, the video ends up being slightly behind, and this problem compounds over time.

I will fix this by instead generating the audio clips based off a fixed number of words, and make the clips however long the generated audio for it is. This is somewhat worrying because I fear it will greatly increase the runtime of the program.
