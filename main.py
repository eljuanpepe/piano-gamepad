import mido
import vgamepad as vg
from config import BUTTON_INPUTS, STICK_MAPPING, TRIGGER_MAPPING
from utils import update_button, update_stick, update_trigger
import logging

try:
    gamepad = vg.VX360Gamepad()
    input_port_name = mido.get_input_names()[1]
    port = mido.open_input(input_port_name)
except IndexError:
    logging.error("\nDispositivo MIDI no encontrado")
    exit(1)
except PermissionError:
    logging.error(
        "\nPermiso denegado"
        "\nEjecuta con sudo o usa el comando 'sudo chmod +0666 /dev/uinput'"
    )
    exit(1)


try:
    print("Escuchando dispositivo MIDI:", input_port_name)
    for msg in port:
        if msg.type == "note_on":
            # Botones
            if msg.note in BUTTON_INPUTS:
                update_button(gamepad, BUTTON_INPUTS[msg.note], msg.velocity)

            # Joystick
            if msg.note in STICK_MAPPING:
                axis, direction = STICK_MAPPING[msg.note]
                update_stick(gamepad, axis, direction, msg.velocity)

            # Triggers
            if msg.note in TRIGGER_MAPPING:
                trigger = TRIGGER_MAPPING[msg.note]
                update_trigger(gamepad, trigger, msg.velocity)
except KeyboardInterrupt:
    pass
