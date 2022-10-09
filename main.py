from API import api

if __name__ == '__main__':

    api = api.Api()
    exit = False
    print('Hello! \nIt`s a TODO list')
    api.read_file()
    while not exit:
        print('Please enter the task or use help(command "help")')
        user_command = input().strip()
        match user_command:
            case 'help':
                api.help()
            case 'add':
                api.add()
            case 'add_few':
                api.add_a_few()
            case 'list':
                api.list()
            case 'completed':
                api.completed()
            case 'canceled':
                api.canceled()
            case 'find':
                api.find()
            case 'remove':
                api.remove()
            case 'remove_all':
                api.remove_all()
            case 'done_list':
                api.done_list()
            case 'exit':
                api.exit()
                exit = True
