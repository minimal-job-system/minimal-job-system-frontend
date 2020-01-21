from constance import config

class Settings:
    @property
    def APP_TITLE(self):
        if 'JOB_SYSTEM_TITLE' in dir(config):
            return config.JOB_SYSTEM_TITLE
        else:
            return 'Minimal Job System'

    @property
    def APP_ICON(self):
        print(config)
        print(dir(config))
        if 'JOB_SYSTEM_ICON' in dir(config):
            return config.JOB_SYSTEM_ICON
        else:
            return 'job_system_frontend/img/default.ico'

    @property
    def ONLY_OWNER_CAN_STOP_JOB(self):
        if 'ONLY_OWNER_CAN_STOP_JOB' in dir(config):
            return config.ONLY_OWNER_CAN_STOP_JOB
        else:
            return False
