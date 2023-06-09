from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPeerChannel
import csv

api_id = 'YOUR_API_ID'
api_hash = '_YOUR_API_HASH'
# international format
phone_number = 'YOUR_PHONE_NUMBER'


client = TelegramClient('session_name', api_id, api_hash)

# create a new instance of TelegramClient
client = TelegramClient('session_name', api_id, api_hash)


async def prompt_and_select_group():
    # connect to telegram
    await client.start(phone_number)

    # get list of available groups
    dialogs = await client.get_dialogs()

    # filter and print only own groups
    own_groups = []
    print("Your Groups: ")
    for dialog in dialogs:
        if dialog.is_group:
            if dialog.entity.creator:
                own_groups.append(dialog)
                print(f"{len(own_groups)}. {dialog.entity.title}")

    # prompt the user to select a group
    group_index = int(
        input("Enter the index of the group you want to move users to: "))
    selected_group = own_groups[group_index - 1].entity

    # disconnect from telegram
    await client.disconnect()

    return selected_group


async def move_users_to_group(target_group, csv_file):
    await client.start(phone_number)

    # get the input entity for the target group
    target_group_entity = await client.get_entity(target_group)

    # read csv file and retrieve the members ID
    user_ids = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_ids.append(int(row['User ID']))

    # move users to the target group
    for user_id in user_ids:
        try:
            if isinstance(target_group_entity, InputPeerChannel):
                await client(InviteToChannelRequest(target_group_entity, [user_id]))
            else:  # If the target group is a chat
                await client(AddChatUserRequest(target_group_entity.id, user_id, fwd_limit=100))
            print(f"User {user_id} moved to {target_group.title}")
        except Exception as e:
            print(f"Failed to move user {user_id}: {e}")

    # disconnect from telegram
    await client.disconnect()

# replace 'users' with the path to your csv file containing the user data
users_csv_file = 'users.csv'

# trigger the function to prompt and select the group
selected_group = client.loop.run_until_complete(prompt_and_select_group())

# trigger the function to move users from CSV to the selected group
with client:
    client.loop.run_until_complete(
        move_users_to_group(selected_group, users_csv_file))
