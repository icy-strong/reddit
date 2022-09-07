import moviepy.editor as mp
import pyttsx3 as ptts
import time as t
import shutil
import os


#generates a video based off still image and audio, with subtitles
class vid:
    #make audio length in seconds
    def __init__(self, wpm, imgs = ['stock.jpg']):
        self.audioLength = None
        self.v = None
        self.imgs = imgs
        self.imageClip = image_clip = mp.ImageClip('stock.jpg')
        self.wmp = wpm
        self.clips=[]
        self.finalVid = None
    


    #makes the clips in sections of how many words the user wants per clip of video
    def makeClips(self, wpc=None):
        if wpc == None:
            wpc = self.wmp//2

      
        os.makedirs('clips',exist_ok=True)
        
        
        f = open('posts.txt','r+')
        script=[word for line in f for word in line.split()]
        f.close()

        f= open('posts.txt','r')
        rawScript = f.read()
        f.close()

        numClips = int(len(script)/wpc)
        endLoop = wpc*numClips
        extra = len(script)-endLoop
       

        scriptSLen =0
        scriptFLen=0
        engine=ptts.init()
        engine.setProperty('rate', self.wmp)

        for i in range(0, numClips, 1):

            sStart = i*wpc
            subScr = ''
            numNewLines = 1
            
            for j in range(sStart, sStart+wpc, 1):
                
                subScr += script[j] + ' '
                scriptFLen += len(script[j])+1
                
                if len(subScr)//numNewLines >=50:
                    subScr += '\n'
                    numNewLines+=1

            
            filePath = './clips/clip'+str(i)+'.mp3'
            engine.save_to_file(rawScript[scriptSLen:scriptFLen], filePath)
            scriptSLen=scriptFLen+1
            engine.runAndWait()

            audio_clip = mp.AudioFileClip(filePath)
            clip = self.imageClip.set_audio(audio_clip)

            
            txt = mp.TextClip(subScr, color = 'white', fontsize = 25)
            txt = txt.set_position('center')
            finalC = mp.CompositeVideoClip([clip,txt])
            finalC.duration= audio_clip.duration
            finalC.fps = 30
            self.clips.append(finalC)


        subScr=''
        numNewLines=1
        
        for i in range(endLoop+1, len(script),1):
            subScr += script[i] + ' '
            if len(subScr)//numNewLines >=50:
                   subScr += '\n'
                   numNewLines+=1

        filePath = './clips/clip'+str(endLoop+1)+'.mp3'
        engine.save_to_file(subScr, filePath)
        engine.runAndWait()

        audio_clip = mp.AudioFileClip(filePath)
            

        clip = self.imageClip.set_audio(audio_clip)
        

        txt = mp.TextClip(subScr, color = 'white', fontsize=25 )
        txt = txt.set_position('center')
        finalC = mp.CompositeVideoClip([clip,txt])
        finalC.duration = audio_clip.duration
        finalC.fps = 30
        self.clips.append(finalC)    

        


    #takes all of the clips and combines them to make one full video
    def group(self):
        self.finalVid = mp.concatenate_videoclips(self.clips)
        self.finalVid.write_videofile('vi.mp4')
        





