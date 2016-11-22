import sys

from transitions import Machine
## pip install transitions

class Scanner(object):

    # states: state machine names
    # reserved: list of reserved words

    states=['START','INNUM','INID','INASSIGN','DONE']
    accepted_state='DONE'
    reserved=['if','then','else','end','repeat','until',
		'read','write','break','for','while',
		'int','float','char','bool','void','main',
		'return', 'endl', 'cout']

    def __init__(self,s):
        # ':' ---> __
        # '=' ---> ___
        self.machine=Machine(model=self,states=Scanner.states
                             ,initial='START')
        self.machine.add_transition('digit','START','INNUM')
        self.machine.add_transition('letter','START','INID')
        self.machine.add_transition('__','START','INASSIGN')
        self.machine.add_transition('other','START','DONE')
        self.machine.add_transition('digit','INNUM','INNUM')
        self.machine.add_transition('other','INNUM','DONE')
        self.machine.add_transition('letter','INID','INID')
        self.machine.add_transition('other','INID','DONE')
        self.machine.add_transition('___','INASSIGN','DONE')
        self.machine.add_transition('other', 'INASSIGN','DONE')
        self.input_string=s
        self.tokens={}              # final output dictionary.
        self.previous_state=None    # previous state in state machine.

    def isaccepted(self):
        ## Check if reached the last state "Done".
        if Scanner.accepted_state == self.state :
            return True
        else:
            return False

    def reset(self):
        ## Reset the current state and previous state.
        self.machine.set_state('START')
        self.previous_state=None


    def character_type(self,c):
        # identify the type of each character in input_string.
        if c.isdigit():
            return 'digit'
        elif c.isalpha():
            return 'letter'
        elif c==':':
            return ':'
        elif c=='=':
            return '='
        else:
            return 'other'

    def run_(self):

        	########### Main Algorithm ###########.

        character='' ## for concatenation of same type characters
        i=0 ## for itteration over input_string

        while i<len(self.input_string):
            try:
                transition=self.character_type(self.input_string[i])
                if transition == 'digit':
                    self.previous_state=self.state
                    self.digit()
                    character = character + self.input_string[i]
                    i=i+1
                elif transition == 'letter':
                    self.previous_state = self.state
                    self.letter()
                    character = character + self.input_string[i]
                    i=i+1
                elif transition == ':':
                    self.previous_state = self.state
                    self.__()
                    character = character + self.input_string[i]
                    i=i+1
                elif transition == '=':
                    self.previous_state = self.state
                    self.___()
                    character = character + self.input_string[i]
                    i=i+1
                elif transition == 'other':
                    self.previous_state = self.state
                    self.other()
            except:
                self.previous_state = self.state
                self.other()
            if self.isaccepted():
                if(self.previous_state == 'INNUM'):
                    self.tokens.update({character:'Number'})
                    character=''
                elif(self.previous_state == 'INID'):
                    self.tokens.update({character:'Identifier'})
                    character = ''
                elif (self.previous_state == 'INASSIGN'):
                    self.tokens.update({character:'SS'})
                    character = ''
                elif (self.previous_state == 'START'):
                    character=self.input_string[i]
                    self.tokens.update({character:'SS'})
                    character = ''
                    i=i+1
                self.reset()

    def print_tokens(self):
        print self.tokens


    def handle_reserved(self):
        for key in self.tokens:
            for j in Scanner.reserved:
                if key==j:
                    self.tokens.update({key:'reserved'})
                    break

    def exec_(self):
        self.run_()
        self.handle_reserved()
        #self.print_tokens()

    def return_token(self):
	return self.tokens


if __name__=="__main__":
	a=''
	b=''
	try:
		a=sys.argv[1]
		b=sys.argv[2]
	except:
		print 'ERROR*:'
		print '--> Enter Input.txt/Output.txt file(s) path.'
		print '--> Example: python scanner.py input.txt output.txt'
		sys.exit()

	input_file=open(a,'r')
	output_file=open(b,'r+')
	strr=input_file.read()
	s=Scanner(strr)
	s.exec_()
	tokens=s.return_token()

	for key in (tokens):
		if(key.isspace()):
			continue
		output_file.write(key)
		output_file.write(' -----> ')
		output_file.write(str(tokens[key]))
		output_file.write("\n")
	output_file.close()
