help_msg = '''
start - to start the car
stop - to stop the car
quit - to exit the game
'''
is_playing = True
car_started = False

while is_playing:
    command = input('> ').lower()
    if command == 'help':
        print(help_msg)
    elif command == 'start':
        if car_started:
            print('Car is already started!')
        else:
            car_started = True
            print('Car started!')
    elif command == 'stop':
        if not car_started:
            print('Car is already stopped!')
        else:
            car_started = False
            print('Car stopped!')
    elif command == 'quit':
        print('Quiting Game')
        is_playing = False
        break
    else:
        print('Not a valid command! Type help for command list.')
