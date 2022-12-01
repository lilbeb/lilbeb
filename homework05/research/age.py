import datetime as dt
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    am = 0
    summ = 0
    friends = get_friends(user_id).items
    currage = dt.datetime.now().year
    for i in friends:
        try:
            summ += int(currage - int(i["bdate"][5:]))
            am += 1
        except:
            pass
    if am > 0:
        return summ // am
    return None
