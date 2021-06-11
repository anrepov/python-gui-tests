def test_del_group(app):
    group_name = "my group"
    old_list = app.groups.get_group_list()

    if group_name not in old_list:
        app.groups.add_new_group(group_name)

    old_list = app.groups.get_group_list()
    app.groups.del_group(group_name)
    new_list = app.groups.get_group_list()
    old_list.remove(group_name)
    assert sorted(old_list) == sorted(new_list)
