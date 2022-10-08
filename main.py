from API import api
from Repository import repository

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
            case 'exit':
                api.exit()
                exit = True
