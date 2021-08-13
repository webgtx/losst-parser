import func

url = 'https://losst.ru/'
counter = 1

while True:
    page_option = input('\n\nWelcome to my parser for losst\n/start - Start Parsing\n/next - Next Page\n/back - Previous Page\n/exit - Exit\n  |\n  |-# ')

    if page_option == "/start":
        func.parse(url)
    elif page_option == "/next":
        counter += 1
        func.parse(url + "page/" + str(counter))
    elif page_option == "/back":
        counter -= 1
        func.parse(url + "page/" + str(counter))
