def run():
    check_num = 0
    while check_num != 6:
        check_num = Number.get_number(View.main_menu(), 6)
        if check_num == 1:
            View.info_create_msg(Functional.
                                 create_new_note(View.input_note_title(),
                                                 View.input_note_text()))
        elif check_num == 2:
            dis = Functional.reading_file()
            View.show_remove(Functional.reading_file())
            id_note = Number.get_key(View.input_update_text(), dis)
            if id_note == 0:
                continue
            elif id_note == -1:
                View.show_note(dis)
            else:
                View.info_update_msg(Functional.
                                     update(id_note,
                                            View.input_note_title(),
                                            View.input_note_text())),
        elif check_num == 3:
            dis = Functional.reading_file()
            View.show_remove(Functional.reading_file())
            id_note = Number.get_key(View.input_remove_text(), dis)
            if id_note == 0:
                continue
            elif id_note == -1:
                View.show_note(dis)
            else:
                View.info_remove_msg(Functional.remove_note(id_note))
        elif check_num == 4:
            View.show_note(Functional.reading_file())
        elif check_num == 5:
            View.info_cleaning_msg(Functional.cleaning_file())
        elif check_num == 6:
            View.exit_msg()
            break