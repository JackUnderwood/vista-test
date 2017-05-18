from html.parser import HTMLParser

__author__ = 'John Underwood'


class VtfHtmlParser(HTMLParser):
    data = []
    _sub = {}
    _index = 0
    _count = 0

    def handle_starttag(self, tag, attributes):
        self._sub = {}
        if self._count is 0:
            self.data.append([])
        self._count += 1
        self.data[self._index].append(tag)
        # print("Start tag:", tag)
        for attr in attributes:
            # print("     attr:", attr)
            self._sub[attr[0]] = attr[1]
        self.data[self._index].append(self._sub)

    def handle_endtag(self, tag):
        # print("END TAG :", tag)
        # print("SUB     : {}".format(self._sub, ))
        self._count -= 1
        if self._count < 0:
            self._count = 0
        if self._count == 0:
            self._index += 1
        # print("INDEX: {}".format(self._index, ))
        # print("COUNT: {}".format(self._count, ))

    def handle_data(self, data):
        # print("Data     :", data)
        self._sub['data'] = data
