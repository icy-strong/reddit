from operator import sub
from tkinter import font
import moviepy.editor as mp


#generates a video based off still image and audio, with subtitles
class vid:
    #make audio length in seconds
    def __init__(self, wpm, imgs = ['stock.jpg']):
        self.audioLength = None
        self.v = None
        self.imgs = imgs
        self.wmp = wpm
        self.clips=[]
        self.finalVid = None
    
    #takes the audio and image, then combines them to make a video
    def genV(self):
    
        audio_clip = mp.AudioFileClip('audio.mp3')
        image_clip = mp.ImageClip('stock.jpg')
        video_clip = image_clip.set_audio(audio_clip)
        video_clip.duration = audio_clip.duration
        video_clip.fps = 15
        #video_clip.write_videofile('noSubtitles.mp4')
        self.audioLength = audio_clip.duration
        self.v=video_clip

    #makes the clips in sections of how long the user specifies in LEN_CLIPS, and adds
    #the amount of words based off the wpm count of video, and length of clips
    def makeClips(self):
        LEN_CLIPS=25
        numClips = int(self.audioLength/LEN_CLIPS)
        endLoop = numClips*LEN_CLIPS
        excess = self.audioLength-(numClips*LEN_CLIPS)
        wpc = int(self.wmp/(60/LEN_CLIPS))
        f = open('posts.txt','r')
        script=[word for line in f for word in line.split()]
        f.close()

        print('numClips:', numClips)
        print('len:',self.audioLength)

        for i in range(0, numClips, 1):
            cStart = i*LEN_CLIPS
            clip = self.v.subclip(cStart,cStart+LEN_CLIPS+1)
    
            
            
            sStart = i*wpc
            subScr = ''
            numNewLines = 1
            
            for j in range(sStart, sStart+wpc, 1):
                
                subScr += script[j] + ' '
                if len(subScr)//numNewLines >=50:
                    subScr += '\n'
                    numNewLines+=1

            txt = mp.TextClip(subScr, color = 'white', fontsize = 25)
            txt = txt.set_position('center')
            finalC = mp.CompositeVideoClip([clip,txt])
            finalC.duration=LEN_CLIPS
            self.clips.append(finalC)


        subScr=''
        numNewLines=1
        clip = self.v.subclip(endLoop, self.audioLength)
        for i in range((numClips-1)*wpc, len(script),1):
             subScr += script[i] + ' '
             if len(subScr)//numNewLines >=50:
                    subScr += '\n'
                    numNewLines+=1

        txt = mp.TextClip(subScr, color = 'white', fontsize=25 )
        txt = txt.set_position('center')
        finalC = mp.CompositeVideoClip([clip,txt])
        finalC.duration = excess
        self.clips.append(finalC)    


    #takes all of the clips and combines them to make one full video
    def group(self):
        self.finalVid = mp.concatenate_videoclips(self.clips)
        self.finalVid.write_videofile('vi.mp4')
        





