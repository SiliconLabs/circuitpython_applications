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

from time import monotonic


class SleepTimerEntry:
    def __init__(self, callback, timedelta, last_invoked) -> None:
        self.callback = callback
        self.timedelta = timedelta
        self.last_invoked = last_invoked


class SleepTimer:
    timers = []

    @classmethod
    def setup_timer(cls, callback, timedelta):
        cls.timers.append(
            SleepTimerEntry(
                callback=callback,
                timedelta=timedelta,
                last_invoked=None,
            ),
        )

    @classmethod
    def delete_timer_by_callback(cls, timer_callback):
        timerobjects = list(filter(lambda e: e.callback == timer_callback, cls.timers))
        if timerobjects:
            cls.timers.remove(timerobjects[0])

    @classmethod
    def main_function(cls):
        for entry in cls.timers:
            if (
                entry.last_invoked is None
                or monotonic() >= entry.last_invoked + entry.timedelta
            ):
                if entry.callback is not None:
                    last_timestamp = entry.last_invoked
                    entry.last_invoked = monotonic()
                    entry.callback(last_timestamp, entry.last_invoked)
