
class ParseUtility(object):

    def text_file_to_list_of_lists(self, filename):
        with open(filename) as my_file:
            raw_data = my_file.readlines()
        return raw_data

    def list_of_lists_to_dictionary(self, data_source, delimiter):
        raw_column_names = data_source[0]
        raw_column_names = raw_column_names.replace("\n", "")
        raw_column_names = raw_column_names.lower()
        del data_source[0]  # remove column names from raw data source after they have been pulled

        column_list = raw_column_names.split(delimiter)
        parsed_dataset = []
        for row in data_source:
            parsed_row = row.split(delimiter)
            column_counter = 0
            row_dictionary = {}

            for cell in parsed_row:
                row_dictionary[column_list[column_counter]] = cell
                column_counter += 1
            parsed_dataset.append(row_dictionary)
        return parsed_dataset

    def load_data(self, filename, delimiter):
        list_of_lists = self.text_file_to_list_of_lists(filename)
        list_of_dictionaries = self.list_of_lists_to_dictionary(list_of_lists, delimiter)
        return list_of_dictionaries

    def select_row_from_list_of_dictionaries(self, data_source, column_name, select_unique=False):
        query_result = []
        for row in data_source:
            query_result.append(row[column_name])
        return query_result

    def clean_list(self, list_of_string_values, convert_datatype_to="float"):
        list_without_blanks = [x for x in list_of_string_values if x != ""]
        if convert_datatype_to == "float":
            clean_list = [float(i) for i in list_without_blanks]
        elif convert_datatype_to == "float":
            clean_list = [int(i) for i in list_without_blanks]
        else:
            clean_list = "NULL"
        return clean_list
