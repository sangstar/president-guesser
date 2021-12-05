import numpy as np

def strip_tags_from_transcript(transcript):
    transcript = transcript.split("<p>")
    transcript = [text.replace("</p>, ","").replace("</p>","").replace("]","") for text in transcript][1:]
    return transcript

def get_outside_voices(stripped_transcript):
    outside_voices = []
    for text in stripped_transcript:
        #if "PRESIDENT:" in text.split(" "):
        for words in text.split(" "):
            if words.upper() == words and words[-1] == ":":
                if words != "PRESIDENT:":
                    outside_voices.append(words)
    outside_voices = list(set(outside_voices)) 
    return outside_voices 



def get_only_president_lines(stripped_transcript, outside_voices):
    spoken = []
    spoken.append(stripped_transcript[0])
    if "PRESIDENT:" in stripped_transcript[0].split(" "):
        for i in np.arange(1,len(stripped_transcript)):
            #print(i)
            if any([outside_voice in stripped_transcript[i].split(" ") for outside_voice in outside_voices]):
                #print(stripped_transcript[i])
                while "PRESIDENT:" not in stripped_transcript[i].split(" "):
                    i += 1
                    #print('looking for next president line... ', i)
                    #print(stripped_transcript[i])
            spoken.append(stripped_transcript[i])
    spoken = sorted(set(spoken), key=spoken.index) 
    return spoken  


def get_president_text(transcript):
    transcript = strip_tags_from_transcript(transcript)
    outside_voices = get_outside_voices(transcript)
    return get_only_president_lines(transcript, outside_voices)