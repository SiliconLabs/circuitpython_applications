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

import board
from LedMatrixBuffer import LedMatrixBuffer

text = 'SILABS NOW SUPPORTS CIRCUITPYTHON!!!'
text_length_in_pixel = len(text) * 6 - 1
screen_width = 13

i2c = board.I2C()

matrix = LedMatrixBuffer(i2c)
matrix.set_led_scaling(0xFF)
matrix.global_current = 0xFF
matrix.enable = True

i = screen_width
while(1):
    # the text will start scrolling from the right side of the screen (13th pixel)
    # if the whole text passed through the screen, the text will roll back to the
    # 13th pixel
    matrix.fill(0)
    matrix.text(text, i, 0, 0xFFFFFF)
    i = i - 1
    if i == -text_length_in_pixel:
        i = screen_width
    matrix.show()

