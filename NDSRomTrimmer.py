import sys

# Fixing Python 2 compatibility
if(sys.version_info.major < (3)):
	input = raw_input

# Getting the rom name
file = input('Enter your rom file or Drag/Drop it here:\n> ')

# Removing \ on non windows systems
if sys.platform != 'win32':
	while file.find('\\') != -1:
		bkslsh = file.find('\\')
		fileCopy = file
		fileCopy = file[:bkslsh]
		fileCopy += file[bkslsh+1:]
		file = fileCopy
# Removing spaces from end of file names (Mac puts them on drag/drop)
if file[-1:] == ' ':
	file = file[:-1]
# Removing " from file names (Windows puts them on drag/drop)
if file[:1] == '"':
	file = file[1:]
if file[-1:] == '"':
	file = file[:-1]

# Opening the rom
romFile = open(file, 'rb')
rom = romFile.read()

print('Trimming', end='', flush=True)

# Trimming the rom
while rom[-10000000:-1] == (b'\xff'*9999999):
	rom = rom[:-10000000]
	print('.', end='', flush=True)
while rom[-1000000:-1] == (b'\xff'*999999):
	rom = rom[:-1000000]
	print('.', end='', flush=True)
while rom[-100000:-1] == (b'\xff'*99999):
	rom = rom[:-100000]
	print('.', end='', flush=True)
while rom[-10000:-1] == (b'\xff'*9999):
	rom = rom[:-10000]
	print('.', end='', flush=True)
while rom[-1000:-1] == (b'\xff'*999):
	rom = rom[:-1000]
	print('.', end='', flush=True)
while rom[-100:-1] == (b'\xff'*99):
	rom = rom[:-100]
	print('.', end='', flush=True)
while rom[-10:-1] == (b'\xff'*9):
	rom = rom[:-10]
	print('.', end='', flush=True)
while rom[-1] == 255:
	rom = rom[:-1]
	print('.', end='', flush=True)

print('\nSaving...')

# Saving the new rom
ouputFile = open(file[:-4] + ' - trimmed.nds', 'wb')
ouputFile.write(rom)
ouputFile.close()

print('\nDone! Trimmed rom saved as:\n"' + file[:-4] + ' - trimmed.nds"')
