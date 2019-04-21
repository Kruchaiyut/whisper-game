# TianTcl - Whisper game - generator

import random

_subject    = ["ครอบครัว","ส่วนตัว","บริษัท","คู่รัก"]
ext_sub     = [None,"อบอุ่น","คนเดียว","ธุรกิจ","หวานๆ"]
_verb       = ["ขับรถส่วนตัว","นั่งรถโดยสาร","ขึ้นเครื่องบิน","โดยสารรถไฟ"]
ext_verb    = [None,"บ่อยๆ","ช้าๆ","รอขึ้นชั่วโมง","เรื่อยๆ"]
_object     = ["กาญจนบุรี","ชลบุรี","เชียงใหม่","เชียงราย","พังงา","ภูเก็ต","ขอนแก่น","นครราชสีมา"]
ext_obj     = [None,"ตะวันตก","ตะวันออก","เหนือ","ใต้","เฉียงเหนือ"]

def make(_part):

    if _part == "subject":
        word = random.choice(_subject)
    elif _part == "verb":
        word = random.choice(_verb)
    elif _part == "object":
        word = random.choice(_object)
    elif _part == "ext subject":
        word = random.choice(ext_sub)
    elif _part == "ext verb":
        word = random.choice(ext_verb)
    elif _part == "ext object":
        word = random.choice(ext_obj)
    return word

def gen():
    parts =["subject","ext subject","verb","object","ext object","ext verb"]
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence
