def test_superuser(superuser):
    is_superuser = superuser.is_superuser
    assert is_superuser == 1


def test_staff_user(staff_user):
    is_staff = staff_user.is_staff
    assert is_staff == 1
