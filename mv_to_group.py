from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPeerChannel
import csv

api_id = 25912041
api_hash = '1e80ae432e20f44e80ce562aaf7e25e9'
phone_number = '+213664445489'


client = TelegramClient('session_name', api_id, api_hash)

# Create a new instance of the TelegramClient
client = TelegramClient('session_name', api_id, api_hash)


async def prompt_and_select_group():
    # Connect to Telegram
    await client.start(phone_number)

    # Get the list of available groups
    dialogs = await client.get_dialogs()

    # Filter and print only own groups
    own_groups = []
    print("Your Groups:")
    for dialog in dialogs:
        if dialog.is_group:
            if dialog.entity.creator:
                own_groups.append(dialog)
                print(f"{len(own_groups)}. {dialog.entity.title}")

    # Prompt the user to select a group
    group_index = int(
        input("Enter the index of the group you want to move users to: "))
    selected_group = own_groups[group_index - 1].entity

    # Disconnect from Telegram
    await client.disconnect()

    return selected_group


async def move_users_to_group(target_group, csv_file):
    # Connect to Telegram
    await client.start(phone_number)

    # Get the input entity for the target group
    target_group_entity = await client.get_entity(target_group)

    # Read the CSV file and retrieve the user IDs
    user_ids = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_ids.append(int(row['User ID']))

    # Move users to the target group
    for user_id in user_ids:
        try:
            if isinstance(target_group_entity, InputPeerChannel):
                await client(InviteToChannelRequest(target_group_entity, [user_id]))
            else:  # If the target group is a chat
                await client(AddChatUserRequest(target_group_entity.id, user_id, fwd_limit=100))
            print(f"User {user_id} moved to {target_group.title}")
        except Exception as e:
            print(f"Failed to move user {user_id}: {e}")

    # Disconnect from Telegram
    await client.disconnect()

# Replace 'USERS_CSV_FILE' with the path to your CSV file containing the user data
users_csv_file = 'users.csv'

# Call the function to prompt and select the group
selected_group = client.loop.run_until_complete(prompt_and_select_group())

# Call the function to move users from CSV to the selected group
with client:
    client.loop.run_until_complete(
        move_users_to_group(selected_group, users_csv_file))
