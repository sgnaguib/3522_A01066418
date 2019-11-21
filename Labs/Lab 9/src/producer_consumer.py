import city_processor
from city_processor import *


class CityOverheadTimeQueue:
    """Create a buffer that will hold the
    calculated CityOverheadTimes objects in a Queue"""

    def __init__(self):
        self.data_q = []

    def put(self, overhead_time: city_processor.CityOverheadTimes):
        """This method is responsible for adding
        to the queue. Accept an overhead_time
        parameter and append it to the list"""
        self.data_q.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        removed_times = self.data_q[0]
        del(self.data_q[0])
        return removed_times

    def __len__(self) -> int:
        return len(self.data_q)


def main():
    q = CityOverheadTimeQueue()
    db = CityDatabase(Path(Path.cwd()/'city_locations_test.xlsx'))
    for city in db.city_db:
        q.put(ISSDataRequest.get_overhead_pass(city))

    print(q.get())



if __name__ == '__main__':
    main()