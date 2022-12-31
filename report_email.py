import json
import reports
import os
import emails
from datetime import datetime

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  # return a list of dictionaries
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def process_data(data):
    output_list = []
    for fruit_dict in data:
        output_list.append( "name: {}<br/>weight: {} lbs<br/>".format(fruit_dict["name"], fruit_dict["weight"]))

    return output_list



def main():
  """Process the JSON data and generate a full report out of it."""
  data = load_data("fruits.json")
  report_data = process_data(data)
  print(report_data) #is a list

  # generate pdf report
  now = datetime.now()
  now_str = now.strftime("%B %d, %Y ")
  reports.generate_report("fruits.pdf", "Process update on {}".format(now_str), "<br/>".join(report_data))


  # send an email
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate(sender, receiver, subject, body, "/tmp/fruits.pdf")
  emails.send(message)

if __name__ == "__main__":
  main()