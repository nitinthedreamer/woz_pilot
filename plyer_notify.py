from plyer import notification
from plyer.utils import platform


notification.notify(
    title = 'Intervention',
    message = 'Read Carefully!',
    app_icon = '/Users/nitinkumar/workspace/intervene/woz.png',
    ticker = 'Currently doing the testing!',
    timeout = 30,
)