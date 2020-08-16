#!/usr/bin/env python3

import sys
import numpy
import locale
import os

def main(args, arg_count):
  locale.setlocale(locale.LC_ALL, '')

  if arg_count < 4:
    print("Invalid amount of arguments. Expected at least the two output files and two log files: ./logs-parse.py output_client.log output_final.log twin.log client.log")
    return 1

  output_client = args[0]
  output_final = args[1]
  twin = args[2]
  clients = args[3:]

  if os.path.exists(output_client):
    os.remove(output_client)

  if os.path.exists(output_final):
    os.remove(output_final)

  parse_clients(clients, output_client)
  parse_twin(twin, output_client, output_final)

def parse_twin(twin, output_client, output_final):
  print("Parsing twin:", twin)

  num_lines = sum(1 for line in open(twin)) + 1

  input_file = open(twin, 'r') 
  count = 0

  total_messages_found = 0

  output_client_file = open(output_client, 'r')
  output_final_file = open(output_final, 'w')

  while True: 
    count += 1
    line = input_file.readline() 

    if count % 1000 == 0:
      print("{:.2f}% - {}/{} lines".format((count / num_lines * 100), count, num_lines))

    if not line:
      print("{:.2f}% - {}/{} lines".format((count / num_lines * 100), count, num_lines))
      print("Total messages found: {}".format(total_messages_found))
      break

    split_line = line.split()
    if len(split_line) == 7 and split_line[5] != "Twin:":
      end_date = split_line[0]
      payload = (split_line[5] + " " + split_line[6]).strip("\"")

      client_line = 0
      found = False
      while found != True:
        output_line = output_client_file.readline()
        if payload in output_line:
          start_date = output_line.split()[0]
          output_final_file.write(start_date + "," + end_date + "," + payload + "\n")
          total_messages_found += 1
          output_client_file.seek(0)
          found = True
      
        if not output_line:
          found = True
        else:
          client_line += 1
      
      output_client_file.seek(0)

  input_file.close()
  output_client_file.close()
  output_final_file.close()

  print("Done parsing twin", twin)
  
  return

def parse_client(client, output):
  print("Parsing client:", client)
  output_file = open(output, 'a')

  input_file = open(client, 'r') 
  count = 0
  
  while True: 
    count += 1
    line = input_file.readline() 

    if not line:
      break

    split_line = line.split()
    if len(split_line) == 7:
      date = split_line[0]
      payload = (split_line[5] + " " + split_line[6]).strip("\"")

      output_file.write(date + " " + payload + "\n")
  
  input_file.close()
  output_file.close()
  print("Done parsing client:", client)

def parse_clients(clients, output):
  print("Parsing {} clients.".format(len(clients)))

  for client in clients:
    parse_client(client, output)  

if __name__ == '__main__':
  main(sys.argv[1:], len(sys.argv) - 1)
