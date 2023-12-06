Changelog
=========

This document records all notable changes to ``omni.simready.explorer`` extension.
This project adheres to `Semantic Versioning <https://semver.org/>`_.

## [1.0.26] - 2023-06-20
- OM-95538: Don't turn off the instanceable attribute on assets with PhysicsVariant set to RigidBody when drag-and-dropping them
into the stage

## [1.0.25] - 2023-06-02
- OM-96886: Update screenshot used in extension registry

## [1.0.24] - 2023-06-01
- OM-96886: Update badge on SimReady asset thumbnails

## [1.0.23] - 2023-05-30
- OM-95406: Set default physics behavior of all assets to "RigidBody"

## [1.0.22] - 2023-05-17
- OM-94398: Removed superfluous print statement from class PropAsset constructor
- OM-94290: Normalized asset paths to use single backslahs ('/') as directory separators

## [1.0.21] - 2023-04-25
- OM-90516: Exposed Collect command in asset right-click menu

## [1.0.20] - 2023-04-24
- OM-83563: Created developer docs and tweaked APIs

## [1.0.19] - 2023-04-20
- Get dropped prim path when preview disabled

## [1.0.18] - 2023-04-14
- OM-90136: Disable preview when drag and drop into viewport

## [1.0.17] - 2023-04-13
- OM-90440: Update UI style of property widget to be same as other property widgets

## [1.0.16] - 2023-03-24
OM-87776: Assets are browsed on AWS S3 staging
- List of tags in asset details window resizes to fit the window

## [1.0.15] - 2023-03-24
OM-87028: "Replace Current Selection" doesn't apply to multiple asset selection
- Fix leak of SimReadyDetailDelegate instance

## [1.0.14] - 2023-03-22
OM-87028: Right-click doesn't select assets, and right-click menu works with multiple assets selected

## [1.0.13] - 2023-03-21
- OM-87026: Simple message displayed in property window when multiple assets selected
- OM-87032: Disabled tooltips since they were interfering with the right click menu

## [1.0.12] - 2023-03-18
- OM-85649: support of lazy load workflow in Create

## [1.0.11] - 2023-03-17
- OM-86101: Multiple drag items into viewport or stage window

## [1.0.10] - 2023-03-15
- OM-86315: Turn off instanceable attribute on _inst prim when adding an asset with Physics on, otherwise turn instanceable attribute on.
- Fixed issue with physics badge update on thumbnails, where the badge would be visible in the assets detail view even if physics would be off (None)

## [1.0.9] - 2023-03-13
- OM-86077: Added Open, Open with Payloads Disabled, Add at Selection, Copy URL Link right-click menu commands
- OM-85906: Renamed menu and tab to "SimReady Explorer"
- OM-86315: Set PhysicsVariant to None by default

## [1.0.8] - 2023-03-08
- OM-84838: Added API for listing an asset's behaviors, and adding an asset to the current stage

## [1.0.7] - 2023-03-07
- OM-83352: Updated asset property panel

## [1.0.6] - 2023-03-02
- OM-84829: Fixed searching against tags with spaces (multi-word tags)

## [1.0.5] - 2023-02-28
- OM-84243: Always search all assets
- OM-84245: Update tag list in search bar on search results

## [1.0.4] - 2023-02-16
- OM-66968: API for filtering assets
- Updated asset database; now includes 539 assets

## [1.0.3] - 2023-02-15
- OM-52823: The explorer looks for the asset database (asset_info.json) on omniverse://simready.ov.nvidia.com/Projects/
- Updated asset database; now includes 487 assets

## [1.0.2] - 2023-02-13
- Assets can be dropped onto the stage from the asset browser (requires omni.kit.widget.stage v2.7.24 which has not been released yet)
- Physics is enabled by default
- New Physx thumbnail badge is displayed when physics is enabled
- Updated asset database; now includes 317 assets (304 are simready)
- OM-81970: Open property panel by default
- OM-81973: Center widgets in property panel
- OM-81977: SimReady Explorer is docked when it starts
This required to not show the window after startup. Show from menu "Window/Browsers/Sim Ready".
- OM-81962: Remove gear button from search bar

omni.simready.explorer-1.0.2 requires the following extensions:
- omni.kit.widget.stage-2.7.24 (not available as of 2023-02-13)
- omni.kit.browser.core-2.2.2
- omni.kit.browser.folder.core-1.7.5
- omni.kit.widget.searchfield-1.1.0

## [1.0.1] - 2023-02-09
- Assets can be pre-configured with right-click menu options, or in the properties view.
- Drag-and-drop of pre-configured asset into the viewport
- Asset properties panel shows the following properties name, QCode, thumbnail, tags, physics behavior
- Asset properties panel updates when selected asset changes
- Supporting 158 assets on omniverse://simready.ov.nvidia.com/Projects/simready_content/common_assets/props/

## [1.0.0] - 2023-02-08
- Hierarchical Asset Categories are displayed
- Asset thumbnails are displayed, with tooltip showing asset name, dimensions and tags
- Asset property panel is displayed when user enables it through the top-right icon
- Search bar is populated with categories as tags when user clicks on a category in the Asset Category panel, and the assets are filtered
