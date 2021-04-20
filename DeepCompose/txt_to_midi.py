import midi
import os
from random import randint
from numpy import inf

class NoteEvent():
    def __init__(self, time, val, on):
        self.time = time
        self.val = val
        self.on = on

names = os.listdir('./texts')
name = names[randint(0, len(names)-1)]
print name
        
#with open('data/classical/txt/' + name, 'rb') as f:
with open('./texts/eighthGenerated.txt', 'rb') as f:
    song_txt = f.read()

# print song_txt

pattern = midi.Pattern()
track = midi.Track()
pattern.append(track)
song_txt = song_txt.split('\n')
song_txt.pop()
counter = 0
for song_txt2 in song_txt:
    split_song = song_txt2.replace('\r', '').split(' ')

    events_to_sort = []
    time = 0
    tempo = 40
    val = 64
    # print(split_song)
    lowest2 = inf
    highest2 = 0 - inf
    lowest = 0
    highest = 127
    for time_event in split_song:
        delta_val, dur = time_event.split(',')
        delta_val = int(delta_val)
        val += delta_val
        if val < lowest:
            lowest = val
        if val < lowest2:
            lowest2 = val
        if val > highest:
            highest = val
        if val > highest2:
            highest2 = val
    field = highest2 - lowest2
    if field > 127:
        print('Invalid File Input, range:', field)
        break
    # Changes key to fit the midi range [0, 127]
    val = 64 - lowest + (127 - highest)
    for time_event in split_song:
        events = time_event.split('/')

        min_dur = 0
        for event in events:
            # print(event)
            delta_val, dur = event.split(',')
            delta_val = int(delta_val)
            dur = int(dur)

            val += delta_val
            print(val)
            
            # dur is inverse of duration...
            if dur > min_dur:
                min_dur = dur

            events_to_sort.append(NoteEvent(time, val, True))
            events_to_sort.append(NoteEvent(time + 16 / float(dur) * tempo, val, False))

        time = time + 16 / float(min_dur) * tempo

    sorted_events = sorted(events_to_sort, key=lambda x: x.time)

    track.append(midi.NoteOnEvent(tick=0, velocity=70, pitch=sorted_events[0].val))

    for idx in range(1,len(sorted_events)):
        evt = sorted_events[idx]
        prev_evt = sorted_events[idx-1]
        tick = int(evt.time - prev_evt.time)
        pitch = int(evt.val)

        if evt.on:
            velocity = 70
        else:
            velocity = 0

        mid_evt = midi.NoteOnEvent(tick=tick, velocity=velocity, pitch=pitch)
        track.append(mid_evt)

    counter += 1
    print(str(counter) + '/' + str(len(song_txt)))

track.append(midi.EndOfTrackEvent(tick=1))

midi.write_midifile("./generated/numbaEight.mid", pattern)

