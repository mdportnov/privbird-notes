import copy
from dataclasses import dataclass
from re import sub

from privbird.messages.Message import Message


def prettify(s: str) -> str:
    return sub(' +', ' ', s.strip().capitalize())


@dataclass
class EmailNotification:
    subject = Message(
        ru='Уведомление от PrivBird',
        en='PrivBird notification'
    )

    fake = Message(
        ru='фейковая',
        en='fake'
    )
    real = Message()

    ending_is_not_destroyed = Message(
        ru='при следующем прочтении будет отображена фейковая записка',
        en='the next time someone reads it, a fake note will be displayed'
    )
    ending_is_destroyed = Message(
        ru='содержимое уничтожено',
        en='the content was destroyed'
    )

    content = Message(
        ru='{real} записка с ID {id} была только что прочитана, {ending}.',
        en='The {real} note with ID {id} has just been read, {ending}.'
    )

    @classmethod
    def __format(cls, real: Message, note_id: str, ending: Message) -> Message:
        content = copy.deepcopy(cls.content)
        content.ru = prettify(cls.content.ru.format(real=real.ru, id=note_id, ending=ending.ru))
        content.en = prettify(cls.content.en.format(real=real.en, id=note_id, ending=ending.en))
        return content

    @classmethod
    def build(cls, is_real: bool, is_destroyed: bool, slug: str) -> Message:
        real = cls.real if is_real else cls.fake
        ending = cls.ending_is_destroyed if is_destroyed else cls.ending_is_not_destroyed
        note_id = slug[-4:].rjust(len(slug), '*')
        return cls.__format(real, note_id, ending)
