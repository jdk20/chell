import os


class GeneralPurposeDevice:
    """
    Initializes a GPIO connected device and verifies the GPIO pin is
    currently available for use. Expects the use of Broadcom, not physical,
    pin numbering.

    :type gpio_pin: int
    :param gpio_pin:
        GPIO Broadcom pin number.
    """
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin

        # Validate choice of GPIO pin, pin not locked
        try:
            pass  # gpiozero
        except ValueError:
            raise ValueError('Invalid GPIO pin selected')

        self.__enter()

    def __enter(self):
        pass

    def __exit(self):
        pass


class Speaker(GeneralPurposeDevice):
    """
    Extends class:`GeneralPurposeDevice` and applies it to a single GPIO
    speaker.

    :type tone: float or list
    :param tone:
        Frequency or list of frequencies (hz) for playing a pure tone.

    :type tone_duration : float or list
    :param tone_duration:
        Duration or list of durations (ms) for playing a pure tone.
    """
    def __init__(self, gpio_pin, tone, tone_duration):
        super().__init__(gpio_pin)

        if not isinstance(tone, list):
            self.tone = [tone]
        else:
            self.tone = tone

        if not isinstance(tone_duration, list):
            self.tone_duration = [tone_duration]
        else:
            self.tone_duration = tone_duration

        for _ in tone:
            if _ < 1000 or _ > 100000:
                raise ValueError('Tone frequency must be within the range of '
                                 'mouse hearing (1 to 100 kHz).')

        for _ in tone_duration:
            if _ <= 0:
                raise ValueError('Tone duration (ms) must be positive.')

        if len(tone) != len(tone_duration):
            raise IndexError('List of tones and tone durations must be the '
                             'same length.')

    def __repr__(self):
        return 'device speaker (%s hz) on gpio pin %s' % (
            self.tone, self.gpio_pin)

    def play(self):
        """
        Plays the tone or sequence of tones.
        """
        pass


class SyringePump(GeneralPurposeDevice):
    def __init__(self, gpio_pin, tone):
        super().__init__(gpio_pin)
        self.tone = tone


a = Speaker(3, [4000, 5000], [100, 100])
