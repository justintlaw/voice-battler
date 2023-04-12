import os
import asyncio
import websockets
import json
import speech_recognition as sr

from time import perf_counter
from queue import Queue
import threading

from parse_command import parse_command

q_commands = Queue()

async def get_command():
  await asyncio.sleep(0.1)

  try:
    command = q_commands.get(block=False, timeout=0.1)
    if command:
      print("command", command)

      return json.dumps(command)
  except:
    pass

  # print("getting command")
  # await asyncio.sleep(5)

  # command = {
  #   "action": "move",
  #   "destination": "mines"
  # }
  # print("command received")
  # return json.dumps(command)

async def handler(websocket, path):
  while True:
    # try:
    #   print("hello1!!!")
    #   # data = await websocket.recv()
    # except websockets.ConnectionClosed:
    #   print("Connection closed.")
    #   break

    command = await get_command()

    try:
      if command:
        await websocket.send(command)
        print("SENT", command)
    except websockets.ConnectionClosedError:
      print("Connection closed.")
      break


def listen():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    # r.energy_threshold = 300
    print("new energy threshold is", r.energy_threshold)
    while(True):
      # audio = r.record(source)
      audio = r.listen(source, phrase_time_limit=5)

      try:
        text = r.recognize_google(audio)
      except:
        text = None

      if text is not None:
        print("text", text)
        command = parse_command(text)
        print("command", command)
        if command:
          q_commands.put(command.toJson())


async def start_server():
  server = await websockets.serve(handler, "localhost", 8765)
  await server.wait_closed()

  
def websocket():
  asyncio.run(start_server())


if __name__ == "__main__":
  if os.environ.get("voiceonly", "false").lower() == "true":
    listen()
  else:
    server = threading.Thread(target=websocket, daemon=True)
    server.start()
    voice_listener = threading.Thread(target=listen)
    voice_listener.start()
    voice_listener.join(timeout=3)
