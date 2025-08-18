# SPDX-FileCopyrightText: 2025 IObundle
#
# SPDX-License-Identifier: MIT

import os
import shutil


def setup(py_params_dict):
    # Copy iob_linux to the build dir submodules/
    src = os.path.join(os.path.dirname(__file__), "..")
    dst = os.path.join(py_params_dict["build_dir"], "submodules/iob_linux")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)

    attributes_dict = {
        "generate_hw": False,
        "instantiate": False,
    }

    return attributes_dict
