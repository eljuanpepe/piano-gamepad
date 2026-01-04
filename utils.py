JOYSTICK_LIMIT = 32767
TRIGGER_LIMIT = 255


def get_controller_value(key_velocity, limit):
    if key_velocity > 0:
        return int((key_velocity / 127) * limit)
    else:
        return 0


def update_stick(gamepad, axis, direction, key_velocity):
    value = get_controller_value(key_velocity, JOYSTICK_LIMIT) * direction

    if axis == "LX":
        gamepad.left_joystick(x_value=value, y_value=gamepad.report.sThumbLY)
    elif axis == "LY":
        gamepad.left_joystick(x_value=gamepad.report.sThumbLX, y_value=value)
    elif axis == "RX":
        gamepad.right_joystick(x_value=value, y_value=gamepad.report.sThumbRY)
    elif axis == "RY":
        gamepad.right_joystick(x_value=gamepad.report.sThumbRX, y_value=value)

    gamepad.update()


def update_trigger(gamepad, trigger, key_velocity):
    value = get_controller_value(key_velocity, TRIGGER_LIMIT)

    if trigger == "LT":
        gamepad.left_trigger(value=value)
    elif trigger == "RT":
        gamepad.right_trigger(value=value)

    gamepad.update()


def update_button(gamepad, button, velocity):
    if velocity > 0:
        gamepad.press_button(button)
    else:
        gamepad.release_button(button)

    gamepad.update()
