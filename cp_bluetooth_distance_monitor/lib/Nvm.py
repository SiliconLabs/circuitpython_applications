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
from microcontroller import nvm
from struct import pack, unpack_from, calcsize


class NvmField:
    def __init__(self, name, default_value) -> None:
        self.name = name
        self.default_value = default_value


class Float(NvmField):
    format: str = "f"


class Int8(NvmField):
    format: str = "b"


class Uint8(NvmField):
    format: str = "B"


class Int16(NvmField):
    format: str = "h"


class Uint16(NvmField):
    format: str = "H"


class Int32(NvmField):
    format: str = "i"


class Uint32(NvmField):
    format: str = "I"


# The whole NVM array (512 byte = 1 NVM block at GSDK level) updated in the background once there is any change in the nvm bytearray
class NvmStorage:
    def __init__(self, fields) -> None:
        self._need_flush = False
        self._nvm_loaded = False
        self._fields = fields
        self._fields.append(Uint8("__nvm_not_empty__", default_value=0))
        if calcsize(self.__marshaling_format) > len(nvm):
            raise ValueError(
                f"The size of the provided NVM fields are larger than the NVM size. ({calcsize(self.__marshaling_format)} byte > {len(nvm)} byte)"
            )
        for field in self._fields:
            setattr(self, field.name, field.default_value)
        self.__load_data_from_nvm()
        self._nvm_loaded = True
        self.logger("Loading parameters from NVM...")

    @property
    def __marshaling_format(self) -> str:
        return f'<{("").join([field.format for field in self._fields])}'

    def __load_data_from_nvm(self) -> None:
        nvm_content = list(
            unpack_from(
                self.__marshaling_format,
                bytearray(nvm[0 : calcsize(self.__marshaling_format)]),
            )
        )
        if nvm_content[-1] == 1:
            # Has data in NVM, override the default values
            for index, field in enumerate(self._fields):
                setattr(self, field.name, nvm_content[index])

    def update(self, key, value) -> None:
        if not key.startswith("_") and self._nvm_loaded:
            current_value = getattr(self, key)
            if current_value != value:
                self._need_flush = True
                setattr(self, key, value)

    def flush(self) -> None:
        if self._need_flush:
            self.logger("Flush parameter changes...")
            if self.__nvm_not_empty__ == 0:
                self.__nvm_not_empty__ = 1
            nvm[0 : calcsize(self.__marshaling_format)] = pack(
                self.__marshaling_format,
                *[getattr(self, field.name) for field in self._fields],
            )
            self._need_flush = False

    def logger(self, text):
        print(f"{self.__class__}: {text}")
