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


class Configuration:
    def __init__(
        self,
        lower_threshold,
        upper_threshold,
        threshold_mode,
        range_mode,
        notification_status,
    ) -> None:
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold
        self.threshold_mode = threshold_mode
        self.range_mode = range_mode
        self.notification_status = notification_status

    @staticmethod
    def check_change(a, b):
        return b if a != b else None

    def changes(self, __value: object):
        changes = {
            "lower_threshold": self.check_change(
                self.lower_threshold, __value.lower_threshold
            ),
            "upper_threshold": self.check_change(
                self.upper_threshold, __value.upper_threshold
            ),
            "threshold_mode": self.check_change(
                self.threshold_mode, __value.threshold_mode
            ),
            "range_mode": self.check_change(self.range_mode, __value.range_mode),
            "notification_status": self.check_change(
                self.notification_status, __value.notification_status
            ),
        }
        return {k: v for k, v in changes.items() if v is not None}

    def update(self, key: str, value) -> None:
        setattr(self, key, value)

    def __eq__(self, __value: object) -> bool:
        return not bool(self.changes(__value))
