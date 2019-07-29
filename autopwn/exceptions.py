class AutoPwnException(Exception):
    pass


# Acid Exceptions


class AcidTestException(AutoPwnException):
    pass


class AcidSSHConfigurationException(AcidTestException):
    pass
