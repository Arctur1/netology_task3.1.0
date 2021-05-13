from main import YaUploader, ytoken, path


def test_create_folder_ok():
    expected_result = 201
    assert YaUploader(ytoken, path).create_folder() == expected_result
    print('Folder made successfully')

def test_create_folder_not_authorized():
    expected_result = 401
    assert YaUploader(ytoken, path).create_folder() == expected_result
    print('Not authorized')

def test_create_folder_ok_path_aleady_exists():
    expected_result = 409
    assert YaUploader(ytoken, path).create_folder() == expected_result
    print('Folder already exists')


