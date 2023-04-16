# python3
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long

class PhonebookQuery:
    ACTION_ADD = 'add'
    ACTION_FIND = 'find'
    ACTION_REMOVE = 'del'

    actions = [
        ACTION_ADD,
        ACTION_FIND,
        ACTION_REMOVE
    ]

    def __init__(self, query):
        self.action = query[0]
        self.number = int(query[1])

        if self.action not in self.actions:
            return

        if self.action == self.ACTION_ADD:
            self.number_alias = query[2] # dynamic prop lol

    def get_action(self):
        print(self.action)
        return self.action

    def get_number(self):
        return self.number

    def get_alias(self):
        return self.number_alias

    def log(self):
        return [self.action, self.number, getattr(self, 'number_alias', None)]

class Phonebook: # methods will return appropriate messages in case something goes wrong in given constraints, (ex. not found)
                 # later will be processed in process_queries() method
    def __init__(self):
        self.entries = {} # no phonebook import support sorry not sorry

    def add_entry(self, number, alias):
        self.entries[number] = alias # not using built-in dict methods just for fun

    def del_entry(self, number):
        if number in self.entries:
            del self.entries[number]

    def get_entry(self, number):
        if number in self.entries:
            return self.entries[number]

        return 'not found'

def read_queries():
    query_amount = int(input())
    # this is overall very dirty but since we only need to solve the problem via simple script i guess its ok
    return [PhonebookQuery(input().split()) for i in range(query_amount)]

def show_results(result):
    if not result:
        return

    print('\n'.join(result))

def process_queries(queries, phonebook):
    results = []

    for query in queries:
        queried_number = query.get_number()

        match query.get_action():
            case PhonebookQuery.ACTION_ADD:
                phonebook.add_entry(queried_number, query.get_alias())
            case PhonebookQuery.ACTION_FIND:
                results.append(phonebook.get_entry(queried_number))
            case PhonebookQuery.ACTION_REMOVE:
                if not phonebook.get_entry(queried_number):
                    return

                phonebook.del_entry(queried_number)


    print(results)
    return results



if __name__ == '__main__':
    phonebook = Phonebook()
    show_results(
        process_queries(read_queries(), phonebook)
    )