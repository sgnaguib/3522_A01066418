import city_processor
from city_processor import *
from threading import *
import time
import logging


class CityOverheadTimeQueue:
    """Create a buffer that will hold the
    calculated CityOverheadTimes objects in a Queue"""

    def __init__(self):
        self.data_q = []
        self.access_queue_lock = Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes):
        """This method is responsible for adding
        to the queue. Accept an overhead_time
        parameter and append it to the list"""

        with self.access_queue_lock:
            logging.info(
                f"Thread {current_thread().name}: lock acquired!")
            self.data_q.append(overhead_time)
            logging.info(f"Thread {current_thread().name}: "
                         f"Releasing lock!")
        logging.info(f"Thread {current_thread().name}: finishing "
            f"put")

    def get(self) -> city_processor.CityOverheadTimes:

        with self.access_queue_lock:
            if len(self.data_q) != 0:
                removed_times = self.data_q[0]
                del(self.data_q[0])
                return removed_times

    def __len__(self) -> int:
        return len(self.data_q)


class ProducerThread(Thread):

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        """This method initialized the class with a list of City
        Objects as well as a CityOverheadTimeQueue"""
        super().__init__()
        self.cities = cities
        self.q = queue

    def run(self):
        """Executes when the thread starts. It loops over each city
        and passes it to the get_overheadpass() method. It then
        add the city to the queue. After reading in five cities,
        the thread sleeps for 1 second."""
        count = 0
        for city in self.cities:
            overhead_times = ISSDataRequest.get_overhead_pass(city)
            self.q.put(overhead_times)
            count += 1
            if count == 5:
                time.sleep(1)
                print("5 passes added. Sleeping 1 second.\n")
                count = 0


class ConsumerThread(Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        """Has same queue as producerthread. data_incoming
        is initialised to True and set False after the producer
        thread has joined the main thread and finished
        processing all the cities"""
        super().__init__()
        self.data_incoming = True
        self.q = queue

    def run(self):
        while self.data_incoming or len(self.q) > 0:
            if len(self.q) == 0:
                print("Empty Queue. Sleeping 0.75 seconds\n")
                time.sleep(0.75)
            else:
                print("Getting from queue. Sleeping 0.5 seconds\n")
                print(self.q.get())
                time.sleep(0.5)


def main():
    start_time = time.time()
    logging.getLogger().setLevel(logging.INFO)

    q = CityOverheadTimeQueue()
    db = CityDatabase(Path(Path.cwd()/'city_locations.xlsx'))

    length = len(db.city_db)

    p_thread_1 = ProducerThread(db.city_db[0:int(length/3)], q)
    p_thread_2 = ProducerThread(db.city_db[int(length/3):int((2*length)/3)], q)
    p_thread_3 = ProducerThread(db.city_db[int((2 * length / 3)):length], q)
    c_thread_1 = ConsumerThread(q)
    # c_thread_2 = ConsumerThread(q)
    # c_thread_3 = ConsumerThread(q)

    p_thread_1.start()
    p_thread_2.start()
    p_thread_3.start()
    c_thread_1.start()
    # c_thread_2.start()
    # c_thread_3.start()

    p_thread_1.join()
    p_thread_2.join()
    p_thread_3.join()

    c_thread_1.data_incoming = False
    # c_thread_2.data_incoming = False
    # c_thread_3.data_incoming = False

    c_thread_1.join()
    # c_thread_2.join()
    # c_thread_3.join()

    end_time = time.time()

    print(f"Execution Time: {end_time-start_time}")


if __name__ == '__main__':
    main()