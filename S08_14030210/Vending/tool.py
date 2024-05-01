class Tool:
    def TxtContentReader(text):
        main_list = text.split("/")
        for index, item in enumerate(main_list):
            main_list[index] = item.split(",")

        return main_list