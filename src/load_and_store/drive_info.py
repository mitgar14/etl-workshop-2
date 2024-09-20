from store import auth_drive

def store_init():
    drive = auth_drive()
    
    about_info = drive.GetAbout()
    
    root_folder_id = about_info['rootFolderId']
    total_storage = int(about_info['quotaBytesTotal'])
    used_storage = int(about_info['quotaBytesUsed'])
    free_storage = total_storage - used_storage

    total_storage_gb = total_storage / (1024**3)
    used_storage_gb = used_storage / (1024**3)
    free_storage_gb = free_storage / (1024**3)

    print(f"Root Folder ID: {root_folder_id}")
    print(f"Total Storage: {total_storage_gb:.2f} GB")
    print(f"Used Storage: {used_storage_gb:.2f} GB")
    print(f"Free Storage: {free_storage_gb:.2f} GB")

store_init()