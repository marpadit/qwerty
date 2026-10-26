tracking_values = 0
basic.show_leds("""
    # . # # #
    # . # . .
    # # # # #
    . . # . #
    # # # . #
    """)
strip = neopixel.create(DigitalPin.P8, 4, NeoPixelMode.RGB)
strip.clear()

def on_forever():
    global tracking_values
    tracking_values = turtleBit.line_tracking()
    if tracking_values == 5 or (tracking_values == 6 or tracking_values == 7):
        turtleBit.run(DIR.RUN_FORWARD, 60)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.show_number(tracking_values)
    elif tracking_values == 4:
        turtleBit.motor(LR.LEFT_SIDE, MD.BACK, 80)
        turtleBit.motor(LR.RIGHT_SIDE, MD.FORWARD, 80)
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        basic.show_number(tracking_values)
    elif tracking_values == 1:
        turtleBit.motor(LR.LEFT_SIDE, MD.FORWARD, 80)
        turtleBit.motor(LR.RIGHT_SIDE, MD.BACK, 80)
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        basic.show_number(tracking_values)
    else:
        turtleBit.car_state(MotorState.STOP)
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.show_number(tracking_values)
basic.forever(on_forever)
