from typing import Self


class Comment:
    def __init__(self, msg: str, author: str):
        self.author = author
        self.msg = msg
        self.replies: list[Comment] = []
        self.deleted = False

    def __str__(self, level=0, prefix="") -> str:
        msg = f"{self.author}: {self.msg}" if not self.deleted else "Цей коментар було видалено."
        ret = "\t" * level + prefix + msg + "\n"
        for msg in self.replies:
            ret += msg.__str__(level + 1, " ")
        return ret

    def add_reply(self, comment: Self) -> None:
        self.replies.append(comment)

    def remove_reply(self) -> None:
        self.deleted = True

    def display(self) -> None:
        print(self)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()


# Приклад очікуваного результату:
"""
    Бодя: Яка чудова книга!
    Цей коментар було видалено.
        Сергій: Не книжка, а перевели купу паперу ні нащо...
    Марина: Що в ній чудового?
"""
