import sqlite3


def main(name_db, name_file_txt):
    sqlite_connection = sqlite3.connect(f"{name_db}")
    cursor = sqlite_connection.cursor()

    with open(f"{name_file_txt}", "r", encoding="utf-8") as words:
        words = list(map(lambda x: x.strip("\n"), words.readlines()))

    for word_translation in words:
        word_translation = word_translation.strip("\n").split(",")
        cursor.execute("INSERT INTO words (word, translation) VALUES (?, ?)", (word_translation[0], word_translation[1]))
        sqlite_connection.commit()


if __name__ == '__main__':
    main('words.db', "english.txt")


"""Закомментированная часть кода служила для соединения двух файлов в 1 для удобства"""

"""The commented out part of the code served to merge two files into 1 for convenience."""

#with open(f"{'translate.txt'}", "r+", encoding="utf-8") as file:
    #    translate = list(map(lambda x: x.strip("\n"), file.readlines()))
    #with open(f"{'english_test.txt'}", "r+", encoding="utf-8") as file:
    #    words = list(map(lambda x: x.strip("\n"), file.readlines()))
    ##with open(f"{name_file_txt}", "a", encoding="utf-8") as file:
    #    for i in range(len(words)):
    #        file.write(f"{words[i]}, {translate[i]} \n")