from blockmate.paths.v1_users_id.get import ApiForget
from blockmate.paths.v1_users_id.post import ApiForpost
from blockmate.paths.v1_users_id.delete import ApiFordelete


class V1UsersId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
