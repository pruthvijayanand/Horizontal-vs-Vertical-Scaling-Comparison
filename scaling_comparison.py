import json
from datetime import datetime


def get_horizontal_scaling_details():
    return {
        "name": "Horizontal Scaling",
        "meaning": "Adding more servers or machines to handle increased traffic.",
        "example": "Adding Server_1, Server_2, and Server_3 behind a load balancer.",
        "advantages": [
            "High availability",
            "Better fault tolerance",
            "Can handle large traffic",
            "Easy to scale for cloud applications"
        ],
        "disadvantages": [
            "More complex setup",
            "Needs a load balancer",
            "Data synchronization can be difficult"
        ],
        "best_for": "Web applications, cloud platforms, and large-scale systems"
    }


def get_vertical_scaling_details():
    return {
        "name": "Vertical Scaling",
        "meaning": "Increasing CPU, RAM, or storage capacity of one existing server.",
        "example": "Upgrading a server from 4 GB RAM to 16 GB RAM.",
        "advantages": [
            "Simple to implement",
            "No major architecture changes",
            "Good for small applications"
        ],
        "disadvantages": [
            "Limited hardware capacity",
            "Single point of failure",
            "May require downtime during upgrade"
        ],
        "best_for": "Small applications, databases, and early-stage projects"
    }


def compare_scaling():
    horizontal = get_horizontal_scaling_details()
    vertical = get_vertical_scaling_details()

    return {
        "report_generated": True,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "comparison": {
            "horizontal_scaling": horizontal,
            "vertical_scaling": vertical
        }
    }


def main():
    try:
        with open("input.json", "r") as file:
            input_data = json.load(file)

        print("Input received:")
        print(json.dumps(input_data, indent=4))

        result = compare_scaling()

        print("\nScaling Comparison Result:")
        print(json.dumps(result, indent=4))

        with open("output.json", "w") as output_file:
            json.dump(result, output_file, indent=4)

        print("\nSuccess: output.json created successfully.")

    except FileNotFoundError:
        print("Error: input.json file not found.")

    except json.JSONDecodeError:
        print("Error: input.json contains invalid JSON.")


if __name__ == "__main__":
    main()