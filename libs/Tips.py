class Remove:
    """去除重复目标IP"""

    def __init__(self, ipList):
        self.ipList = ipList

    def list_remove_repeat(self):
        afterRemoveList = []
        for ip in self.ipList:
            if ip not in afterRemoveList:
                afterRemoveList.append(ip)
        return afterRemoveList