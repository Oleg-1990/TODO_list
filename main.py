from API import api


if __name__ == '__main__':
    api = api.Api()
    exit = False
    print('Hello! \nIt`s a TODO list')
    while not exit:
        print('Please enter the task or use help(command "help")')
        user_command = input().strip()
        match user_command:
            case 'help':
                api.help()
            case 'add':
                api.add()
            case 'list':
                api.list()
            case 'completed':
                api.completed()
            case 'canceled':
                api.canceled()
            case 'remove':
                api.remove()
            case 'remove_all':
                api.remove_all()
            case 'exit':
                exit = api.exit()
