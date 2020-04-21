import pickle
import os
import YCWTPP
# The next 4 lines fills data files with either a blank, or a number to that files won't be completely empty
if os.path.getsize("times.dat") == 0:
    pickle.dump("", open("times.dat", "wb"))
if os.path.getsize("savedchanneldata.dat") == 0:
    pickle.dump("", open("savedchanneldata.dat", "wb"))
os.system("cls")
channels = {
}
# When user starts program for first time ever, times.dat is empty, so program adds 0 into data.
if str(pickle.load(open("times.dat", "rb"))) is "":
    YCWTPP.timesdataprep()
# Sets the variable time to whatever the data is, prevents overwrite as variable gets it from file.
times = pickle.load(open("times.dat", "rb"))
pickle.dump(times, open("times.dat", "wb"))
if int(pickle.load(open("times.dat", "rb"))) > 1:
    times = 1
else:
    times = 0

while True:
    # This part of the code will run when there is no data inputted, does not make Python crash.
    if times == 0:
        option = input("Type 1 for Enter channel name, 2 for See data, or 3 to delete a YouTube Channel or take 1 watch count away:")

        # Update a channels watch count or adds in a new channel depending on if channel exists.
        if option == "1":

            user_input = input("What YouTube channel have you just watched? Type it in correctly (uppercase, lowercase, etc):")

            def add_or_update(channels, key):

                if key in channels.keys():

                    channel_watch_update = int(channels[key]) + 1
                    channels[user_input] = channel_watch_update
                else:
                    channels.update({str(user_input): 1})

            key = user_input
            add_or_update(channels, key)

            # Prints the full list of all the channels including the new channel and their watch counts.
            for key, value in channels.items():
                print(key, ' : ', value)
            # Saves the updated data to savedchanneldata.dat file.
            pickle.dump(channels, open("savedchanneldata.dat", "wb"))
            loaded_times_data = pickle.load(open("times.dat", "rb"))
            times = int(loaded_times_data) + 1
            pickle.dump(times, open("times.dat", "wb"))

        # Allows user to see channel data.
        if option == "2":
            # Program checks if data/file has data inside, if not, tells user that no data exists and can't be shown.
            if str(pickle.load(open("savedchanneldata.dat", "rb"))) is "":
                print("There are no channels stored! Unable to carry out the process.")
            else:
                for key, value in pickle.load(open("savedchanneldata.dat", "rb")).items():
                    print(key, ' : ', value)
        # Allows user to delete Youtube channel, or if channel has more than 1 watch count, takes away one. This is for accidental miss types.
        if option == "3":
            # Checks if file has data in the first place, if it does, process continues, if not, process discontinues.
            if str(pickle.load(open("savedchanneldata.dat", "rb"))) is "":
                print("There are no channels stored! Unable to carry out the process.")
            # If data is found, program allows user to input a name and subtract watch count or delete channel.
            else:

                user_input_delete = input("What channel do you want to delete? If channel has more than 1 watch count, program will only subtract 1, if = to 1, deletes channel:")
                # Checks if entered name exists in the data/file
                if str(user_input_delete) in pickle.load(open("savedchanneldata.dat", "rb")):

                    channels = pickle.load(open("savedchanneldata.dat", "rb"))
                    delete_subtract_value = int(channels[user_input_delete]) - 1
                    # If channel only has 1 watch count, program deletes from the data/file.
                    if int(delete_subtract_value) == 0:
                        channels.pop(str(user_input_delete), None)
                    # If channel has more than 1 watch count, program subtracts 1 watch count.
                    else:

                        channels.update({str(user_input_delete): int(delete_subtract_value)})
                    # Saves the new information.
                    pickle.dump(channels, open("savedchanneldata.dat", "wb"))
                    # Gives user updated data.
                    updated_channels_data = pickle.load(open("savedchanneldata.dat", "rb"))
                    print(updated_channels_data)
                # If entered name does not exist, but data/file is not empty, program tells user that name does not exist.
                else:

                    print("The channel that was entered does not exist.")

    # Since data has been put in by this time (determined by value of times) it can now take data from files without crashing
    if int(times) >= 1:
        # Updates channels variable to the saved data file instead of resetting data.
        channels_info = pickle.load(open("savedchanneldata.dat", "rb"))
        channels = channels_info
        option = input("Type 1 for Enter channel name, 2 for See data, or 3 to delete a YouTube Channel or take 1 watch count away:")

        # Update a channels watch count or adds in a new channel depending on if channel exists.
        if option == "1":

            user_input = input("What YouTube channel have you just watched? Type it in correctly (uppercase, lowercase, etc):")

            def add_or_update(channels, key):

                if key in channels.keys():

                    channel_watch_update = int(channels[key]) + 1
                    channels[user_input] = channel_watch_update

                else:

                    channels.update({str(user_input): 1})

            key = user_input
            add_or_update(channels, key)

            # Prints the full list of all the channels including the new channel and their watch counts.
            for key, value in channels.items():
                print(key, ' : ', value)
            # Saves the updated data to savedchanneldata.dat file.
            pickle.dump(channels, open("savedchanneldata.dat", "wb"))
            loaded_times_data = pickle.load(open("times.dat", "rb"))
            times = int(loaded_times_data) + 1
            pickle.dump(times, open("times.dat", "wb"))

        # Allows user to see channel data.
        if option == "2":
            # Program checks if data/file has data inside, if not, tells user that no data exists and can't be shown.
            if str(pickle.load(open("savedchanneldata.dat", "rb"))) is "":
                print("There are no channels stored! Unable to carry out the process.")
            else:
                for key, value in pickle.load(open("savedchanneldata.dat", "rb")).items():
                    print(key, ' : ', value)
        # Allows user to delete Youtube channel, or if channel has more than 1 watch count, takes away one.
        if option == "3":
            # Checks if file has data in the first place, if it does, process continues, if not, process discontinues.
            if str(pickle.load(open("savedchanneldata.dat", "rb"))) is "":
                print("There are no channels stored! Unable to carry out the process.")
            # If data is found, program allows user to input a name and subtract watch count or delete channel.
            else:

                user_input_delete = input(
                    "What channel do you want to delete? If channel has more than 1 watch count, program will only subtract 1, if = to 1, deletes channel:")
                # Checks if entered name exists in the data/file
                if str(user_input_delete) in pickle.load(open("savedchanneldata.dat", "rb")):

                    channels = pickle.load(open("savedchanneldata.dat", "rb"))
                    delete_subtract_value = int(channels[user_input_delete]) - 1
                    # If channel only has 1 watch count, program deletes from the data/file.
                    if int(delete_subtract_value) == 0:
                        channels.pop(str(user_input_delete), None)
                    # If channel has more than 1 watch count, program subtracts 1 watch count.
                    else:

                        channels.update({str(user_input_delete): int(delete_subtract_value)})
                    # Saves the new information.
                    pickle.dump(channels, open("savedchanneldata.dat", "wb"))
                    # Gives user updated data.
                    updated_channels_data = pickle.load(open("savedchanneldata.dat", "rb"))
                    print(updated_channels_data)
                # If entered name does not exist, but data/file is not empty, program tells user that name does not exist.
                else:

                    print("The channel that was entered does not exist.")







