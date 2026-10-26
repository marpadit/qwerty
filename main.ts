basic.showLeds(`
    # . # # #
    # . # . .
    # # # # #
    . . # . #
    # # # . #
    `)
let strip = neopixel.create(DigitalPin.P8, 4, NeoPixelMode.RGB)
strip.setBrightness(100)
strip.clear()
let distance = turtleBit.ultra()
basic.forever(function () {
    distance = turtleBit.ultra()
    if (distance >= 30) {
        turtleBit.run(DIR.Run_forward, 80)
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
    } else {
        turtleBit.run(DIR.Turn_Left, 80)
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    }
})
