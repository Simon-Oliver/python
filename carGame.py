help_msg = '''
start - to start the car
stop - to stop the car
quit - to exit the game
'''
is_playing = True

while is_playing:
    command = input('> ').lower()
    if command == 'help':
        print(help_msg)
    elif command == 'start':
        print('Car started!')
    elif command == 'stop':
        print('Car stopped!')
    elif command == 'quit':
        print('Quiting Game')
        is_playing = False
        break
    else:
        print('Not a valid command! Type help for command list.')
