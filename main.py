class Scale(object):
    '''
    An object for scale objects.

    e.g.
    key = 'Ab'

    tonality can be one of 
        - 'major', 
        - 'minor', 
        - 'whole_tone', 
        - 'chromatic'
    
    articulartion is 
        - legato
        - staccato

    apart will be one from
        - '8' (Octave apart)
        - '6' (Major 6th apart)
        - '3' (3rd apart)

    scale_in 
        - None
        - '3' (in 3rds)
        - '6' (in 6ths)

    Tempo - int value for bpm

    hands
        - together
        - separate

    motion
        - 'contrary' (Contrary motion)
        - 'similar' (Similar motion)
    
    starting_on is the first note of the scale. Default being the tonal

    '''

    def __init__(self, 
            key, 
            tonality = 'major', 
            articulation = 'legato', 
            apart = '8',
            scale_in = '', 
            motion = 'similar', 
            tempo = 88, 
            hands = 'together',
            starting_on = None
        ):
        self.key = key
        self.tonality = tonality
        self.articulation = articulation
        self.apart = get_hands_apart(apart)
        self.scale_in = get_scale_in(scale_in)
        self.motion = motion
        self.tempo = tempo
        self.hands = hands
        self.starting_on = starting_on if starting_on else self.key

    def print(self):

        print('Scales %s(%s motion) %s %s %s, %s, hands %s, starting on %s' 
        % (self.apart, 
            self.motion, 
            self.scale_in, 
            self.key, 
            self.tonality,
            self.articulation, 
            self.hands,
            self.starting_on)
        )


def get_hands_apart(apart):
    if apart == '8':
        return ''
    elif apart == '6':
        return 'major 6th apart '
    elif apart == '3':
        return 'major 3rd apart '

def get_scale_in(scale_in):
    if scale_in == '':
        return ''
    elif scale_in == '3':
        return 'in 3rds'
    elif scale_in == '6':
        return 'in 6ths'


class Appergio(object):

    '''
    A class for appergio classes

    key = 'Ab'
    
    tonality can be one of 
        - 'major', 
        - 'minor', 
        - 'dominant7', (dominant 7th, in the key specified)
        - 'diminished' (diminished 7th starting on 'key' note)
    '''

    def __init__(self, key, tonality = 'major'):

        self.key = key
        self.tonality = tonality

    def print(self):

        print(
            'Appergio %s %s' % (self.key, self.tonality)
        )


class Workout(object):
    '''
    Generates a list of randomly selected scales and appergios. 

    keys - a dictionary of keys
    '''

    def __init__(self, keys = {
        'C':{'tonality': ['major', 'minor']}, 
        'Eb':{'tonality': ['major', 'minor']}, 
        'F#':{'tonality': ['major', 'minor']}, 
        'A':{'tonality': ['major', 'minor']}
    }
        ):
        self.keys = keys

    def generate(self):

        for key in self.keys:
            # Scale(key).print()
            # print(key)
            for tonality in self.keys[key]['tonality']:

                Scale(key = key, tonality= tonality).print()
        


# Scale('C', motion='contrary').print()
# Scale('C', starting_on= 'Bb').print()
# Scale('C', apart='6').print()
# Scale('C', starting_on= 'Bb').print()
# Scale('Eb', scale_in = '3').print()
# Scale('Eb', scale_in = '6', articulation='staccato', hands = 'separate').print()
# Appergio('F#').print()
# Appergio('F#', tonality='dominant7').print()

Workout().generate()