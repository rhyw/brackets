## Tips for sublime configuration

- Change default layout(2 for example):
    Preferences->Browse Packages->User->default_layout.py:

    ```
    import sublime
    
    def plugin_loaded():
        sublime.active_window().run_command("set_layout", {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
        })
    ```

- Prevent opening previous tabs:
    Preferences->Settings->User:
    {
        "remember_open_files": false,
        "hot_exit": false,
    }

