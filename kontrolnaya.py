"""
10. Класс Post Класс описывает публикацию от пользователя в сети:
никнейм пользователя, время публикации, кол-во лайков, текст сообщения, список комментариев.
Конструктор класса получает автора, устанавливает время, зануляет кол-во ругательств, а для
комментариев создает списочный массив. Добавить метод, позволяющий поставить лайк сообщению.
"""


class Post:
    def __init__(self, name, time, matershinka):
        self.name=name
        self.time=time
        self.matershinka=matershinka
        if "дурачок".lower() in self.matershinka or "тормоз".lower() in self.matershinka:
            self.matershinka="\n"
            self.matershinka+="Маты: Все ругательства почищены :)"

    def print_info(self):
        print(self.name,self.time,self.matershinka)


class Sms(Post):
    def __init__(self,name,time,matershinka,likes,text,comments):
        self.likes=likes
        self.text=text
        self.comments=comments
        super().__init__(name,time,matershinka)


    def print_info(self):
        super().print_info()
        print(self.likes,self.text,self.comments)


sms=Sms("Имя пользователя: Gonep","\nВремя: 12:38", "\nМаты: дурачок, тормоз", "Лайков: 564", "\nТекст Поста: Уфф, это че за тигрр", "\nКомментарии: АУффф, брат, внатуре тигррр")
commentslist=[]
commentslist.append(sms)
commentslist[0].comments
sms.print_info()


def push_like():
    a=input("\n\nХотите поставить лайк?\n")
    if a.lower() == "да":
        print("Лайк поставлен :)")
    if a.lower() == "нет":
        print("Лайк не поставлен :(")


push_like()