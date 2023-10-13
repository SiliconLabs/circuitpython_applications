"""
*****************************************************************************
Copyright 2023 Silicon Laboratories Inc. www.silabs.com
*****************************************************************************
SPDX-License-Identifier: Zlib

The licensor of this software is Silicon Laboratories Inc.

This software is provided \'as-is\', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.

*****************************************************************************
# EXPERIMENTAL QUALITY
This code has not been formally tested and is provided as-is. It is not
suitable for production environments. In addition, this code will not be
maintained and there may be no bug maintenance planned for these resources.
Silicon Labs may update projects from time to time.
******************************************************************************
"""

from board import PA0,PA4,PB1,PB0,PC0,PC1,PC2,PC3,PC6
from busio import SPI
from DrawApplication import DrawApplication

# Map PIN for touch screen   
XP = PA0
XM = PB1
YP = PA4
YM = PB0

# Map PIN SPI 
CS = PC1
SCK = PC2
MISO = PC3
MOSI = PC6
DC = PC0

# initialize application
app = DrawApplication(
    spi = SPI(clock = SCK, MISO = MISO, MOSI = MOSI),
    CS = CS,
    DC = DC,
    XM = XM,
    XP = XP,
    YP = YP,
    YM = YM
    )
# show logo Silabs and Circuit Python for 5s
app.clear_screen()
app.show_start_up()
app.show_color_palette() 
app.show_footer_logo()
    
while True:
    app.main_function()

            
