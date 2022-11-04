from dataclasses import dataclass

from privbird.messages.Message import Message


@dataclass
class EmailNotifications:
    subject = Message(
        ru='Уведомление от PrivBird',
        en='PrivBird notification'
    )
    fake = Message(
        ru='фейковая',
        en='fake'
    )
    has_fake = Message(
        ru='при следующем прочтении будет отображена фейковая записка',
        en='the next time someone reads it, a fake note will be displayed'
    )
    notification = Message(
        ru='{fake:} записка с ID {id} была только что прочтена, {has_fake:содержимое уничтожено}.',
        en='The {fake:} note with ID {id} has just been read, {has_fake:the content was destroyed}.'
    )
