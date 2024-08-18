#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time


class PingProcessor:
    def start(self):
        print("ping_cell_thread start to run")
        self.ping_cell_thread = threading.Thread(target=self.__ping_cell_thread)
        self.ping_cell_thread.start()

    def __ping_cell_thread(self):
        while True:
            self.primes(1000000)
            time.sleep(0.0001)

    def primes(self, n):
        if n == 2:
            return [2]
        elif n < 2:
            return []
        s = []
        for i in range(3, n + 1):
            if i % 2 != 0:
                s.append(i)
        mront = n ** 0.5
        half = (n + 1) / 2 - 1
        i = 0
        m = 3

        while m <= mront:
            if s[i]:
                j = (m * m - 3) / 2
                s[j] = 0
                while j < half:
                    s[j] = 0
                    j += m
            i = i + 1
            m = 2 * i + 3
        l = [2]
        for x in s:
            if x:
                l.append(x)
        return l


class Main:
    def run(self):
        print("cbs_diskmon_framework start to run")
        self.__run_service()
        self.collect_end_time = time.time()
        self.tmp_time = time.time()
        self.flag = True

        while self.flag:
            self.start_ts = time.time()
            try:
                self.primes2(1000000)
                time.sleep(0.0001)
            except:
                pass
            if self.start_ts - self.tmp_time >= 1 * 60:
                print("end")
                self.flag = False

    def __run_service(self):
        p = PingProcessor()
        p.start()

    def primes2(self, n):
        if n == 2:
            return [2]
        elif n < 2:
            return []
        s = []
        for i in range(3, n + 1):
            if i % 2 != 0:
                s.append(i)
        mront = n ** 0.5
        half = (n + 1) / 2 - 1
        i = 0
        m = 3

        while m <= mront:
            if s[i]:
                j = (m * m - 3) / 2
                s[j] = 0
                while j < half:
                    s[j] = 0
                    j += m
            i = i + 1
            m = 2 * i + 3
        l = [2]
        for x in s:
            if x:
                l.append(x)
        return l


def main():
    m = Main()
    m.run()


if __name__ == '__main__':
    main()
