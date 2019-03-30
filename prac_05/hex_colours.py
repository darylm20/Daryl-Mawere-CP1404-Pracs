colour_codes = {"gray50":"#7f7f7f",
                "ivory1": "#fffff0",
                "NavyBlue": "#000080",
                "purple": "#a020f0",
                "PowderBlue": "#b0e0e6",
                "WhiteSmoke": "#f5f5f5",
                "tomato4": "#8b3626",
                "salmon": "#fa8072",
                "DarkGreen": "#006400",
                "cyan3": "#00cdcd"}

colour_name = input ("Enter the name of a colour: ")

while colour_name != "":
    print ("The hex code for \"{}\" is {}".format(colour_name, colour_codes.get(colour_name)))

    colour_name = input ("Enter the name of a colour: ")