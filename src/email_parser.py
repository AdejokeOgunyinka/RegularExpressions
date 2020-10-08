import re


class EmailParser:
    pattern = r'(^[a-zA-Z][a-zA-Z0-9]+[\+]*[a-zA-Z0-9]+)@([a-zA-Z]([a-zA-Z0-9]+.com))'  # Provide email pattern here ...
    keys = ['username', 'domain']

    @classmethod
    def parse(cls, email):
        """ This function takes in an email address(a string) and then splits it using a regular expression into
        the username part before @, and the domain name part at the end of the email string."""
        pattern = re.compile(cls.pattern)

        # save the keys into another variable
        # create an empty dictionary to store the search values
        if not type(email) is str:
            return None
        else:
            dictionary = {}
            search_result = re.search(pattern, email)

            if search_result is None:
                return search_result

            else:
                # Loop through the keys and assign them to the two values and save them to the dictionary
                for _ in cls.keys:
                    dictionary[cls.keys[0]] = search_result.group(1)
                    dictionary[cls.keys[1]] = search_result.group(2)
                return dictionary

