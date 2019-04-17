from fu_clips.push_button_led_handler import PushButtonLedHandler


def test_push_button_led_handler():
    led_handler = PushButtonLedHandler()
    assert not led_handler.is_on()
    led_handler.on()
    assert led_handler.is_on()
