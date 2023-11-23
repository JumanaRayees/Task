#write a Python code to transform the data from input to result....

#import library
import json

# Read input from JSON file
with open("task.json", "r") as file:
     data = json.load(file)


# Transform the data from "task.json" file
transformed_data = []

for entry in data:
    transformed_entry = {
        "id": entry["id"],
        "title": entry["data"]["title"],
        "annotations": []
    }

    for annotation in entry["annotations"]:
        transformed_annotation = {
            "id": annotation["id"],
            "completed_by": annotation["completed_by"],
            "result": []
        }

        for result_entry in annotation["result"]:
            transformed_result_entry = {
                "id": result_entry["id"],
                "label": result_entry["value"]["labels"][0],  # Assuming only one label per result
                "start": result_entry["value"]["start"],
                "end": result_entry["value"]["end"]
            }

            transformed_annotation["result"].append(transformed_result_entry)

        transformed_entry["annotations"].append(transformed_annotation)

    transformed_data.append(transformed_entry)

# Print the transformed data
print("result =", transformed_data)
