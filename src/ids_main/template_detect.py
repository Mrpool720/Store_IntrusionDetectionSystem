from keywords import Keyword

class MatchTemplate:

    def __init__(self, template):
        self.template = template

    def checkMatch(self, query):
        keyword = Keyword()

        if len(query.split()) == 0:
            return True

        key = query.split()[0].upper()
        queryTemplate = keyword.getKeyword(key)
        queryTemplate.parse(query)

        if key not in self.template:
            print("OOPS")
            return False
        print("result ", queryTemplate == self.template[key])
        return queryTemplate == self.template[key]