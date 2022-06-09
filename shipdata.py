#!/usr/bin/env python3
passenger_liners = {
    pl1 : { length : 165, draught : 7, height : 39 },
    pl2 : { length : 170, draught : 8, height : 38 },
    pl3 : { length : 150, draught : 7, height : 36 },
    pl4 : { length : 162, draught : 7, height : 39 },
    pl5 : { length : 140, draught : 6, height : 30 }
}

heavy_tankers = {
    ht1 : { length : 142, draught : 5, height : 26 },
    ht2 : { length : 138, draught : 5, height : 46 },
    ht3 : { length : 145, draught : 5, height : 49 },
    ht4 : { length : 144, draught : 6, height : 47 },
    ht5 : { length : 140, draught : 5, height : 35 },
    ht6 : { length : 142, draught : 5, height : 24 },
    ht7 : { length : 150, draught : 6, height : 40 },
    ht8 : { length : 152, draught : 7, height : 41 },
    ht9 : { length : 149, draught : 5, height : 37 },
    ht10 : { length : 153, draught : 6, height : 38 },
    ht11 : { length : 135, draught : 6, height : 37 },
    ht12 : { length : 150, draught : 5, height : 28 },
    ht13 : { length : 145, draught : 5, height : 28 },
    ht14 : { length : 139, draught : 5, height : 46 },
    ht15 : { length : 134, draught : 4, height : 43 },
    ht16 : { length : 137, draught : 5, height : 42 },
    ht17 : { length : 132, draught : 6, height : 44 },
    ht18 : { length : 130, draught : 6, height : 41 },
    ht19 : { length : 129, draught : 6, height : 36 },
    ht20 : { length : 125, draught : 4, height : 47 },
    ht21 : { length : 127, draught : 5, height : 38 },
    ht22 : { length : 125, draught : 5, height : 34 },
    ht23 : { length : 130, draught : 6, height : 31 },
    ht24 : { length : 142, draught : 6, height : 37 },
    ht25 : { length : 144, draught : 6, height : 31 },
    ht26 : { length : 147, draught : 7, height : 35 },
    ht27 : { length : 142, draught : 6, height : 38 },
    ht28 : { length : 147, draught : 7, height : 38 },
    ht29 : { length : 156, draught : 6, height : 28 },
    ht30 : { length : 158, draught : 6, height : 30 },
    ht31 : { length : 156, draught : 6, height : 51 },
    ht32 : { length : 150, draught : 6, height : 52 },
    ht33 : { length : 138, draught : 6, height : 36 },
    ht34 : { length : 133, draught : 6, height : 34 },
    ht35 : { length : 144, draught : 7, height : 38 }
}
