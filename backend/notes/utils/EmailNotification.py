from privbird.messages.Message import Message


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

    has_fake = Message(
        ru='при следующем прочтении будет отображена фейковая записка',
        en='the next time someone reads it, a fake note will be displayed'
    )
    dont_have_fake = Message(
        ru='содержимое уничтожено',
        en='the content was destroyed'
    )

    content = Message(
        ru='{real} записка с ID {id} была только что прочтена, {ending}.',
        en='The {real} note with ID {id} has just been read, {ending}.'
    )

    def __init__(self, is_real: bool, has_fake: bool, slug: str):
        real = self.fake if not is_real else self.real
        ending = self.has_fake if not has_fake else self.dont_have_fake
        note_id = slug[-4:].rjust(len(slug), '*')
        self.content.ru = self.content.ru.format(real=real.ru, id=note_id, ending=ending.ru)
        self.content.en = self.content.en.format(real=real.en, id=note_id, ending=ending.en)
