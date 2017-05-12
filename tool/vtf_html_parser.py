from html.parser import HTMLParser

__author__ = 'John Underwood'


class VtfHtmlParser(HTMLParser):
    data = []
    _sub = {}
    _count = 0

    def handle_starttag(self, tag, attributes):
        self._sub = {}
        self.data.append([])
        self.data[self._count].append(tag)
        # print("Start tag:", tag)
        for attr in attributes:
            # print("     attr:", attr)
            self._sub[attr[0]] = attr[1]
        self.data[self._count].append(self._sub)

    def handle_endtag(self, tag):
        # print("End tag  :", tag)
        # print("SUB_DATA: {}".format(self.sub, ))
        # print("COUNT: {}".format(self.count, ))
        self._count += 1

    def handle_data(self, data):
        # print("Data     :", data)
        self._sub['data'] = data
