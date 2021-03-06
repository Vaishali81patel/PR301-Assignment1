from cmd import Cmd


class InterpreterController(Cmd):

    def __init__(self, in_view, in_interpreter):
        Cmd.__init__(self)
        self.prompt = '> '
        self.my_view = in_view
        self.my_interpreter = in_interpreter

    def do_add(self, *args):
        # Vaishali
        """ *** OPTIONS
            -l : This loads the information from a file.
                 The file is given to the command as a string.
            -m : This is for manual data entry. The user will be
                 prompted for the information in steps
                 after entering this option.
            -d : This loads the information into the system from a database.
        *** """

        options_arr = self.parse_args(args)
        option_dict = {
            '-l': self.my_interpreter.load_file,
            '-m': self.manual_add,
            '-d': self.my_interpreter.load_database
        }
        self.find_in_dict(options_arr, option_dict)

    def do_save(self, *args):
        # Vaishali
        """ *** OPTIONS
            -s : This is a standard save. The information
                 is saved to a file in the saves folder in the program files.
                 (object is serialized)
            -d : This saves the current information to the database.
            -f : This saves a file to the specified file location.
        *** """
        options_arr = self.parse_args(args)
        option_dict = {
            '-s': self.my_interpreter.save_file,
            '-d': self.my_interpreter.save_database,
            '-f': self.my_interpreter.serialize_data_arr
        }
        self.find_in_dict(options_arr, option_dict)

    def do_show(self, *args):
        """ *** OPTIONS
                    -a : Shows a bar graph of the total sales made
                         by males verse the total sales made by female.
                    -b : Shows a pie chart of the percentage of female
                         workers verse male workers
                    -c : Shows a scatter plot graph of peoples
                    -d : Shows a pie chart of the BMI of a set of people.
        *** """
        options_arr = self.parse_args(args)
        option_dict = {
            '-a': self.my_view.sales_by_gender_graph
            (self.my_interpreter.get_data()),
            '-b': self.my_view.employees_by_gender_graph
            (self.my_interpreter.get_data()),
            '-c': self.my_view.ages_verse_salary_graph
            (self.my_interpreter.get_data()),
            '-d': self.my_view.bmi_pie_graph(self.my_interpreter.get_data())
        }
        self.find_in_dict(options_arr, option_dict)

    def do_quit(self, *args):
        quit()

    do_q = do_quit

    def parse_args(self, arg_str):
        for arg in arg_str:
            arg_arr = arg.split(' ')
        if len(arg_arr) > 2:
            return "Too many arguments were given"
        else:
            return arg_arr

    def manual_add(self):
        self.my_interpreter.add_manual_data(self.my_view.manual_person_flow())

    def load_file(self):
        pass

    def find_in_dict(self, options_arr, options_dict):
        arg_found = False
        for key, value in options_dict.items():
            if options_arr[0] == key:
                arg_found = True
                if not self.try_launch(key, value, options_arr):
                    self.my_view.show("command FAILED")
                else:
                    self.my_view.show("SUCCESS")
        if not arg_found:
            self.my_view.show("That option doesnt work with the given command")

    def try_launch(self, key, value, options_arr):
        if (key == '-m'):
            value()
            return True
        else:
            if len(options_arr) == 2:
                value(options_arr[1])
                return True
            else:
                self.my_view.show("Incorrect amount of arguments")
                return False

