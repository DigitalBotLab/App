# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
"""SimReady Explorer API

This module contains the API for the SimReady Explorer extension.
"""

__all__ = [
    "AssetType",
    "AssetFactory",
    "SimreadyAsset",
    "PropAsset",
    "find_assets",
    "add_asset_to_stage",
    "add_asset_to_stage_using_prims",
    "get_average_position_of_prims",
    "get_selected_xformable_prim_paths",
]


from .asset import AssetFactory, AssetType, PropAsset, SimreadyAsset  # noqa: F401, symbol is reexported
from .browser_api import (  # noqa: F401, F403, symbol is reexported
    add_asset_to_stage,
    add_asset_to_stage_using_prims,
    find_assets,
    get_average_position_of_prims,
    get_selected_xformable_prim_paths,
)
from .browser_model import SimReadyBrowserModel  # noqa: F401, symbol is reexported
from .extension import SimReadyBrowserExtension, get_instance  # noqa: F401, symbol is reexported
