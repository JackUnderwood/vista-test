from ui import UI

__author__ = 'John Underwood'


class AuditEdit(UI):
    process = UI()
    process.go_to_driver_url("http://indytest/auditConfig")

    process.wait(1)
    process.teardown()
    pass
