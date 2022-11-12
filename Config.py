import configparser


class BaseConfig:
    def __init__(self):
        super(BaseConfig, self).__init__()

    def get_type_file(self):
        type_file = {
            'video': 'video/mp4',
            'audio': 'audio/mp3',
        }

        return type_file


class SettingsConfigMenu:
    def __init__(self):
        super(SettingsConfigMenu, self).__init__()

    def get_default_path(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        default_directory = 'C:/Users/Admin/Desktop'

        config.set('SETTINGS_PATH', 'status', 'True')
        config.set('SETTINGS_PATH', 'directory', default_directory)

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        return config

    def get_user_path(self, directory):

        config = configparser.ConfigParser()
        config.read('config.ini')

        config.set('SETTINGS_PATH', 'status', 'False')
        config.set('SETTINGS_PATH', 'directory', directory)

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        return config

    def update_status_convert_audio(self, status: str):
        config = configparser.ConfigParser()
        config.read('config.ini')

        config.set('SETTINGS_AUDIO_CONVERT', 'status', str(status))

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        return config

