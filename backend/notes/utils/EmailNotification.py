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

    ending_has_fake = Message(
        ru='при следующем прочтении будет отображена фейковая записка',
        en='the next time someone reads it, a fake note will be displayed'
    )
    ending_dont_have_fake = Message(
        ru='содержимое уничтожено',
        en='the content was destroyed'
    )

    content = Message(
        ru='{real} записка с ID {id} была только что прочтена, {ending}.',
        en='The {real} note with ID {id} has just been read, {ending}.'
    )

    @classmethod
    def __format(cls, real: Message, note_id: str, ending: Message) -> Message:
        content = copy.deepcopy(cls.content)
        content.ru = prettify(cls.content.ru.format(real=real.ru, id=note_id, ending=ending.ru))
        content.en = prettify(cls.content.en.format(real=real.en, id=note_id, ending=ending.en))
        return content

    @classmethod
    def build(cls, is_real: bool, has_fake: bool, slug: str) -> Message:
        real = cls.fake if not is_real else cls.real
        ending = cls.ending_has_fake if is_real and has_fake else cls.ending_dont_have_fake
        note_id = slug[-4:].rjust(len(slug), '*')
        return cls.__format(real, note_id, ending)
