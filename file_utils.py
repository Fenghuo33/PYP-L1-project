SEPARATOR = ','

def append_file(file_name, *args):
    """
    :param file_name: A string of the file name e.g. 'user.txt'
    :param args: Set of strings to be written at the end of the file (separated with commas)
    :return: None
    """
    with open(file_name, 'a') as file:
        data = SEPARATOR.join(args)
        #writes the data in comma-separated strings and add a new line
        file.write(data + '\n')

def search_in_file(file_name, **kargs):
    """
    :param file_name: A string of the file name e.g. 'user.txt'
    :param kargs: A set of keys to check e.g. name = 'Lim'. Left empty would return all rows (including the headers)
    :return: A list of lists, where each inner list is a row of data (use this with a [0] if only one result is expected)

    ***PLEASE USE [0] IF ONLY ONE ROW OF DATA IS EXPECTED, THIS RETURNS A LIST OF LISTS***
    Used like a select statement in SQL: \n
    SELECT * FROM file_name \n
    WHERE kargs.key = kargs.value
    """

    result = []
    with open(file_name, 'r') as file:
        #reads header
        header = file.readline().strip().split(SEPARATOR)
        #index the header to their positions
        column_index = {x:i for i,x in enumerate(header)}

        for line in file:
            #splits line into a list of data
            data = line.strip().split(SEPARATOR)
            # checks for the conditions
            if not kargs or all(column in column_index and data[column_index[column]] == str(target) for column, target in kargs.items()):
                result.append(data)   # appends the whole row to result
    return result  # return the whole result


def update_file(file_name, update_data: dict, target_data: dict):
    """
    :param file_name: A string of the file name e.g. 'user.txt'
    :param update_data: A set of new data to update -> {column_name:value} like SET column_name = value in SQL.
    Can have multiple inputs -> only valid with headers would be updated
    :param target_data: A set of conditions to check -> {column_name:value} like WHERE column_name = value in SQL.
    Can have multiple inputs -> only change when all inputs are matched
    :return: An integer of updated times (0 if no update happen)
    """

    #for returning update count
    update_count = 0

    with open(file_name, 'r') as file:
        #reads the file and cache it
        orig_lines = file.readlines()

    #reserve the first line as header
    result_lines = orig_lines[0]
    header = orig_lines[0].strip().split(SEPARATOR)
    #index the header to their positions
    column_index = {x: i for i, x in enumerate(header)}

    #[1:] to skip the first line (which is header)
    for line in orig_lines[1:]:
        #splits the line into data
        data = line.strip().split(SEPARATOR)
        #checks the conditions
        if all(target_column in column_index and data[column_index[target_column]] == str(target) for target_column, target in target_data.items()):
            #updates all column that needs an update in that line
            for update_column, new_data in update_data.items():
                #checks the column_name is in the header
                if update_column in column_index:
                    #update the data (str to change int into string for values like age)
                    data[column_index[update_column]] = str(new_data)
            #actually write the updated data to result
            result_lines += SEPARATOR.join(data) + '\n'
            #increment the updated rows
            update_count += 1
        else:
            #simply add the original line if it does not match the conditions
            result_lines += line

    #actually writes the updated lines into the text file
    with open(file_name, 'w') as file:
        file.writelines(result_lines)

    return update_count