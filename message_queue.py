# guess/message_queue.py
import queue
from threading import RLock

from line import reply_message


def get_id(event):
    return event.source.sender_id


def ask(event, question):
    reply_message(event, question)
    return MessageQueue.request(event)


class RequestTimout(Exception):
    pass


class MessageQueue:
    __lock = RLock()
    __requests = {}
    __responses = {}

    @classmethod
    def create_if_not_exists(cls, room):
        '''Create the requests and responses queues for the room if not exists'''
        with cls.__lock:
            if room not in cls.__requests:
                cls.__requests[room] = queue.Queue(maxsize=1)

            if room not in cls.__responses:
                cls.__responses[room] = queue.Queue(maxsize=1)

    @classmethod
    def handle(cls, event):
        '''Handle the message, check whether there is room request for'''
        room = get_id(event)
        cls.create_if_not_exists(room)

        try:
            if not cls.__requests[room].empty():
                cls.__responses[room].put(event, timeout=1)
                cls.__requests[room].get()
                return True
            return False
        except queue.Empty:
            '''No request, ignore the message'''
            return False

    @classmethod
    def request(cls, event, timeout=30):
        '''Request a message, block until message comes in or timeout'''
        room_id = get_id(event)
        try:
            cls.create_if_not_exists(room_id)

            cls.__requests[room_id].put_nowait(True)
            return cls.__responses[room_id].get(timeout=timeout)

        except queue.Empty:
            MessageQueue.clear(room_id)
            raise RequestTimout

    @classmethod
    def clear(cls, room):
        '''Clear the requests'''
        cls.create_if_not_exists(room)
        try:
            cls.__requests[room].get_nowait()
        except queue.Empty:
            pass
