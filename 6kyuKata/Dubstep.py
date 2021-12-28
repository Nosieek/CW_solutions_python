import re
def song_decoder(song):
    return ' '.join(re.sub('WUB', ' ', song).strip(' ').split())
print(song_decoder('AWUBWUBWUBBWUBWUBWUBC'))