import hiero.core
import hiero.ui
import nuke

# Determine Nuke major version
nuke_major_version = int(nuke.NUKE_VERSION_MAJOR)

# Import the appropriate Qt bindings
if nuke_major_version < 16:
    from PySide2.QtWidgets import QMessageBox, QAction
else:
    from PySide6.QtWidgets import QMessageBox
    from PySide6.QtGui import QAction

def delete_empty_tracks():
    timeline = hiero.ui.activeSequence()
    if not timeline:
        QMessageBox.warning(None, "No Timeline", "No active timeline is selected.")
        return

    removed_count = 0

    for track in list(timeline.videoTracks()):
        if not track.items():
            timeline.removeTrack(track)
            removed_count += 1

    for track in list(timeline.audioTracks()):
        if not track.items():
            timeline.removeTrack(track)
            removed_count += 1

    QMessageBox.information(
        None,
        "Done",
        f"Deleted {removed_count} empty track(s)."
    )

# def add_delete_empty_tracks_action():
#     menu_action = hiero.ui.findMenuAction("Sandwich Dailies")
#     if not menu_action:
#         print("Sandwich Dailies menu not found.")
#         return

#     sandwich_menu = menu_action.menu()
#     action = QAction("Delete Empty Tracks", sandwich_menu)
#     action.triggered.connect(delete_empty_tracks)
#     sandwich_menu.addAction(action)

# add_delete_empty_tracks_action()