import storage

storage.remount("/", readonly=False)

newName = storage.getmount("/")
newName.label = "HO-mouse"

storage.remount("/", readonly=True)
storage.enable_usb_drive()