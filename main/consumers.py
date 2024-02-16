
import os
from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import asyncio

class LoggerConsumer(AsyncJsonWebsocketConsumer):
   
            
    def last_10_lines(self):
        lines = []
        
        with open(self.log_file_path) as f:
            while len(lines) <= 10:
                try:
                    f.seek(-11, 2)
                except IOError:
                    f.seek(0)
                    break
                finally:
                    lines = list(f)
                pos *= 2
            self.last_line = f.tell()
        return lines[-10:]

    async def connect(self):
        self.log_file_path = os.path.join(settings.BASE_DIR, 'test.log')
        await self.accept()
        await self.send_last_ten_logs()
        while(True):
            await asyncio.sleep(1)
            with open(self.log_file_path,'r') as f:
                f.seek(0,os.SEEK_END)
                last_pos = f.tell()
                if last_pos <self.last_line:
                    continue
                f.seek(self.last_line)
                for l in f:
                    await self.send(l)
                self.last_line = f.tell()
            print(self.last_line)



    async def disconnect(self, close_code):
        pass

    async def send_last_ten_logs(self):
        last_lines = self.last_10_lines()
        print(last_lines)
        for l in last_lines:
            await self.send(l)
        # with open(self.log_file_path,'r') as f:
        #     lines = f.readlines()
        #     # print(lines[-1])
        #     for l in lines[-10:]:
        #         await self.send(l)
        #     self.last_line = f.tell()
        #     print(self.last_line)