import argparse
import json

import cloudinary
import cloudinary.uploader
import cloudinary.api

EVENTS_FOLDER = "ComSSA-Website/events"


def parse_args():
    parser = argparse.ArgumentParser(description="Cloudinary CLI app")
    parser.add_argument("--cloud-name", required=True, help="Cloud name for Cloudinary")
    parser.add_argument("--api-key", required=True, help="API key for Cloudinary")
    parser.add_argument("--api-secret", required=True, help="API secret for Cloudinary")
    parser.add_argument(
        "--mode",
        choices=["folder", "url"],
        required=True,
        help="""Operation mode. Either 'folder' for getting all event folders into a JSON file, or 
        'url' for getting all event urls from an ordered JSON file and populating the image url fields.""",
    )
    parser.add_argument(
        "--in",
        "-i",
        required=False,
        type=str,
        default="./events.json",
        help="Path to input JSON file (containing event folders) for 'url' mode.",
    )
    parser.add_argument(
        "--out",
        "-o",
        required=False,
        type=str,
        default="./events.json",
        help="Path to output resulting JSON file",
    )

    args = parser.parse_args()

    return args.__dict__


def main(args: dict):
    # Configure cloudinary
    cloudinary.config(
        cloud_name=args["cloud_name"],
        api_key=args["api_key"],
        api_secret=args["api_secret"],
    )

    json_dict: dict

    if args["mode"] == "folder":  # Get subfolders mode
        # Get all subfolders
        subfolders_result = cloudinary.api.subfolders(EVENTS_FOLDER + "/")
        event_folders: list[str] = [
            subfolder["path"] for subfolder in subfolders_result["folders"]
        ]

        json_dict = {"events": []}

        print("Got the following event folders:")
        for event_folder in event_folders:
            print(event_folder)

        for event_folder in event_folders:
            # Create a properly cased event name for each event (NOTE this may have to be manually adjusted in the JSON)
            event_folder_name = event_folder.split("/")[-1]
            event_name = event_folder_name.replace("-", " ").title()

            json_dict["events"].append(
                {
                    "folder": event_folder,
                    "name": event_name,
                }
            )

    elif args["mode"] == "url":  # Populate urls mode
        with open(args["in"], "r") as in_file:
            json_dict = json.load(in_file)

        for event in json_dict["events"]:
            event_folder = event["folder"]

            # Get images within the event folder
            resources_result = cloudinary.api.resources(
                type="upload", prefix=event_folder + "/"
            )
            event_image_urls: list[str] = [
                resource["secure_url"] for resource in resources_result["resources"]
            ]

            # Apply extra parsing
            event_image_urls: list[str] = [
                ".".join(url.split(".")[:-1]) + ".webp" for url in event_image_urls
            ]

            # TODO some extra parsing here (webp, image size)

            event["imageUrls"] = event_image_urls

    # No matter what we did, save the output json to the '--out' location
    print(f"Writing output to '{args['out']}'...")
    with open(args["out"], "w") as f:
        json.dump(json_dict, f)

    print("Done. Goodbye!")


if __name__ == "__main__":
    args = parse_args()

    main(args)
