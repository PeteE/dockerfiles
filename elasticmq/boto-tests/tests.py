#!/usr/bin/env python

import boto.sqs
from boto.sqs.message import Message
import os
import sys
import time

class BotoTests:
	def __init__(self):
		os.environ["BOTO_ENDPOINTS"] = "./elasticmq-endpoints.json"
		self.conn = boto.sqs.connect_to_region("elasticmq", aws_access_key_id='x', aws_secret_access_key='x', is_secure=False, port=9324)
		
	def create_queue(self, name=None):
		q = self.conn.create_queue(name)
		print("Created %s" % q)

	def list_queues(self):
		for q in self.conn.get_all_queues():
			print(q)

	def send_message(self, queue_name=None, msg=None):
		q = self.conn.lookup(queue_name)
		m = Message()
		m.set_body(msg)
		q.write(m)

	def receive_messages(self, queue_name=None, max_count=50):
		messages = []
		q = self.conn.lookup(queue_name)
		for message in q.get_messages(max_count):
			messages.append(message.get_body())
			q.delete_message(message)
		return messages

	def delete_queue(self, queue_name=None):
		q = self.conn.lookup(queue_name)
		self.conn.delete_queue(q)

if __name__ == '__main__':
	queue_name = 'test'
	tests = BotoTests()
	tests.create_queue(queue_name)
	tests.list_queues()
	
	tests.send_message(queue_name=queue_name, msg="msg1")
	tests.send_message(queue_name=queue_name, msg="msg2")
	tests.send_message(queue_name=queue_name, msg="msg3")
	
	for msg in tests.receive_messages(queue_name=queue_name, max_count=50):
		print("Received: %s" % msg)

	tests.delete_queue(queue_name)


	

