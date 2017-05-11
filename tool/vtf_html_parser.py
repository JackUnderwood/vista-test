from html.parser import HTMLParser

__author__ = 'John Underwood'


class VtfHtmlParser(HTMLParser):
    data = []
    sub = {}
    count = 0
    change = None

    def handle_starttag(self, tag, attributes):
        self.sub = {}
        self.data.append([])
        self.data[self.count].append(tag)
        # print("Start tag:", tag)
        for attr in attributes:
            # print("     attr:", attr)
            self.sub[attr[0]] = attr[1]
        self.data[self.count].append(self.sub)

    def handle_endtag(self, tag):
        # print("End tag  :", tag)
        # print("SUB_DATA: {}".format(self.sub, ))
        # print("COUNT: {}".format(self.count, ))
        self.count += 1

    def handle_data(self, data):
        # print("Data     :", data)
        self.sub['data'] = data
