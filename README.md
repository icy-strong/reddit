# Reddit Video Generator
### Description
Have you ever seen videos of a still image, overlayed with a robot voice reading content farmed from a public form, and thought "wow, this is such easy content! Anyone could do it"?

Well now, even a robot can!

This program uses the praw api to get reddit posts, then uses the python tts library to read it out loud over a still image with the text overlayed.

### Update!
The original version of this program is still avalible in another branch, but now instead of generating one big video, it is generated in sections as to keep the text and audio in sync. This hurts the runtime, but at this time I do not think there is a faster way to do it that is still reliable.
