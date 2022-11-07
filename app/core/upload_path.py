import time

from app.core.enum_const import EnumConst
from app.utils.utils import format_date_now, get_filename_ext


def upload_avatar_path(instance, filename):
    path = "images/avatar"
    date_today = format_date_now(format_date=EnumConst.DATE_UPLOAD_FORMAT)
    new_filename = time.time()
    name, ext = get_filename_ext(filename)
    return f"{path}/{date_today}/{new_filename}{ext}"
