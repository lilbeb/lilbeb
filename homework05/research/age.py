import datetime as dt
import typing as tp
from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    friend = get_friends(user_id).items
    age_now = dt.datetime.now().year
    t = 0
    age = 0
    for i in friend:
        try:
            age += int(age_now - int(i["bdate"][5:]))
            t += 1
        except:
            pass
    if t > 0:
        return age // t
    return None
