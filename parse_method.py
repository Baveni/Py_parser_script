# The method itself is basic. We create a function that opens a file
# you want to parse data from (Read only). Then opens a new file to write
# parsed output to. For each data it will go to new line. You can also rewrite
# the script to match CSV.
# Note that the new file will get overwritten each time
# you run the script.


def data_write():
    target = open("test_output.txt", "r")
    file_new = open("data_output.txt", "w")

    for line in target:
        if "SLOT_1" in line and "'(SLOT_1)'"not in line:
            slot_line = line
            file_new.write(slot_line + "\n")
        elif "bitErrorCountHi" in line and "bitErrorCountHi" > 1000:
            bit_line = line
            file_new.write(bit_line + "\n")
        elif "frameCountLow" in line and "frameCountLow" > 1000:
            frame_line = line
            file_new.write(frame_line + "\n")
        elif "frameCountHi" in line:
            frame_line = line
            file_new.write(frame_line + "\n")
        elif "frameCountLow" in line:
            frame_line = line
            file_new.write(frame_line + "\n")
        elif "Temperature" in line:
            temp_line = line
            file_new.write(temp_line + "\n")
        else:
            if "SLOT_4" in line and "'(SLOT_4)'" not in line:
                slot_line = line
                file_new.write(slot_line + "\n")
            elif "bitErrorCountHi" in line and "bitErrorCountHi" > 1000:
                bit_line = line
                file_new.write(bit_line + "\n")
            elif "frameCountLow" in line and "frameCountLow" > 1000:
                frame_line = line
                file_new.write(frame_line + "\n")
            elif "frameCountHi" in line:
                frame_line = line
                file_new.write(frame_line + "\n")
            elif "frameCountLow" in line:
                frame_line = line
                file_new.write(frame_line + "\n")
            elif "Temperature" in line:
                temp_line = line
                file_new.write(temp_line + "\n")
    file_new.close()
